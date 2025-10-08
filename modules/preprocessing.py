import pandas as pd
import re
import nltk
import spacy
from nltk.corpus import stopwords

# Download NLTK data
nltk.download("stopwords")
nltk.download("punkt")

# Load English spaCy model
nlp_en = spacy.load("en_core_web_sm")

# Stopwords dictionary for supported languages
STOPWORDS_DICT = {
    "en": set(stopwords.words("english")),
    "hi": set(nltk.corpus.stopwords.words("hindi")) if "hindi" in nltk.corpus.stopwords.fileids() else set(),
    # Add more languages if needed with appropriate stopwords
}

def clean_text(text: str) -> str:
    """Clean text: lowercasing, remove URLs, punctuation, extra spaces."""
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove punctuation
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    return text

def tokenize_and_lemmatize(text: str, lang="en") -> tuple:
    """
    Tokenize and lemmatize text based on language.
    Returns tokens and lemmas.
    """
    if lang == "en":
        doc = nlp_en(text)
        tokens = [token.text for token in doc if token.text not in STOPWORDS_DICT.get(lang, set())]
        lemmas = [token.lemma_ for token in doc if token.text not in STOPWORDS_DICT.get(lang, set())]
    else:
        # For other languages, basic tokenization and lowercasing
        tokens = [word for word in nltk.word_tokenize(text)]
        lemmas = tokens  # No proper lemmatization without language-specific models
    return tokens, lemmas

def preprocess_news(df: pd.DataFrame, text_column="content", lang_column="language") -> pd.DataFrame:
    """
    Apply cleaning, tokenization, and lemmatization.
    Adds 'cleaned_text', 'tokens', 'lemmas' columns.
    """
    df = df.copy()
    
    # Determine language per row
    if lang_column not in df.columns:
        df[lang_column] = "en"  # default
    
    df["cleaned_text"] = df[text_column].apply(clean_text)
    
    tokens_list = []
    lemmas_list = []
    
    for idx, row in df.iterrows():
        lang = row[lang_column] if row[lang_column] in STOPWORDS_DICT else "en"
        tokens, lemmas = tokenize_and_lemmatize(row["cleaned_text"], lang)
        tokens_list.append(tokens)
        lemmas_list.append(lemmas)
    
    df["tokens"] = tokens_list
    df["lemmas"] = lemmas_list
    
    return df
