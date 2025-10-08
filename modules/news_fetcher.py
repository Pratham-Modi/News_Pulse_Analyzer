import requests
import pandas as pd
from config import NEWS_API_KEY, NEWSDATAIO_API_KEY, NEWS_CACHE_FILE, DEFAULT_NEWS_LANGUAGE

# -----------------------------
# Column normalization helpers
# -----------------------------
def normalize_newsapi_columns(df):
    if df.empty:
        return df
    df = df.rename(columns={
        "title": "title",
        "description": "content",
        "content": "content_full",
        "publishedAt": "published_at",
        "source": "source_info",
        "url": "url",
        "author": "author"
    })
    if "source_info" in df.columns:
        df["source"] = df["source_info"].apply(lambda x: x.get("name") if isinstance(x, dict) else x)
        df = df.drop(columns=["source_info"])
    df["language"] = df.get("language", "en")  # Default English
    return df

def normalize_newsdataio_columns(df):
    if df.empty:
        return df
    df = df.rename(columns={
        "title": "title",
        "content": "content",
        "pubDate": "published_at",
        "link": "url",
        "source_id": "source",
        "creator": "author",
        "language": "language"
    })
    if "language" not in df.columns:
        df["language"] = "en"  # Default English
    return df

# -----------------------------
# Fetching functions
# -----------------------------
def fetch_news_newsapi(category="general", language=DEFAULT_NEWS_LANGUAGE, page_size=20):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": NEWS_API_KEY,
        "category": category,
        "language": language,
        "pageSize": page_size
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data.get("status") != "ok":
        return pd.DataFrame()
    df = pd.DataFrame(data.get("articles", []))
    df["language"] = language  # Tag all articles with requested language
    return normalize_newsapi_columns(df)

def fetch_news_newsdataio(country="in", language=DEFAULT_NEWS_LANGUAGE, category="general", page_size=20):
    url = "https://newsdata.io/api/1/news"
    params = {
        "apikey": NEWSDATAIO_API_KEY,
        "country": country,
        "language": language,
        "category": category,
        "page": 0
    }
    all_articles = []
    while len(all_articles) < page_size:
        response = requests.get(url, params=params)
        data = response.json()
        results = data.get("results", [])
        if not results:
            break
        all_articles.extend(results)
        params["page"] += 1
    df = pd.DataFrame(all_articles[:page_size])
    df["language"] = language  # Tag all articles
    return normalize_newsdataio_columns(df)

# -----------------------------
# Combined function with language-based API selection
# -----------------------------
INDIAN_LANGUAGES = [
    "hi", "mr", "ta", "te", "kn", "ml", "gu", "pa", "or", "bn", "ur"
]

def get_all_news(category="general", language=DEFAULT_NEWS_LANGUAGE):
    """
    Fetch news according to language:
    - Indian languages -> NewsData.io
    - Foreign languages -> NewsAPI
    - English/Hindi -> both APIs
    """
    df_newsapi, df_newsdataio = pd.DataFrame(), pd.DataFrame()
    
    # English/Hindi: both APIs
    if language in ["en", "hi"]:
        df_newsapi = fetch_news_newsapi(category, language)
        df_newsdataio = fetch_news_newsdataio(language=language, category=category)
    # Indian languages: NewsData.io only
    elif language in INDIAN_LANGUAGES:
        df_newsdataio = fetch_news_newsdataio(language=language, category=category)
    # Foreign languages: NewsAPI only
    else:
        df_newsapi = fetch_news_newsapi(category, language)

    # Combine results
    df_combined = pd.concat([df_newsapi, df_newsdataio], ignore_index=True)
    
    # Cache locally
    df_combined.to_json(NEWS_CACHE_FILE, orient="records", force_ascii=False)
    
    return df_combined
