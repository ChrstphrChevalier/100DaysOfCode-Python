# analysis.py

import pandas as pd

def basic_overview(df):
    """
    Affiche un résumé global du DataFrame : tailles, colonnes nulles, etc.
    """
    print("🧠 Aperçu général :")
    print(df.shape)
    print("\nColonnes avec valeurs manquantes :")
    print(df.isnull().sum()[df.isnull().sum() > 0])

def count_killings_by_city(df, top_n=10):
    """
    Retourne les villes avec le plus de décès recensés.
    """
    return df['city'].value_counts().head(top_n)

def groupby_race(df):
    """
    Compte les décès par race (si dispo).
    """
    if 'race' in df.columns:
        return df['race'].value_counts(dropna=False)
    else:
        print("❌ Colonne 'race' introuvable.")
        return None

def correlation_with_deaths(df):
    """
    Calcule les corrélations entre le nombre de décès par ville
    et les variables socio-éco (si disponibles).
    """
    df_count = df.groupby("city").size().reset_index(name="killings")

    cols_to_merge = [col for col in df.columns if col not in ['state', 'race']]
    df_meta = df[cols_to_merge].drop_duplicates(subset="city")

    merged = pd.merge(df_count, df_meta, on="city", how="left")
    num_cols = merged.select_dtypes(include='number').columns

    print("📊 Corrélations avec 'killings' :")
    return merged[num_cols].corr()['killings'].sort_values(ascending=False)

def killings_by_state(df, top_n=10):
    """
    Retourne les états avec le plus de décès.
    """
    if 'state' in df.columns:
        return df['state'].value_counts().head(top_n)
    else:
        print("❌ Colonne 'state' introuvable.")
        return None
