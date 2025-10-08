import pandas as pd
import spacy

# Load multilingual spaCy NER model (supports 50+ languages)
nlp = spacy.load("xx_ent_wiki_sm")  

def extract_entities(df, text_column="cleaned_text"):
    """
    Extract named entities from news articles (multi-language).
    
    Parameters:
        df (pd.DataFrame): DataFrame containing news articles.
        text_column (str): Column name containing preprocessed text.
    
    Returns:
        pd.DataFrame: Original DataFrame with additional 'entities' column.
    """
    df = df.copy()
    
    entities_list = []
    for doc in nlp.pipe(df[text_column].tolist(), disable=["tagger", "parser", "lemmatizer"]):
        # Extract entities as (text, label)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        entities_list.append(entities)
    
    df["entities"] = entities_list
    return df
