from dotenv import load_dotenv
import os

load_dotenv()

# API Keys
NEWS_API_KEY = os.getenv("NEWS_API_KEY")           # Global news API
NEWSDATAIO_API_KEY = os.getenv("NEWSDATAIO_API_KEY")  # India-focused news API
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")      # Chatbot API

# -------------------------
# News Languages
# -------------------------
# Default language
DEFAULT_NEWS_LANGUAGE = "en"

# Languages supported by NewsAPI (global news)
NEWSAPI_LANGUAGES = [
    "en", "hi", "ar", "de", "es", "fr", "he", "it", "nl", "no", "pt", "ru", "sv", "ud", "zh"
]

# Languages supported by NewsData.io (India-focused news + English)
NEWSDATA_LANGUAGES = [
    "en", "hi", "bn", "gu", "kn", "ml", "mr", "or", "pa", "ta", "te", "ur"
]

# Combined selectable news languages for the UI
USER_SELECTABLE_NEWS_LANGUAGES = sorted(list(set(NEWSAPI_LANGUAGES + NEWSDATA_LANGUAGES)))

# -------------------------
# News Categories
# -------------------------
# Direct NewsAPI categories
NEWSAPI_CATEGORIES = [
    "business",
    "entertainment",
    "general",
    "health",
    "science",
    "sports",
    "technology"
]

# Extended categories for UI and analytics
EXTENDED_CATEGORIES = {
    "Business": ["business", "economy", "finance", "markets"],
    "Entertainment": ["entertainment", "movies", "tv", "music"],
    "General": ["general", "world", "politics", "education", "lifestyle", "culture"],
    "Health": ["health", "medicine", "wellness"],
    "Science": ["science", "research", "technology startups"],
    "Sports": ["sports"],
    "Technology": ["technology", "innovation", "startups"],
    "Environment": ["environment", "climate", "energy", "infrastructure"],
    "Travel": ["travel", "tourism"],
    "Crime": ["crime", "law"]
}

# -------------------------
# UI Languages & Text
# -------------------------
# Languages supported by UI interface
INTERFACE_LANGUAGES = [
    "English", "Hindi", "Arabic", "Bengali", "Chinese", "French", "German",
    "Gujarati", "Italian", "Kannada", "Malayalam", "Marathi", "Oriya", "Punjabi",
    "Russian", "Spanish", "Tamil", "Telugu", "Urdu"
]

# UI Translation dictionary (labels for interface)
UI_TEXT = {
    "English": {
        "login": "Login",
        "username": "Username",
        "password": "Password",
        "select_category": "Select Category",
        "language": "Language",
        "fetch_news": "Fetch News",
        "logout": "Logout"
    },
    "Hindi": {
        "login": "लॉगिन",
        "username": "यूज़रनेम",
        "password": "पासवर्ड",
        "select_category": "श्रेणी चुनें",
        "language": "भाषा",
        "fetch_news": "समाचार लाएं",
        "logout": "लॉगआउट"
    }
    # [Additional UI languages can be added here as needed]
}

# -------------------------
# Data & Cache
# -------------------------
# Local cache for fetched news to reduce API calls during testing
NEWS_CACHE_FILE = "data/news_cache.json"
