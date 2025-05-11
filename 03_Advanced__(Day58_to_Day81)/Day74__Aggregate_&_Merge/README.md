# <p align="center"> ![image](https://github.com/user-attachments/assets/9d1cc291-e667-4ba6-976a-6b88f5a24776) </p>

## <p align="center"> LEGO Analysis - Analyse des ensembles LEGO </p>
### <p align="center"> #Day74 </p>

### Aperçu
**LEGO Analysis** est un projet en Python qui explore un ensemble de données sur les pièces et ensembles LEGO provenant de [Rebrickable](https://rebrickable.com/downloads/). Ce projet utilise **Pandas** pour manipuler les données et **Matplotlib** pour visualiser les tendances. Il répond à des questions sur l’histoire de LEGO, comme la popularité des thèmes, la taille des ensembles, et l’évolution de l’offre produit.

### Compétences acquises
- **Manipulation de données** : Utilisation de Pandas pour lire, explorer et agréger des fichiers CSV.
- **Exploration de données** : Analyse des dimensions, unicité des valeurs (`.nunique()`), et regroupement avec `.groupby()`.
- **Calculs statistiques** : Comptage des couleurs transparentes et opaques, analyse des tendances par année et thème.
- **Visualisation** : Création de graphiques avec Matplotlib pour illustrer l’évolution des ensembles.
- **Fusion de données** : Compréhension des bases pour agréger et fusionner des datasets (préliminaire).

### Partie obligatoire
- **Importation des données** : Lecture du fichier `colors.csv` pour analyser les couleurs LEGO.
- **Exploration** : Calcul du nombre total de couleurs uniques (135) avec `.nunique()`.
- **Analyse** : Décompte des couleurs transparentes (28) et opaques (107) via `.groupby()` et `.count()`.
- **Robustesse** : Gestion correcte des formats de données et vérification des résultats.

### Pourquoi ce projet est pertinent
**LEGO Analysis** est un excellent moyen de pratiquer l’analyse de données avec Python, en explorant un dataset réel et riche. Il permet de développer des compétences en manipulation de DataFrames, en agrégation, et en visualisation, tout en offrant des insights sur l’évolution d’une marque emblématique comme LEGO. Ce projet pose les bases pour des analyses plus complexes impliquant la fusion de datasets.
