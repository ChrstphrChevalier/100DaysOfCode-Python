# <p align="center"> ![image](https://github.com/user-attachments/assets/a615bca9-bd69-4679-b79d-a0d9eaa996db) </p>

## <p align="center"> API Request - Suivi de Cyclisme avec Pixela </p>
### <p align="center"> #Day37 </p>

#### Aperçu
**API Request** est un projet en Python qui utilise l'API de Pixela pour suivre les kilomètres parcourus à vélo chaque jour. Il permet de créer un graphique de suivi, d'ajouter des pixels représentant des données quotidiennes, ainsi que de mettre à jour ou supprimer ces données via des requêtes HTTP. Ce projet met en pratique l'utilisation des **requêtes HTTP** avec la bibliothèque `requests` et l'interaction avec des **API RESTful**.

#### Compétences acquises
- **Requêtes HTTP** : Utilisation de `requests` pour envoyer des requêtes GET, POST, PUT, DELETE.
- **Gestion des API** : Interaction avec l'API Pixela pour créer un utilisateur, un graphique, et ajouter des données.
- **Manipulation de la date** : Utilisation de `datetime` pour gérer les dates et les formater selon les besoins de l'API.
- **Entrées utilisateur** : Récupération des informations via `input()` pour suivre les distances parcourues.
- **Gestion des erreurs API** : Affichage des réponses API pour déboguer les requêtes.

#### Partie obligatoire
- **Création de l'utilisateur** : Envoi de données à l'API Pixela pour créer un utilisateur avec un token et un nom d'utilisateur.
- **Création d'un graphique** : Création d'un graphique de suivi avec un ID, un nom, une unité de mesure, et une couleur.
- **Ajout de pixels** : Ajout d'un pixel représentant la distance parcourue à vélo chaque jour.
- **Mise à jour de pixels** : Modification des données existantes (ex : mise à jour du nombre de kilomètres).
- **Suppression de pixels** : Suppression des pixels si nécessaire.
  
#### Pourquoi ce projet est pertinent
Ce projet est un excellent moyen de se familiariser avec les interactions API en Python et de comprendre comment gérer les données utilisateurs à travers des requêtes HTTP. De plus, il offre une approche concrète pour interagir avec des services web, ce qui est une compétence clé pour tout développeur backend ou full-stack. Ce type de projet peut être étendu pour suivre diverses autres activités, comme la course, l'alimentation, ou même la productivité.
