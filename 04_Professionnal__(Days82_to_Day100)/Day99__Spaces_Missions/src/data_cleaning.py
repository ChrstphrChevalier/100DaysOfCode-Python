# data_cleaning.py

import pandas as pd

def load_and_clean_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)

    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    df = df.loc[:, ~df.columns.str.startswith('unnamed')]

    df = df.dropna(how='all')
    df = df.dropna(axis=1, how='all')

    if 'price' in df.columns:
        df['price'] = pd.to_numeric(df['price'], errors='coerce')

    df = df.fillna({
        'organisation': 'Unknown',
        'location': 'Unknown',
        'date': 'Unknown',
        'detail': 'Unknown',
        'rocket_status': 'Unknown',
        'price': 0,
        'mission_status': 'Unknown'
    })

    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    if 'organisation' in df.columns:
        df['organisation'] = df['organisation'].str.strip().str.lower()

    return df