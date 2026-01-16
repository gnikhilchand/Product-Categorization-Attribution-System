import re
import pandas as pd

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess(df):
    df["clean_text"] = (
        df["title"].fillna("") + " " +
        df["description"].fillna("")
    ).apply(clean_text)
    return df
