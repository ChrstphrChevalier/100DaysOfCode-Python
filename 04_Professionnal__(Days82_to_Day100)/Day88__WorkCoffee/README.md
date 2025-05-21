# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> WorkCoffee - Trouvez les Meilleurs Cafés pour Travailler </p>

### <p align="center"> #Day88 </p>

### Aperçu

**WorkCoffee** est une **application web** développée avec **Flask** pour aider les **travailleurs à distance**, les **nomades numériques** et les **amateurs de café** à trouver les **cafés** parfaits pour travailler. Construite avec **Python**, **Flask**, **SQLAlchemy** et **Bootstrap**, cette application permet de consulter, ajouter et supprimer des fiches de cafés avec des informations comme la **disponibilité du Wi-Fi**, les **prises électriques** et les **liens de sites web**. L'interface moderne et élégante, stylisée avec du **CSS personnalisé** et des **polices Google**, offre une expérience intuitive pour découvrir des espaces de travail conviviaux.

### Compétences Utilisées

- **Développement web avec Flask** : Gestion des routes, des formulaires et des interactions avec la base de données.
- **Gestion de base de données avec SQLAlchemy** : Utilisation d’un ORM pour interagir avec une base **SQLite** et gérer les données des cafés.
- **Conception d’interface avec Bootstrap** : Interface réactive et moderne grâce à Bootstrap 5.3 pour la mise en page et le style.
- **Stylisation CSS personnalisée** : Boutons en dégradé doré, typographie avec **Playfair Display** et **Cormorant Garamond** pour une esthétique raffinée.
- **Gestion des formulaires et validation** : Traitement sécurisé des entrées utilisateur pour ajouter des cafés avec champs obligatoires et optionnels.
- **Rendu HTML dynamique avec Jinja2** : Templating pour afficher les listes de cafés et les formulaires interactifs.
- **Structure prête pour le déploiement** : Code modulaire avec séparation des modèles, templates et fichiers statiques pour une évolutivité optimale.

### Mise en Œuvre

- **Interface utilisateur** :
  - **Page d'accueil (`index.html`)** : Affiche une liste de cafés avec des détails comme le nom, l’adresse (liée à Google Maps), le Wi-Fi, les prises électriques et le site web. Inclut un bouton pour ajouter de nouveaux cafés et supprimer les existants.
  - **Formulaire d’ajout (`add.html`)** : Formulaire convivial pour soumettre les détails d’un nouveau café, incluant le nom, l’adresse, le site web, la disponibilité du Wi-Fi et des prises électriques.
  - **Design responsive** : Bootstrap garantit une compatibilité mobile, avec un CSS personnalisé pour une esthétique dorée luxueuse.

- **Logique backend** :
  - **Routes Flask** : Gère les requêtes `GET` et `POST` pour lister les cafés (`/`), ajouter des entrées (`/add`) et supprimer des entrées (`/delete/<cafe_id>`).
  - **Modèle SQLAlchemy** : Le modèle `Coffee` définit le schéma de la base de données avec des champs pour l’ID, le nom, l’adresse, le site web, le Wi-Fi, les prises électriques et l’URL de l’image.
  - **Opérations sur la base de données** : Fonctionnalités CRUD pour créer, lire et supprimer des enregistrements de cafés dans une base SQLite.
  - **Traitement des formulaires** : Traite les soumissions de formulaires de manière sécurisée et redirige vers la page d’accueil après ajout ou suppression.

- **Design** :
  - **Esthétique visuelle** : Boutons en dégradé doré et typographie inspirée des marques de café de luxe, utilisant **Playfair Display** et **Cormorant Garamond**.
  - **Éléments interactifs** : Effets de survol sur les boutons, indicateurs emoji pour le Wi-Fi (✅/❌) et les prises électriques, et intégration de Google Maps pour les adresses.
  - **Expérience utilisateur** : Navigation intuitive avec une section héroïque sur la page d’accueil et un formulaire épuré avec une ombre élégante pour l’ajout de cafés.

### Pourquoi ce projet est pertinent

**WorkCoffee** est un projet idéal pour démontrer des compétences en **développement web full-stack** avec **Python** et **Flask**. Il illustre la maîtrise du **développement backend** (Flask, SQLAlchemy), du **design frontend** (Bootstrap, CSS personnalisé) et de la **gestion de bases de données** (SQLite). L’application répond à un besoin réel des travailleurs à distance et des amateurs de café, offrant une solution pratique pour trouver des espaces de travail productifs. Sa structure modulaire et son design responsive en font une base solide pour des améliorations futures, comme l’authentification utilisateur, la recherche ou l’ajout d’images.

##