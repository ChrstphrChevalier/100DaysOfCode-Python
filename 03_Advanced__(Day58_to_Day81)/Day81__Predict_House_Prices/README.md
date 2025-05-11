# <p align="center"> ![image](https://github.com/user-attachments/assets/9d1cc291-e667-4ba6-976a-6b88f5a24776) </p>

## <p align="center"> Predict House Prices - Modèle de prédiction des prix immobiliers </p>
### <p align="center"> #Day81 </p>

### Aperçu
**Predict House Prices** est un projet d'analyse de données et de machine learning en Python qui utilise le jeu de données Boston Housing pour prédire les prix des maisons en fonction de leurs caractéristiques (nombre de pièces, distance aux centres d'emploi, niveau de pollution, etc.). Ce projet met en œuvre une **régression linéaire multivariable**, l'**exploration de données**, la **transformation des données**, et l'**évaluation des performances du modèle**.

### Compétences acquises
- **Manipulation de données** : Utilisation de pandas pour explorer, nettoyer et préparer les données.
- **Visualisation** : Création de graphiques avec seaborn, matplotlib et plotly pour analyser les relations entre variables.
- **Machine Learning** : Entraînement et évaluation d'un modèle de régression linéaire avec scikit-learn.
- **Transformation des données** : Application d'une transformation logarithmique pour améliorer les performances du modèle.
- **Évaluation statistique** : Calcul du coefficient de détermination (R²) pour évaluer la précision du modèle.
- **Prédiction** : Utilisation des coefficients de régression pour estimer les prix des propriétés.

### Partie obligatoire
- **Exploration des données** : Analyse de la structure du jeu de données (506 lignes, 14 colonnes), vérification des valeurs manquantes (aucune) et des doublons.
- **Préparation des données** : Séparation des données en ensembles d'entraînement et de test, transformation logarithmique de la variable cible (PRICE).
- **Modélisation** : Entraînement de deux modèles de régression linéaire (original et avec transformation logarithmique).
- **Évaluation** : Comparaison des performances via le R² (0.67 pour le modèle original, 0.74 pour le modèle logarithmique sur les données de test).
- **Prédiction** : Estimation du prix d'une maison moyenne (~20 703 $) et d'une maison spécifique avec des caractéristiques définies (~25 792 $).
- **Conclusion** : Le modèle logarithmique est plus performant, expliquant mieux la variance des prix.

### Pourquoi ce projet est pertinent
**Predict House Prices** est un projet clé pour comprendre les bases du machine learning appliqué à la régression. Il illustre l'importance de la transformation des données pour améliorer les modèles et montre comment interpréter les résultats pour des applications concrètes, comme l'estimation immobilière. Ce projet combine analyse statistique, visualisation et modélisation, offrant une expérience pratique précieuse pour tout data scientist en herbe.
