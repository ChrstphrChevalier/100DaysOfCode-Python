# main.py

from src.loader import dict_dataframe
from src.cleaner import cleaner
from src.merger import merge_all
from src.analysis import (
    basic_overview,
    count_killings_by_city,
    groupby_race,
    correlation_with_deaths,
    killings_by_state
)

import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
OUTPUT_PATH = os.path.join(DATA_DIR, "Merged_Datasets.csv")

def main():
    print("📥 Chargement des données...")
    raw_datasets = dict_dataframe()

    print("🧼 Nettoyage des données...")
    cleaned_datasets = cleaner(raw_datasets)

    print("🔗 Fusion des données...")
    merged_df = merge_all(cleaned_datasets)

    print(f"💾 Export du DataFrame final dans {OUTPUT_PATH}")
    merged_df.to_csv(OUTPUT_PATH, index=False)

    # ===== 🔍 Analyse exploratoire rapide =====
    print("\n📊 ANALYSE RAPIDE :\n")

    basic_overview(merged_df)

    print("\n🏙️ Villes avec le plus de décès recensés :")
    print(count_killings_by_city(merged_df))

    print("\n👥 Répartition des décès par race :")
    print(groupby_race(merged_df))

    print("\n🧩 Corrélations avec le nombre de décès par ville :")
    print(correlation_with_deaths(merged_df))

    print("\n📍 États avec le plus de décès recensés :")
    print(killings_by_state(merged_df))

if __name__ == "__main__":
    main()
