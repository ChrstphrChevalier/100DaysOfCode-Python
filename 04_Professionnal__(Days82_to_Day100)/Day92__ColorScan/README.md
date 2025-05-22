# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> ColorScan - Dominant Color Extraction Web App </p>

### <p align="center"> #Day92 </p>

### Aperçu

**ColorScan** est une application web développée avec **Flask**, **Pillow**, **NumPy**, et **scikit-learn**, permettant aux utilisateurs de **télécharger une image** et d’**extraire automatiquement une palette des couleurs dominantes**. L’utilisateur peut spécifier le **nombre de couleurs** à extraire (de 1 à 20), visualiser l’image uploadée, et obtenir une **palette de couleurs** avec leurs codes **HEX** et **RGB**. L’application est hébergée sur **Render** et inclut un système de **nettoyage automatique** des fichiers uploadés pour optimiser l’espace serveur.

### Compétences Utilisées

- **Développement web avec Flask** : Création d’une application web légère avec gestion des routes, formulaires, et rendu de templates dynamiques.
- **Manipulation d’images avec Pillow** : Chargement, redimensionnement, et conversion des images en format **RGB** pour l’extraction des couleurs.
- **Analyse de données avec scikit-learn** : Utilisation de l’algorithme **KMeans** pour identifier les couleurs dominantes via le clustering des pixels.
- **Calcul numérique avec NumPy** : Manipulation efficace des tableaux de pixels pour préparer les données à l’analyse.
- **Gestion des fichiers et nettoyage automatisé** : Mise en place d’un script **cron** pour supprimer automatiquement les images uploadées après 24 heures.
- **Design d’interface utilisateur** : Création d’une interface **HTML/CSS** moderne avec **Tailwind**-inspired styling, utilisant des polices Google Fonts (**Inter**, **Playfair Display**) pour une expérience utilisateur fluide.
- **Déploiement sur Render** : Configuration d’un environnement **Python** avec **gunicorn** pour le serveur web et un job **cron** pour la maintenance.

### Mise en Œuvre

- **Interface utilisateur** :
  - Formulaire pour **uploader une image** (formats acceptés : tous les formats d’image standard).
  - Champ numérique pour définir le **nombre de couleurs** à extraire (par défaut : 5, max : 20).
  - Bouton **"Analyser"** pour lancer l’extraction des couleurs.
  - Affichage de l’**image uploadée** et de la **palette de couleurs** extraite avec leurs codes **HEX** et **RGB** dans une grille responsive.

- **Logique de traitement** :
  - Redimensionnement automatique des images pour limiter la taille maximale à **500 pixels** (optimisation des performances).
  - Conversion des images en **RGB** et transformation des pixels en un tableau **NumPy** pour l’analyse.
  - Application de l’algorithme **KMeans** pour regrouper les pixels en clusters et extraire les couleurs dominantes.
  - Conversion des centres des clusters en codes **HEX** et **RGB** pour un affichage clair.

- **Gestion des fichiers** :
  - Les images uploadées sont stockées dans un dossier **static/Uploads**.
  - Un script **cleaner.py** s’exécute quotidiennement via un job **cron** sur Render pour supprimer les fichiers datant de plus de 24 heures.

- **Personnalisation** :
  - Choix flexible du **nombre de couleurs** à extraire (1 à 20).
  - Affichage visuel des couleurs dans des blocs carrés avec une présentation claire des codes **HEX** et **RGB**.
  - Interface responsive adaptée à tous les écrans (mobile, tablette, desktop).

### Pourquoi ce projet est pertinent

**ColorScan** démontre des compétences avancées en **développement web full-stack**, combinant un **backend Flask** robuste avec un **frontend HTML/CSS** moderne. Il illustre l’utilisation de **machine learning** (KMeans) pour l’analyse d’images, la manipulation efficace de données avec **NumPy**, et la gestion d’images avec **Pillow**. Le projet met également en avant des bonnes pratiques en **déploiement cloud** (Render, gunicorn, cron) et en **optimisation des ressources** (nettoyage automatisé).

Ce projet est idéal pour des cas d’usage réels comme la **création de palettes de couleurs** pour le design graphique, l’UX/UI, ou le branding. Il peut évoluer avec des fonctionnalités comme l’**exportation de la palette en PNG/SVG**, l’intégration d’un **aperçu en temps réel**, ou l’ajout de **filtres de couleur** pour affiner les résultats.


## <p align="center"> ColorScan - Dominant Color Extraction Web App </p>

### <p align="center"> #Day92 </p>

### Aperçu

**ColorScan** est une application web développée avec **Flask**, **Pillow**, **NumPy**, et **scikit-learn**, permettant aux utilisateurs de **télécharger une image** et d’**extraire automatiquement une palette des couleurs dominantes**. L’utilisateur peut spécifier le **nombre de couleurs** à extraire (de 1 à 20), visualiser l’image uploadée, et obtenir une **palette de couleurs** avec leurs codes **HEX** et **RGB**. L’application est hébergée sur **Render** et inclut un système de **nettoyage automatique** des fichiers uploadés pour optimiser l’espace serveur.

### Compétences Utilisées

- **Développement web avec Flask** : Création d’une application web légère avec gestion des routes, formulaires, et rendu de templates dynamiques.
- **Manipulation d’images avec Pillow** : Chargement, redimensionnement, et conversion des images en format **RGB** pour l’extraction des couleurs.
- **Analyse de données avec scikit-learn** : Utilisation de l’algorithme **KMeans** pour identifier les couleurs dominantes via le clustering des pixels.
- **Calcul numérique avec NumPy** : Manipulation efficace des tableaux de pixels pour préparer les données à l’analyse.
- **Gestion des fichiers et nettoyage automatisé** : Mise en place d’un script **cron** pour supprimer automatiquement les images uploadées après 24 heures.
- **Design d’interface utilisateur** : Création d’une interface **HTML/CSS** moderne avec **Tailwind**-inspired styling, utilisant des polices Google Fonts (**Inter**, **Playfair Display**) pour une expérience utilisateur fluide.
- **Déploiement sur Render** : Configuration d’un environnement **Python** avec **gunicorn** pour le serveur web et un job **cron** pour la maintenance.

### Mise en Œuvre

- **Interface utilisateur** :
  - Formulaire pour **uploader une image** (formats acceptés : tous les formats d’image standard).
  - Champ numérique pour définir le **nombre de couleurs** à extraire (par défaut : 5, max : 20).
  - Bouton **"Analyser"** pour lancer l’extraction des couleurs.
  - Affichage de l’**image uploadée** et de la **palette de couleurs** extraite avec leurs codes **HEX** et **RGB** dans une grille responsive.

- **Logique de traitement** :
  - Redimensionnement automatique des images pour limiter la taille maximale à **500 pixels** (optimisation des performances).
  - Conversion des images en **RGB** et transformation des pixels en un tableau **NumPy** pour l’analyse.
  - Application de l’algorithme **KMeans** pour regrouper les pixels en clusters et extraire les couleurs dominantes.
  - Conversion des centres des clusters en codes **HEX** et **RGB** pour un affichage clair.

- **Gestion des fichiers** :
  - Les images uploadées sont stockées dans un dossier **static/Uploads**.
  - Un script **cleaner.py** s’exécute quotidiennement via un job **cron** sur Render pour supprimer les fichiers datant de plus de 24 heures.

- **Personnalisation** :
  - Choix flexible du **nombre de couleurs** à extraire (1 à 20).
  - Affichage visuel des couleurs dans des blocs carrés avec une présentation claire des codes **HEX** et **RGB**.
  - Interface responsive adaptée à tous les écrans (mobile, tablette, desktop).

### Pourquoi ce projet est pertinent

**ColorScan** démontre des compétences avancées en **développement web full-stack**, combinant un **backend Flask** robuste avec un **frontend HTML/CSS** moderne. Il illustre l’utilisation de **machine learning** (KMeans) pour l’analyse d’images, la manipulation efficace de données avec **NumPy**, et la gestion d’images avec **Pillow**. Le projet met également en avant des bonnes pratiques en **déploiement cloud** (Render, gunicorn, cron) et en **optimisation des ressources** (nettoyage automatisé).

Ce projet est idéal pour des cas d’usage réels comme la **création de palettes de couleurs** pour le design graphique, l’UX/UI, ou le branding. Il peut évoluer avec des fonctionnalités comme l’**exportation de la palette en PNG/SVG**, l’intégration d’un **aperçu en temps réel**, ou l’ajout de **filtres de couleur** pour affiner les résultats.

##