# data_loader/phone_review_selector.py

import pandas as pd
from ast import literal_eval

def safe_eval(value):
    try:
        if isinstance(value, str):
            return literal_eval(value)
        elif pd.isna(value):
            return []
        else:
            return list(value) if isinstance(value, list) else []
    except:
        return []

def load_top_reviews(csv_path: str = "data/sample_10_phones_aggregated.csv") -> pd.DataFrame:
    return pd.read_csv(csv_path)

def get_all_phones(df: pd.DataFrame) -> list:
    return sorted(df['normalized_product'].unique())

def get_reviews_and_scores(df: pd.DataFrame, phone: str) -> dict:
    row = df[df['normalized_product'] == phone]
    if row.empty:
        return {"phone": phone, "reviews": [], "ratings": []}

    reviews = safe_eval(row.iloc[0]['all_reviews'])
    ratings = safe_eval(row.iloc[0]['all_scores'])

    return {"phone": phone, "reviews": reviews, "ratings": ratings}
