import pandas as pd
from bertopic import BERTopic

def generate_topics(df, text_column="cleaned_text", n_topics=None):
    """
    Perform topic modeling on news articles using BERTopic with multilingual embeddings.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing news articles.
        text_column (str): Column containing preprocessed text.
        n_topics (int or None): Number of topics to generate (None = automatic).
        
    Returns:
        tuple:
            - df (pd.DataFrame): Original DataFrame with a 'topic' column.
            - topic_model (BERTopic): Fitted BERTopic model object.
            - probs (list): Topic probabilities for each document.
    """
    df = df.copy()
    texts = df[text_column].tolist()
    
    # Use multilingual sentence embeddings for topic modeling
    topic_model = BERTopic(
        embedding_model="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        nr_topics=n_topics
    )
    
    topics, probs = topic_model.fit_transform(texts)
    
    # Add topic assignments to DataFrame
    df["topic"] = topics
    
    return df, topic_model, probs
