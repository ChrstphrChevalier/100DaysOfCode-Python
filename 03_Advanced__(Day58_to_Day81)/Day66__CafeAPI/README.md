# <p align="center"> ![image](https://github.com/user-attachments/assets/9d1cc291-e667-4ba6-976a-6b88f5a24776) </p>

## <p align="center"> Cafe API - API RESTful de gestion de cafés avec Flask </p>
### <p align="center"> #Day66 </p>

#### Aperçu
**CafeAPI** est une API web simple construite avec **Flask** et **SQLAlchemy** permettant de gérer une base de données de cafés. Elle offre plusieurs endpoints RESTful pour consulter, ajouter, modifier et supprimer des cafés. Ce projet met en pratique la **création d'API**, l'**interaction avec une base SQLite**, la **sérialisation JSON**, et les **méthodes HTTP**.

#### Compétences acquises
- **Flask** : Routing, gestion des requêtes HTTP, templates HTML.
- **SQLAlchemy ORM** : Modélisation de base de données avec classes, mapping, création de schéma.
- **REST API** : Méthodes GET, POST, PATCH, DELETE.
- **JSON** : Sérialisation des objets Python en format JSON pour communication avec l’API.
- **Sécurité basique** : Vérification d’une clé API pour certaines routes sensibles.
- **Utilisation de base de données** : Création automatique des tables avec `db.create_all()`.

#### Partie obligatoire
- **Endpoints disponibles** :
  - `/` : Page d'accueil (HTML).
  - `/random` : Récupère un café aléatoire.
  - `/all` : Liste de tous les cafés.
  - `/search?loc=` : Rechercher les cafés par localisation.
  - `/add` *(POST)* : Ajoute un nouveau café à la base.
  - `/update-price/<id>?new_price=` *(PATCH)* : Met à jour le prix du café.
  - `/report-closed/<id>?api-key=` *(DELETE)* : Supprime un café avec clé API.

- **Base de données SQLite** :
  - Champs : `name`, `map_url`, `img_url`, `location`, `seats`, `has_toilet`, `has_wifi`, `has_sockets`, `can_take_calls`, `coffee_price`.

- **Fonctionnalité clé** : Conversion automatique des objets modèles en dictionnaires grâce à la méthode `to_dict()`.

#### Pourquoi ce projet est pertinent
**CafeAPI** est un excellent projet pour apprendre à construire une **API REST** en Python avec Flask. Il couvre toutes les bases essentielles : création de routes, gestion de requêtes, connexion à une base de données, manipulation de données, et retour en JSON. C’est une très bonne porte d’entrée vers le **développement backend** moderne.
