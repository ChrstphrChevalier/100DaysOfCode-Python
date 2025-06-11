# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center">Police_Violence_US – Analyse croisée entre Recensement Américain et Décès causés par la Police</p>

### <p align="center">#Day100</p>

### Aperçu

**Police_Violence_US** est un projet complet en **Python** mêlant **analyse exploratoire** et **visualisation de données sensibles**, centré sur les décès imputables à la police aux États-Unis depuis 2015.  
Les données proviennent de la base du *Washington Post* ainsi que du recensement américain (*US Census*) incluant :  
- le **revenu médian**,  
- le **taux de pauvreté**,  
- le **niveau d’éducation**,  
- la **démographie raciale** par ville.

L’objectif est d’identifier et de comprendre les corrélations sociales et géographiques autour de l’usage de la force létale.

* 📁 Chargement et nettoyage via `main.py`  
* 📊 Visualisation interactive dans `exploration.ipynb`  
* Technologies : `Python`, `Pandas`, `Seaborn`, `Matplotlib`, `Plotly`  

### Compétences Utilisées

* 🧼 **Nettoyage de données** : standardisation des noms de colonnes (`snake_case`), harmonisation des champs (`city`, `state`), suppression des lignes incomplètes.
* 🔗 **Fusion intelligente** : jointure des datasets via la clé commune `city`, sans perte de données critiques.
* 📊 **Exploration visuelle** : bar plots, heatmaps de corrélation, histogrammes interactifs.
* 📈 **Analyse socio-économique** : impact du niveau d’éducation, des revenus et de la race sur la fréquence des décès.
* 🛠️ **Architecture modulaire** : découpage du projet en modules (`loader`, `cleaner`, `merger`, `analysis`, `main`, `exploration.ipynb`) pour un code clair, maintenable et testable.
* 📂 **Pratiques de projet pro** : arborescence propre, usage de `requirements.txt`, séparation données brutes / transformées.

### Mise en œuvre

* **loader.py** :  
  * `load_csv()` : chargement intelligent avec fallback d'encodage.  
  * `dict_dataframe()` : charge automatiquement les 5 fichiers CSV d'entrée.

* **cleaner.py** :  
  * Nettoyage global (colonnes, noms, typages, valeurs manquantes).  
  * `clean_dataframe()` appliqué à tous les fichiers en dictionnaire.

* **merger.py** :  
  * Fusionne les 5 DataFrames en un seul sur la colonne `city`, en préservant toutes les informations sociales.

* **analysis.py** :  
  * Fonctions analytiques : top villes, répartition raciale, corrélations entre décès et pauvreté/éducation/revenus.

* **main.py** :  
  * Exécute l’ensemble du pipeline, et exporte le DataFrame fusionné (`merged_dataset.csv`).  
  * Affiche aussi un résumé analytique en terminal.

* **exploration.ipynb** :  
  * Visualisation et analyse interactive des données finales, avec `Seaborn`, `Matplotlib` et `Plotly`.

### Pourquoi ce projet est pertinent

Ce projet incarne une **application sérieuse et citoyenne** de la Data Science, en lien avec des enjeux de société cruciaux :

* 🧠 Application rigoureuse des **fondamentaux de la Data Analyse** : nettoyage, fusion, EDA, visualisation.
* 📊 Données réelles, sensibles et politiquement importantes, issues de sources fiables.
* 🧩 Mise en œuvre d’un **pipeline modulaire Python** clair et réutilisable.
* 📍 Contexte réel d’analyse sociale et territoriale.
* 💼 Excellent projet de portfolio pour des rôles en **Data Science**, **Analyse Sociale Quantitative**, ou **Python appliqué**.

##