# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> DinoBot - Bot IA pour le jeu Chrome Dino </p>

### <p align="center"> #Day94 </p>

### Aperçu

**DinoBot** est un **bot d’automatisation intelligent** capable de jouer au célèbre jeu **Chrome Dino** en détectant les obstacles à l’écran et en réagissant en temps réel. Il repose sur une **capture dynamique de l’écran**, un **modèle de Machine Learning entraîné** pour reconnaître les situations de saut, et un **contrôle du clavier automatisé**. Il peut collecter des données, entraîner son propre modèle et jouer de façon autonome.

- Lancement : `python3 main.py collect` ou `python3 main.py train`
- Exécution du bot : `python3 main_bot.py`
- Données : `data/obstacle_*.png`, `data/no_obstacle_*.png`
- Modèle : `model/dino_model.joblib`

### Compétences Utilisées

- **Vision par ordinateur (OpenCV)** : Découpe d’une **région d’intérêt (ROI)** sur l’écran, conversion en niveaux de gris, redimensionnement et normalisation des données d’image.
- **Contrôle du clavier (pynput)** : Interaction automatisée avec le jeu via la détection de touches et les actions comme le saut (`pyautogui.press("space")`).
- **Screenshot dynamique (pyautogui)** : Capture rapide de l’environnement de jeu pour traitement.
- **Machine Learning supervisé (scikit-learn)** : Entraînement d’un modèle avec les images labellisées pour prédire la présence ou non d’un obstacle.
- **Prétraitement d’images** : Resize, flatten, grayscale... pour convertir chaque image en vecteur utilisable par un modèle ML.
- **Structure modulaire** : Répartition claire en fichiers `capture.py`, `preprocess.py`, `trainer.py`, `main_bot.py`...

### Mise en Œuvre

- **Collecte de données (`bot/capture.py`)** :
  - Capture la zone de jeu sur pression des touches `o` (obstacle) ou `n` (no_obstacle).
  - Sauvegarde automatique dans le dossier `data/` avec nommage structuré.

- **Prétraitement (`bot/preprocess.py`)** :
  - Charge et transforme les images en vecteurs normalisés (flatten grayscale resized).
  - Crée `X` et `y` pour l'entraînement.

- **Entraînement du modèle (`bot/trainer.py`)** :
  - Utilise un `SGDClassifier` ou autre algo sklearn sur les images labellisées.
  - Sauvegarde le modèle en `.joblib` dans `model/`.

- **Lancement du bot (`main_bot.py`)** :
  - Chargement du modèle.
  - Boucle de capture + prédiction.
  - Appui automatique sur `space` en cas d’obstacle détecté.
  - Quitte si touche `q` pressée.

### Pourquoi ce projet est pertinent

**DinoBot** combine **IA pratique**, **automatisation**, et **contrôle en temps réel** sur une base ludique. C’est un excellent exemple de **projet machine learning appliqué**, avec :
- Collecte personnalisée des données
- Entraînement et déploiement d’un modèle
- Interaction directe avec un environnement graphique

Tu peux l’enrichir avec :
- Une meilleure architecture de modèle (CNN avec TensorFlow ?),
- Une capture vidéo + tracking des performances,
- Une interface Streamlit pour observer les prédictions en live.

Ce projet est idéal pour comprendre le **cycle de vie complet d’un projet ML** : de la data brute à l’action automatisée.

##