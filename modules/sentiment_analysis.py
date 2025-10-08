import pandas as pd
from transformers import pipeline

# Initialize multilingual sentiment analysis pipeline
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def analyze_sentiment(df, text_column="cleaned_text"):
    """
    Analyze sentiment of news articles, supports multiple languages.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing news articles.
        text_column (str): Column name containing preprocessed text.
    
    Returns:
        pd.DataFrame: Original DataFrame with additional 'sentiment' and 'score' columns.
    """
    df = df.copy()
    
    # Replace empty text with neutral placeholder to avoid errors
    df[text_column] = df[text_column].fillna("No content")
    
    sentiments = sentiment_pipeline(df[text_column].tolist())
    
    # Extract sentiment label and map numeric scores to Positive/Neutral/Negative
    df["sentiment"] = []
    df["score"] = []
    
    for item in sentiments:
        # For nlptown model: labels are '1 star' to '5 stars'
        stars = int(item["label"][0])
        df["score"].append(item["score"])
        if stars <= 2:
            df["sentiment"].append("Negative")
        elif stars == 3:
            df["sentiment"].append("Neutral")
        else:
            df["sentiment"].append("Positive")
    
    return df
