import pandas as pd
import numpy as np

def sentiment_to_score(sentiment_label):
    """
    Convert sentiment label to numerical score.
    Maps Hugging Face sentiment output to numbers.
    """
    mapping = {"POSITIVE": 1, "NEGATIVE": -1, "NEUTRAL": 0, "Positive": 1, "Negative": -1, "Neutral": 0}
    return mapping.get(sentiment_label, 0)

def detect_trends(df, date_column="published_at", topic_column="topic", sentiment_column="sentiment", window=3):
    """
    Detect trends and spikes/dips in news topics and sentiment over time.

    Parameters:
        df (pd.DataFrame): DataFrame containing news articles with topic and sentiment.
        date_column (str): Column with publication date of articles.
        topic_column (str): Column with topic assigned to each article.
        sentiment_column (str): Column with sentiment label or score.
        window (int): Rolling window size for trend calculation.

    Returns:
        pd.DataFrame: Aggregated trends per topic with rolling counts and sentiment averages.
    """
    df = df.copy()

    # Ensure date is in datetime format
    df[date_column] = pd.to_datetime(df[date_column], errors="coerce")

    # Remove rows with invalid dates
    df = df.dropna(subset=[date_column])

    # Group by topic and date
    trends = df.groupby([topic_column, date_column]).agg(
        article_count=pd.NamedAgg(column=topic_column, aggfunc="count"),
        avg_sentiment=pd.NamedAgg(column=sentiment_column, aggfunc=lambda x: np.mean([sentiment_to_score(s) for s in x]))
    ).reset_index()

    # Sort for rolling calculation
    trends = trends.sort_values(by=[topic_column, date_column])

    # Rolling averages to detect spikes/dips
    trends["rolling_count"] = trends.groupby(topic_column)["article_count"].transform(lambda x: x.rolling(window, min_periods=1).mean())
    trends["rolling_sentiment"] = trends.groupby(topic_column)["avg_sentiment"].transform(lambda x: x.rolling(window, min_periods=1).mean())

    # Flag significant spikes
    trends["spike_flag"] = trends["article_count"] > (trends["rolling_count"] * 1.5)

    return trends
