# <p align="center"> ![image](https://github.com/user-attachments/assets/9d1cc291-e667-4ba6-976a-6b88f5a24776) </p>

## <p align="center"> Safe Signin - Application de connexion sécurisée </p>
### <p align="center"> #Day68 </p>

#### Aperçu
**Safe Signin** est une application web développée avec Flask, permettant une gestion sécurisée des utilisateurs. Les utilisateurs peuvent s'inscrire, se connecter et accéder à une page protégée nécessitant une authentification. Les mots de passe sont hachés à l'aide de la méthode `pbkdf2:sha256` pour garantir la sécurité des données. Ce projet met en pratique l'utilisation de **Flask**, **SQLAlchemy**, **Flask-Login**, et la gestion de sessions utilisateurs.

#### Compétences acquises
- **Flask** : Création d'une application web avec gestion des routes, des formulaires et des templates.
- **SQLAlchemy** : Gestion des bases de données avec création de tables et requêtes.
- **Flask-Login** : Implémentation de la gestion des sessions utilisateurs pour la connexion et la déconnexion.
- **Sécurité** : Hachage des mots de passe avec `generate_password_hash` et vérification avec `check_password_hash`.
- **Gestion des erreurs** : Gestion des erreurs d'authentification avec des messages d'alerte personnalisés.

#### Partie obligatoire
- **Inscription** : Création d'un utilisateur avec un email unique et un mot de passe sécurisé.
- **Connexion** : Authentification des utilisateurs via email et mot de passe.
- **Pages protégées** : Accès à une page secrète réservée aux utilisateurs connectés.
- **Déconnexion** : Possibilité de se déconnecter et d'être redirigé vers la page d'accueil.
- **Téléchargement sécurisé** : Accès à un fichier uniquement pour les utilisateurs connectés.

#### Pourquoi ce projet est pertinent
**Safe Signin** est un projet idéal pour maîtriser l'authentification d'utilisateurs dans des applications web. En utilisant Flask et SQLAlchemy, ce projet met l'accent sur les bonnes pratiques de sécurité, notamment le hachage des mots de passe, la gestion des sessions et l'utilisation de base de données. Ce projet est une base solide pour tout développement nécessitant une gestion d'utilisateurs et une protection des données sensibles.
