# <p align="center"> ![image](https://github.com/user-attachments/assets/a615bca9-bd69-4679-b79d-a0d9eaa996db) </p>

## <p align="center"> Amazon Price Alert - Alerte de prix Amazon en Python </p>
### <p align="center"> #Day47 </p>

#### Aperçu
**Amazon Price Alert** est un programme en Python qui surveille le prix d'un produit spécifique sur Amazon. Si le prix du produit devient inférieur à un seuil pré-défini, il envoie une alerte par e-mail. Ce projet utilise **BeautifulSoup** pour le scraping web, **requests** pour l'envoi de requêtes HTTP, et **smtplib** pour envoyer des e-mails.

#### Compétences acquises
- **Web Scraping** : Utilisation de BeautifulSoup pour extraire des informations d'une page web.
- **Requêtes HTTP** : Récupération de données via l'API `requests`.
- **Envoi d'e-mails** : Automatisation de l'envoi d'alertes par e-mail avec **smtplib**.
- **Gestion des variables d'environnement** : Utilisation de `.env` pour la gestion sécurisée des informations sensibles comme l'adresse e-mail et les mots de passe.
- **Manipulation de données** : Conversion de prix en format numérique pour la comparaison.

#### Partie obligatoire
- **Scraping** : Extraire le prix et le titre du produit à partir de la page Amazon.
- **Comparaison** : Vérifier si le prix est inférieur au seuil défini (BUY_PRICE).
- **Alerte** : Envoi d'un e-mail d'alerte si le prix est inférieur au seuil.
- **Environnement sécurisé** : Utilisation de `python-dotenv` pour charger les informations sensibles depuis un fichier `.env`.

#### Pourquoi ce projet est pertinent
**Amazon Price Alert** est un excellent projet pour apprendre le web scraping avec BeautifulSoup, ainsi que l'automatisation des notifications par e-mail. Il offre également une première introduction à l'utilisation des variables d'environnement pour sécuriser les informations sensibles, une compétence clé pour tout projet en production. Ce projet peut être étendu à d'autres sites de commerce en ligne et amélioré pour surveiller plusieurs produits simultanément.
