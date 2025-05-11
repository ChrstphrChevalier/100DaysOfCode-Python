# <p align="center"> ![image](https://github.com/user-attachments/assets/9d1cc291-e667-4ba6-976a-6b88f5a24776) </p>

## <p align="center"> FlaskAuth - Authentification basique avec Flask </p>
### <p align="center"> #Day61 </p>

#### Aperçu
**FlaskAuth** est une application web simple construite avec **Flask** qui implémente un système d’authentification rudimentaire. Elle utilise **Flask-WTF** pour la gestion des formulaires, **WTForms** pour la validation des champs, et **Flask-Bootstrap** pour un rendu élégant des pages HTML. L’utilisateur peut se connecter via une interface `/login` qui redirige vers une page de succès ou d’échec selon les identifiants fournis.

#### Compétences acquises
- **Flask** : Création de routes, rendu de templates avec `render_template`.
- **Formulaires Flask-WTF** : Définition de formulaires avec validations.
- **WTForms** : Champs typés (email, mot de passe), validation de données.
- **Sécurité de base** : Clé secrète pour les formulaires Flask-WTF.
- **Bootstrap5** : Intégration du design Bootstrap dans Flask.
- **Logique conditionnelle** : Vérification des identifiants en POST.

#### Partie obligatoire
- **Formulaire de connexion** avec champ email, mot de passe et bouton de soumission.
- **Validation** des données saisies (champ requis).
- **Traitement conditionnel** : vérification des identifiants saisis (`admin@email.com` / `12345678`).
- **Redirection dynamique** selon que l’utilisateur réussit ou échoue la connexion.
- **Utilisation de Bootstrap 5** pour le style et la responsivité.

#### Pourquoi ce projet est pertinent
**FlaskAuth** est un excellent point de départ pour comprendre l’authentification web avec **Flask**. Il initie aux bonnes pratiques de structure Flask, à la séparation des routes et des templates, ainsi qu’à la sécurité basique via les formulaires sécurisés. Ce projet est une base concrète pour des systèmes de login plus avancés (bases de données, sessions, cookies, etc.).
