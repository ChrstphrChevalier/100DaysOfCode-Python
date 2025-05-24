from analysis.trends import count_languages, top_projects, find_recurring_words
import streamlit as st
import streamlit.components.v1 as components
import json

# 1. Charger les données
st.title("📊 GitRadar - Tendances GitHub")
if st.button("Charger les données"):
    with open("data/trending_repos.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # 2. Afficher le top langages
    st.subheader("Langages les plus populaires")
    langs = count_languages(data)
    st.bar_chart(langs)

    # 3. Top projets
    st.subheader("🔥 Top projets GitHub")

    import pandas as pd

    top = top_projects(data)
    df = pd.DataFrame(top)[["name", "description", "language", "stars", "url"]]
    df["description"] = df["description"].apply(lambda x: x[:120] + "..." if x and len(x) > 120 else x)
    df.index = df.index + 1

    # HTML stylisé pour afficher proprement la table
    table_html = """
    <style>
        .github-table {
            width: 100%;
            border-collapse: collapse;
            font-family: 'Segoe UI', sans-serif;
            font-size: 14px;
            margin-top: 1em;
        }
        .github-table th {
            background-color: #0e1117;
            color: white;
            padding: 12px 8px;
            text-align: left;
            border-bottom: 1px solid #30363d;
        }
        .github-table td {
            padding: 10px 8px;
            border-bottom: 1px solid #21262d;
            color: #c9d1d9;
        }
        .github-table a {
            color: #58a6ff;
            text-decoration: none;
            font-weight: bold;
        }
        .github-table a:hover {
            text-decoration: underline;
        }
        .github-table tr:hover {
            background-color: #161b22;
        }
    </style>
    <table class="github-table">
        <thead>
            <tr>
                <th>#</th>
                <th>Nom</th>
                <th>Description</th>
                <th>Langage</th>
                <th>⭐</th>
                <th>Lien</th>
            </tr>
        </thead>
        <tbody>
    """

    for i, row in df.iterrows():
        table_html += f"""
        <tr>
            <td>{i}</td>
            <td>{row['name']}</td>
            <td>{row['description'] or ''}</td>
            <td>{row['language'] or '-'}</td>
            <td>{row['stars']}</td>
            <td><a href="{row['url']}" target="_blank">Voir le repo</a></td>
        </tr>
        """

    table_html += "</tbody></table>"

    # Affiche la table stylisée
    components.html(table_html, height=600, scrolling=True)


    # 4. Mots-clés fréquents
    st.subheader("Mots-clés fréquents")
    words = find_recurring_words(data)
    st.bar_chart(words)
