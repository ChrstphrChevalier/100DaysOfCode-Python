import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set(style="whitegrid")

def plot_missions_over_time(df: pd.DataFrame):
    df_year = df.copy()
    df_year['year'] = df_year['date'].dt.year
    missions_per_year = df_year.groupby('year').size()

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=missions_per_year)
    plt.title('Nombre de missions spatiales par année')
    plt.xlabel('Année')
    plt.ylabel('Nombre de missions')
    plt.tight_layout()
    plt.show()

def plot_top_organisations(df: pd.DataFrame, top_n=10):
    top_orgs = df['organisation'].value_counts().head(top_n)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_orgs.values, y=top_orgs.index, palette="rocket")
    plt.title(f'Top {top_n} organisations par nombre de missions')
    plt.xlabel('Nombre de missions')
    plt.ylabel('Organisation')
    plt.tight_layout()
    plt.show()

def plot_mission_status_distribution(df: pd.DataFrame):
    status_counts = df['mission_status'].value_counts()

    plt.figure(figsize=(8, 6))
    sns.barplot(x=status_counts.index, y=status_counts.values, palette="coolwarm")
    plt.title('Répartition des statuts de mission')
    plt.xlabel('Statut')
    plt.ylabel('Nombre de missions')
    plt.tight_layout()
    plt.show()
