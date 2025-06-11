# cleaner.py

import pandas as pd

def clean_columns_names(df):
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('[^a-z0-9_]', '', regex=True)
    )
    return df

def standardize_city_state(df):
    for col in ['city', 'state']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.title()
    return df

def drop_missing_row(df, treshold=1):
    return df.dropna(thresh=int(df.shape[1] * treshold))

def clean_dataframe(df):
    df = clean_columns_names(df)
    df = standardize_city_state(df)
    df = drop_missing_row(df)
    return df

def cleaner(datasets: dict):
    return {name: clean_dataframe(df.copy()) for name, df in datasets.items()}
