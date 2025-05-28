# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> README Analyzer - Évalue la qualité des README GitHub </p>

### <p align="center"> #Day96 </p>

### Aperçu

**README Analyzer** est une application web développée en **Python** avec le micro-framework **Flask**, qui permet d’analyser automatiquement le fichier `README.md` d’un dépôt GitHub. Elle évalue des éléments clés pour déterminer la **qualité** du README : **nombre de mots**, **présence de sections importantes**, et **présence de badges**. L'outil donne un **score global** sur 5 pour aider à améliorer la présentation d’un projet open source.

- Lancement : `python3 app.py`
- URL analysée : `https://github.com/owner/repo`
- Technologies : `Flask`, `Requests`, `BeautifulSoup`, `Regex`

### Compétences Utilisées

- **Développement web avec Flask** : Création d’un serveur web léger avec routes dynamiques.
- **Manipulation de texte avec Regex** : Extraction du contenu, découpage en sections, comptage de mots.
- **Scraping HTML avec BeautifulSoup** : Analyse des éléments visuels comme les badges (images).
- **Requête HTTP avec Requests** : Récupération du fichier README brut depuis GitHub.
- **Rendu HTML avec Jinja2** : Affichage dynamique des résultats dans une interface simple et claire.
- **Détection de contenu Markdown** : Analyse de sections typiques d’un README bien structuré.

### Mise en œuvre

- **app.py** :
  - Lance un serveur Flask.
  - Récupère et analyse le contenu du `README.md` d’un dépôt GitHub.
  - Calcule un **score de qualité** basé sur :
    - Nombre de mots,
    - Présence de sections clés (installation, usage, contribution, licence),
    - Présence de badges.
  - Retourne les résultats à une page HTML via Jinja2.

- **index.html** :
  - Interface utilisateur propre avec **Bootstrap**.
  - Formulaire d’entrée pour l’URL GitHub (`owner/repo`).
  - Affichage des résultats : score, nombre de mots, feedback.

### Pourquoi ce projet est pertinent

Ce projet montre comment construire une **application web utile** avec un **backend Python léger**. Il est idéal pour apprendre :

- À interagir avec des API tierces (GitHub),
- À analyser et structurer des fichiers Markdown,
- À créer une interface utilisateur propre et responsive,
- À proposer une **analyse automatique de contenu open source**.

Ce projet peut être intégré dans un pipeline d’automatisation ou servir d'outil pour les développeurs cherchant à **améliorer la lisibilité de leur documentation**.

##