# <p align="center"> ![image](https://github.com/user-attachments/assets/9d1cc291-e667-4ba6-976a-6b88f5a24776) </p>

## <p align="center"> BlogMail - Blog personnel avec formulaire de contact </p>
### <p align="center"> #Day60 </p>

#### Aperçu
**BlogMail** est une application web développée avec **Flask** qui permet d’afficher des articles de blog dynamiques et d’envoyer des messages via un formulaire de contact. Les données des articles sont récupérées depuis une API externe, et les messages envoyés via le formulaire sont transmis par email grâce au module **smtplib**.

#### Compétences acquises
- **Flask** : Routage, rendu de templates HTML, gestion des méthodes GET/POST.
- **APIs** : Récupération de données dynamiques via `requests`.
- **Formulaires** : Traitement des entrées utilisateur avec `request.form`.
- **Emailing** : Envoi d’email automatique avec `smtplib`.
- **Templates Jinja** : Intégration dynamique des données dans des pages HTML.

#### Partie obligatoire
- **Affichage du blog** : Page d’accueil listant les articles, page individuelle pour chaque post.
- **Pages fixes** : À propos (`/about`) et contact (`/contact`).
- **Formulaire de contact** : Nom, email, téléphone, message.
- **Envoi de mail** : Les données du formulaire sont envoyées à une adresse définie via SMTP sécurisé.
- **Données JSON dynamiques** : Les articles sont chargés depuis un endpoint JSON hébergé sur npoint.io.

#### Pourquoi ce projet est pertinent
**BlogMail** offre une introduction complète à la création d’une application Flask avec plusieurs routes, gestion de formulaires, récupération de données via API, et envoi d’emails. C’est un projet concret qui simule un mini-CMS personnel avec une vraie fonctionnalité de communication — parfait pour apprendre à structurer un projet web complet en Python.
