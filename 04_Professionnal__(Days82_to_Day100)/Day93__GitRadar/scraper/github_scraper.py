import requests
from bs4 import BeautifulSoup
from datetime import datetime

import csv
import json
import os

def ftech_trending_repos() -> list[dict]:
    url = f"https://github.com/trending"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')

    repos = []
    articles = soup.find_all('article', class_='Box-row')
    for article in articles:
        # 🔹 Nom et lien
        h2_tag = article.find('h2')
        a_tag = h2_tag.find('a') if h2_tag else None
        repo_name = a_tag.text.strip().replace('\n', '').replace(' ', '') if a_tag else None
        repo_url = f"https://github.com{a_tag['href']}" if a_tag and 'href' in a_tag.attrs else None

        # 🔹 Description
        p_tag = article.find('p', class_='col-9 color-fg-muted my-1 pr-4')
        description = p_tag.text.strip() if p_tag else None

        # 🔹 Langage principal
        lang_tag = article.find('span', itemprop='programmingLanguage')
        language = lang_tag.text.strip() if lang_tag else None

        # 🔹 Stars
        star_tag = article.find('a', href=lambda x: x and x.endswith('/stargazers'))
        stars = star_tag.text.strip().replace(',', '') if star_tag else '0'

        # 🔹 Date
        date = datetime.today().isoformat()

         # 🧠 Regroupe tout dans un dict
        repos.append({
            'name': repo_name,
            'description': description,
            'language': language,
            'stars': int(stars.replace('k', '000').replace('.', '')) if 'k' in stars else int(stars),
            'url': repo_url,
            'date': date
        })

    return repos
    
def save_to_csv(data: list[dict], filepath: str) -> None:
    if not data:
        return
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def save_to_json(data: list[dict], filepath: str) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)