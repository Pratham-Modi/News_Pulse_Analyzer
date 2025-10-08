import matplotlib.pyplot as plt
from wordcloud import WordCloud
import plotly.express as px
import pandas as pd
import streamlit as st

# -----------------------------
# Sentiment Pie Chart
# -----------------------------
def plot_sentiment_pie(df, sentiment_col="sentiment"):
    """Create a pie chart of sentiment distribution."""
    if df.empty or sentiment_col not in df.columns:
        st.warning("No sentiment data available for plotting.")
        return None

    sentiment_counts = df[sentiment_col].value_counts()
    fig = px.pie(
        names=sentiment_counts.index,
        values=sentiment_counts.values,
        title="Sentiment Distribution"
    )
    return fig

# -----------------------------
# Category Bar Chart
# -----------------------------
def plot_category_bar(df, category_col="category"):
    """Create a bar chart for number of articles per category."""
    if df.empty or category_col not in df.columns:
        st.warning("No category data available for plotting.")
        return None

    category_counts = df[category_col].value_counts()
    fig = px.bar(
        x=category_counts.index,
        y=category_counts.values,
        title="Articles per Category",
        labels={"x": "Category", "y": "Count"}
    )
    return fig

# -----------------------------
# Word Cloud
# -----------------------------
def generate_wordcloud(text, title="Word Cloud", max_words=100):
    """Generate and display a word cloud."""
    if not text:
        st.warning("No text provided for Word Cloud.")
        return

    wordcloud = WordCloud(width=800, height=400, background_color="white",
                          max_words=max_words).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)
    plt.tight_layout()
    st.pyplot(plt)  # Streamlit-friendly display
    plt.close()

# -----------------------------
# Timeline Plot
# -----------------------------
def plot_timeline(df, date_col="published_at", category_col="category"):
    """Plot a timeline of article counts over time."""
    if df.empty or date_col not in df.columns or category_col not in df.columns:
        st.warning("Insufficient data for timeline plotting.")
        return None

    df[date_col] = pd.to_datetime(df[date_col])
    timeline = df.groupby([date_col, category_col]).size().reset_index(name="count")
    fig = px.line(
        timeline,
        x=date_col,
        y="count",
        color=category_col,
        title="News Timeline by Category"
    )
    return fig
