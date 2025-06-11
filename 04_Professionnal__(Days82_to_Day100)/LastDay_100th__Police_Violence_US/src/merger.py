# merger.py

import pandas as pd

def merge_on_city(base_df, other_df, suffix):
    """
    Effectue une jointure LEFT entre base_df et other_df sur la colonne 'city'.
    Ajoute un suffixe aux colonnes de other_df pour éviter les conflits.
    """
    if 'city' not in other_df.columns:
        raise ValueError(f"Le DataFrame fusionné n’a pas de colonne 'city'.")
    
    # Éviter les colonnes dupliquées
    common_cols = [col for col in other_df.columns if col in base_df.columns and col != 'city']
    other_df = other_df.drop(columns=common_cols)

    return base_df.merge(other_df, how='left', on='city', suffixes=('', f'_{suffix}'))

def merge_all(datasets: dict):
    """
    Fusionne tous les datasets sur 'city' uniquement, en gardant 'deaths' comme base.
    """
    base = datasets['deaths'].copy()

    for name in ['income', 'education', 'poverty', 'race']:
        print(f"🔗 Fusion de '{name}'...")
        base = merge_on_city(base, datasets[name], suffix=name)

    return base
