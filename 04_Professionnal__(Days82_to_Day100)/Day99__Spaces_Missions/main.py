# main.py

import os
from src.data_cleaning import load_and_clean_data
from src.analysis import (
    missions_per_country,
    success_rate_by_organisation,
    average_price_by_organisation,
    yearly_success_rate
)
from src.visualizations import (
    plot_missions_over_time,
    plot_top_organisations,
    plot_mission_status_distribution
)


def main():
    # 🔹 Charger et nettoyer les données
    base_path = os.getcwd()
    file_path = os.path.join(base_path, "data", "spaces_missions.csv")
    df = load_and_clean_data(file_path)

    # 🔹 Affichage console des analyses simples
    print("Top pays par nombre de missions :")
    print(missions_per_country(df).head(10), end="\n\n")

    print("Taux de succès par organisation :")
    print(success_rate_by_organisation(df).head(10), end="\n\n")

    print("Prix moyen par organisation :")
    print(average_price_by_organisation(df).head(10), end="\n\n")

    print("Taux de succès par année :")
    print(yearly_success_rate(df).tail(10), end="\n\n")

    # 🔹 Visualisations
    plot_missions_over_time(df)
    plot_top_organisations(df)
    plot_mission_status_distribution(df)


if __name__ == "__main__":
    main()
