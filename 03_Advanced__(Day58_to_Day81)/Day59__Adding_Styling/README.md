# <p align="center"> ![image](https://github.com/user-attachments/assets/9d1cc291-e667-4ba6-976a-6b88f5a24776) </p>

## <p align="center"> Blog Website - Mini blog dynamique avec Flask </p>
### <p align="center"> #Day59 </p>

#### Aperçu
**Blog Website** est une application web dynamique construite avec **Flask**, un micro-framework Python. Elle récupère dynamiquement les données d’un blog depuis une API externe (JSON hébergé) et les affiche sous forme de posts individuels. Ce projet met en œuvre les **routes Flask**, le **rendu de templates HTML**, et l’**intégration de données externes** via **API**.

#### Compétences acquises
- **Flask (Python)** : Initialisation d'une app Flask, définition de routes, `@app.route()`, lancement du serveur.
- **Rendu de templates** : Utilisation de `render_template()` pour injecter des données dans le HTML.
- **Requêtes API** : Récupération de contenu JSON via `requests.get()`.
- **Gestion dynamique des routes** : Affichage d’un article en fonction de son `id` dans l’URL.
- **Structuration d’un site** : Pages "Home", "About", "Contact", et "Post".

#### Partie obligatoire
- **Routes** : `/`, `/about`, `/contact`, `/post/<int:index>`.
- **Données** : Import des articles de blog depuis une API JSON externe.
- **Templates HTML** : Utilisation de fichiers `.html` pour le rendu visuel des pages.
- **Navigation** : Liens fonctionnels entre les différentes pages du site.
- **Affichage** : Chaque post est affiché individuellement avec ses données spécifiques.

#### Pourquoi ce projet est pertinent
Ce mini-projet est une excellente introduction au **développement web backend avec Flask**. Il démontre comment structurer une application multi-pages, consommer une API, et afficher des données dynamiquement avec des templates HTML. Ce type d'application pose les bases pour des projets plus complexes comme un CMS, un blog complet, ou une API REST.
