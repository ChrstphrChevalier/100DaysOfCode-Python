# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## 📝 Ma Todo List – Gérez Vos Tâches Simplement

### #Day89

### 🚀 Aperçu

**Ma Todo List** est une application web développée avec **Flask** pour permettre aux utilisateurs de gérer leurs tâches de manière simple et intuitive.
Construite avec **Python**, **Flask**, **SQLite** et du **CSS personnalisé**, cette application permet d’**ajouter**, **marquer comme terminées**, et **supprimer** des tâches.
L’interface épurée, stylisée avec un design responsive et une esthétique minimaliste, offre une expérience utilisateur fluide pour organiser ses activités quotidiennes.

### 🧠 Compétences utilisées

* 🔹 **Développement web avec Flask** : gestion des routes, des formulaires et des interactions avec la base de données.
* 🔹 **Gestion de base de données avec SQLite** : création et manipulation d’une base légère pour stocker les tâches.
* 🔹 **Conception d’interface avec Jinja2** : rendu dynamique des templates HTML pour afficher les tâches.
* 🔹 **Stylisation CSS personnalisée** : design moderne, mise en page centrée, bordures colorées, effets visuels sur les tâches terminées.
* 🔹 **Gestion des formulaires** : traitement sécurisé des entrées via des requêtes `POST`.
* 🔹 **Structure modulaire** : séparation du code (Python, HTML, CSS) pour une meilleure maintenabilité.
* 🔹 **Programmation Python** : logique backend complète avec opérations CRUD.

### ⚙️ Mise en œuvre

#### 🧑‍💻 Interface utilisateur

* 🏠 **Page d'accueil (`index.html`)** :
  Affiche la liste des tâches, leur contenu, leur statut (terminée ou non), avec des boutons emoji : ✅ (terminer) et ❌ (supprimer).

* ➕ **Formulaire d’ajout** :
  Champ texte et bouton pour ajouter une tâche.

* 📱 **Design responsive** :
  Mise en page fluide, largeur maximale de 600px, adaptée aux écrans mobiles et desktop.


#### 🔧 Logique backend

* 🔁 **Routes Flask** :

  * `GET /` : afficher les tâches
  * `POST /add` : ajouter une tâche
  * `GET /done/<task_id>` : marquer une tâche comme terminée
  * `GET /delete/<task_id>` : supprimer une tâche

* 🗃️ **Base de données SQLite** :
  Table `tasks` avec les champs `id`, `content`, `done`.

* ⚙️ **Opérations CRUD** :
  Création, lecture, mise à jour et suppression des tâches.

* 📥 **Initialisation automatique** :
  Création de la base SQLite si elle n’existe pas, avec un schéma simple.

#### 🎨 Design

* ✨ **Esthétique visuelle** :
  Fond gris clair, tâches affichées dans des boîtes blanches avec une bordure latérale colorée :

  * noire pour les tâches en cours
  * verte pour les tâches terminées

* 🎭 **Éléments interactifs** :
  Texte barré + opacité réduite pour les tâches terminées.

* 🧭 **Expérience utilisateur** :
  Interface intuitive, formulaire simple, emojis pour des actions rapides.

### 💡 Pourquoi ce projet est pertinent

**Ma Todo List** est un projet idéal pour démontrer des compétences en **développement web full-stack avec Python**.
Il illustre la maîtrise du **backend** (Flask, SQLite), du **frontend** (HTML, CSS, Jinja2) et de la **gestion de base de données**.
L’application répond à un besoin universel : organiser ses tâches efficacement.
Sa structure claire et son design responsive en font une base solide pour des évolutions futures : catégories, échéances, authentification, etc.

##