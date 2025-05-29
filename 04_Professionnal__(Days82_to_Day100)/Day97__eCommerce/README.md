# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> eCommerce - Site de vente simple avec Stripe & Flask </p>

### <p align="center"> #Day97 </p>

### Aperçu

**eCommerce** est une application web développée en **Python** avec **Flask**, qui permet de gérer une boutique en ligne simple. L’utilisateur peut consulter les produits disponibles, ajouter de nouveaux articles, et simuler un achat via **Stripe Checkout**.

* Lancement : `python3 app.py`
* URL : `http://localhost:5000`
* Technologies : `Flask`, `Jinja2`, `Stripe`, `JSON`, `HTML/CSS`

### Compétences Utilisées

* **Développement web avec Flask** : Routage, gestion de formulaires, rendu dynamique des pages.
* **Gestion de fichiers JSON** : Lecture/écriture de produits dans un fichier `products.json`.
* **Intégration de Stripe Checkout** : Simulation de paiements sécurisés avec redirection.
* **Design moderne** : Utilisation de **CSS responsive** et structure HTML claire.
* **Séparation logique front/back** : Templates propres, backend clair, données structurées.

### Mise en œuvre

* **app.py** :

  * Route `/` : affiche les produits disponibles.
  * Route `/create` : ajoute un nouveau produit.
  * Route `/checkout/<pid>` : initie une session Stripe Checkout pour un produit.
  * Gestion d’erreurs si aucun produit n’est présent ou si `products.json` est vide.
  * Crée automatiquement le fichier `products.json` s’il est absent.

* **templates/** :

  * `index.html` : page d’accueil listant tous les produits.
  * `create.html` : formulaire d’ajout de produit.
  * `checkout.html` : page de redirection Stripe.
  * `empty.html` : message lorsqu’aucun produit n’est disponible.

* **static/** :

  * `styles.css` : design responsive avec une mise en page épurée.

### Pourquoi ce projet est pertinent

Ce projet montre comment construire une **application e-commerce légère** avec **paiement simulé**, gestion de fichiers locaux et **design responsive**. Il est idéal pour apprendre :

* À structurer une app Flask avec plusieurs routes et templates,
* À manipuler des fichiers de données (JSON) pour stocker des produits,
* À intégrer des solutions de paiement tierces (Stripe),
* À créer une **interface utilisateur agréable et fonctionnelle**.

Ce projet peut servir de base pour des projets plus ambitieux avec **base de données**, **authentification**, ou **inventaire**.

##