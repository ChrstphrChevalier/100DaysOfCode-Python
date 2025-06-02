# analysis.py

import pandas as pd

def missions_per_country(df: pd.DataFrame) -> pd.Series:
    country_counts = df['location'].str.extract(r',\s*([^,]+)$')[0].value_counts()
    return country_counts

def success_rate_by_organisation(df: pd.DataFrame) -> pd.DataFrame:
    df_copy = df.copy()
    df_copy['success'] = df_copy['mission_status'].str.lower().str.contains('success')
    return df_copy.groupby('organisation')['success'].mean().sort_values(ascending=False)

def average_price_by_organisation(df: pd.DataFrame) -> pd.Series:
    return df.groupby('organisation')['price'].mean().sort_values(ascending=False)

def yearly_success_rate(df: pd.DataFrame) -> pd.DataFrame:
    df_copy = df.copy()
    df_copy['year'] = df_copy['date'].dt.year
    df_copy['success'] = df_copy['mission_status'].str.lower().str.contains('success')
    return df_copy.groupby('year')['success'].mean()
