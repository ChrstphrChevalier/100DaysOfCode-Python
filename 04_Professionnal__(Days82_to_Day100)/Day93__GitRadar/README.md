# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> GitRadar - Scraper & Dashboard des projets GitHub tendance par stack </p>

### <p align="center"> #Day93 </p>

### Aperçu

**GitRadar** est un outil de veille technologique qui scrute les **projets GitHub les plus tendance** et en extrait les informations clés comme le **langage**, le **nombre de stars**, la **description** et plus encore. Ces données sont ensuite **analysées**, **exportées** (CSV/JSON) et **visualisées via un dashboard interactif** Streamlit. L'objectif est d’identifier les **stacks populaires**, les **technos qui montent**, et les projets à suivre chaque semaine.

- Dashboard local : 👉 `./run_all.sh`
- Données brutes : `data/trending_repos.csv` / `data/trending_repos.json`

### Compétences Utilisées

- **Scraping web avec requests & BeautifulSoup** : Extraction automatique des projets en tendance sur `https://github.com/trending`, avec filtrage par langage.
- **Analyse de données avec Python** : Détection des langages les plus utilisés, des mots-clés récurrents et des projets qui explosent.
- **Export CSV / JSON** : Sauvegarde structurée des données pour exploitation future ou réutilisation.
- **Visualisation avec Streamlit** : Création d’un dashboard interactif pour explorer les tendances par langage, par popularité et par fréquence de mots-clés.
- **Automatisation via script shell** : Lancement d’un script unifié (`run_all.sh`) pour exécuter le scraping, l’analyse et démarrer le dashboard.
- **Structure modulaire** : Organisation claire en modules `scraper/`, `analysis/`, `dashboard/` et `data/`.

### Mise en Œuvre

- **Scraper (`scraper/github_scraper.py`)** :
  - Récupère les projets de `https://github.com/trending`
  - Extrait nom, langage, nombre d’étoiles, description, lien et date.
  - Stocke les données dans des objets Python exploitables.

- **Analyse (`analysis/trends.py`)** :
  - Classement des langages les plus fréquents.
  - Extraction des mots-clés récurrents dans les descriptions.
  - Sélection des projets avec forte progression en stars.

- **Export (`main.py`)** :
  - Exporte les données dans `data/trending_repos.csv` et `.json`
  - Affiche dans la console un résumé rapide des résultats.

- **Dashboard (`dashboard/streamlit_app.py`)** :
  - Chargement dynamique des fichiers de données.
  - Graphiques interactifs : langages dominants, top projets, nuage de mots.
  - Interface fluide et responsive pour explorer les résultats.

- **Automatisation (`run_all.sh`)** :
  - Lancement du scraping, sauvegarde des fichiers, puis ouverture automatique du dashboard Streamlit.

### Pourquoi ce projet est pertinent

**GitRadar** est un projet idéal pour combiner **scraping web**, **analyse de données**, et **visualisation interactive**. Il permet de rester à jour sur les technos en vogue tout en apprenant à structurer une application **modulaire**, **automatisée** et **axée sur la donnée**.

Le dashboard peut être enrichi avec des filtres avancés (par pays, organisation, nombre de contributeurs, etc.), l’historique hebdomadaire, ou une publication automatique des résultats sur LinkedIn ou en newsletter. Il peut aussi évoluer en API ou service SaaS de veille technologique.

##