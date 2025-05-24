from scraper.github_scraper import ftech_trending_repos, save_to_csv, save_to_json
from analysis.trends import count_languages, top_projects, find_recurring_words
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    data = ftech_trending_repos()
    save_to_csv(data, os.path.join(BASE_DIR, "data/trending_repos.csv"))
    save_to_json(data, os.path.join(BASE_DIR, "data/trending_repos.json"))

    # print("Langages populaires :", count_languages(data))
    # print('\n')
    # print("Top projets :", top_projects(data))
    # print('\n')
    # print("Mots fréquents :", find_recurring_words(data))

if __name__ == "__main__":
    main()
