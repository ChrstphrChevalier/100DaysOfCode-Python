# <p align="center"> ![image](https://github.com/user-attachments/assets/9d1cc291-e667-4ba6-976a-6b88f5a24776) </p>

## <p align="center"> The Tragic Discovery - Analyse des données de Semmelweis sur le lavage des mains </p>
### <p align="center"> #Day80 </p>

### Aperçu
**The Tragic Discovery** est un projet d'analyse de données en Python qui retrace la découverte historique du Dr Ignaz Semmelweis sur l'importance du lavage des mains pour réduire les décès par fièvre puerpérale dans les maternités. Ce projet utilise des données réelles collectées entre 1841 et 1849 à l'Hôpital Général de Vienne pour analyser les taux de mortalité avant et après l'introduction du lavage des mains. Il met en pratique des techniques de **manipulation de données**, de **visualisation**, et de **tests statistiques**.

### Compétences acquises
- **Manipulation de données** : Utilisation de pandas pour charger, explorer et transformer des DataFrames.
- **Visualisation** : Création de graphiques interactifs avec plotly et matplotlib pour illustrer les tendances des taux de mortalité.
- **Statistiques** : Application d'un test t (ttest_ind de scipy.stats) pour évaluer la significativité statistique des différences dans les taux de mortalité.
- **Analyse temporelle** : Gestion des données temporelles avec conversion des dates et agrégation annuelle/mensuelle.
- **Interprétation des résultats** : Traduction des résultats statistiques en conclusions pratiques.

### Partie obligatoire
- **Exploration des données** : Analyse des DataFrames `df_yearly` et `df_monthly` pour comprendre leur structure, vérifier l'absence de valeurs manquantes et calculer des moyennes.
- **Calculs** : Calcul des taux de mortalité (pourcentage de décès par rapport aux naissances) avant et après l'introduction du lavage des mains.
- **Test statistique** : Utilisation du test t pour comparer les taux de mortalité, avec un seuil de significativité de 99% (p-valeur < 0.01).
- **Visualisation** : Génération de graphiques montrant l'évolution des décès et l'impact du lavage des mains.
- **Conclusion** : Confirmation que le lavage des mains a significativement réduit les taux de mortalité, avec une p-valeur de 0.0000002985.

### Pourquoi ce projet est pertinent
**The Tragic Discovery** est un projet captivant qui combine l'analyse de données avec une histoire médicale réelle ayant sauvé des milliers de vies. Il illustre comment les données et les statistiques peuvent révéler des vérités cruciales et influencer des pratiques concrètes. Ce projet renforce les compétences en analyse de données, visualisation, et pensée critique, tout en offrant une perspective historique sur l'importance de l'hygiène en médecine.
