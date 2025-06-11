# loader.py

import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    try:
        return pd.read_csv(path)  # essaie UTF-8 par défaut
    except UnicodeDecodeError:
        print(f"⚠️ UnicodeDecodeError avec UTF-8 pour {filename}, tentative avec windows-1252...")
        try:
            return pd.read_csv(path, encoding='windows-1252')
        except Exception as e:
            print(f"❌ Erreur lors de la lecture de {filename} avec windows-1252 : {e}")
            return None
    except FileNotFoundError:
        print(f"❌ FileNotFound : {filename}")
        return None
    
def dict_dataframe():
    return {
        "deaths": load_csv("Deaths_by_Police_US.csv"),
        "income": load_csv("Median_Household_Income_2015.csv"),
        "education": load_csv("Pct_Over_25_Completed_High_School.csv"),
        "poverty": load_csv("Pct_People_Below_Poverty_Level.csv"),
        "race": load_csv("Share_of_Race_By_City.csv"),
    }
