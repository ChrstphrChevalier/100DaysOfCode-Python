# <p align="center"> ![image](https://github.com/user-attachments/assets/a615bca9-bd69-4679-b79d-a0d9eaa996db) </p>

## <p align="center"> Trading News - Suivi de l'actualité boursière en Python </p>
### <p align="center"> #Day36 </p>

#### Aperçu
**Trading News** est un programme Python qui permet de suivre les actualités boursières en temps réel en fonction des variations de prix d'une action spécifique. Le programme récupère les données de l'action via l'API d'Alphavantage, analyse les fluctuations de son prix et envoie les dernières actualités concernant l'entreprise à l'aide de l'API NewsAPI. Il utilise également Twilio pour envoyer ces informations par SMS à un utilisateur vérifié.

#### Compétences acquises
- **APIs** : Utilisation d'API externes (Alphavantage et NewsAPI).
- **Gestion des données JSON** : Extraction et manipulation des données JSON.
- **Calculs de pourcentage** : Calcul de la variation du prix de l’action en pourcentage.
- **Envoi de SMS avec Twilio** : Intégration de l'API Twilio pour l'envoi de messages.
- **Logique conditionnelle** : Mise en place de la logique pour envoyer des notifications uniquement en cas de variation significative du prix de l'action.

#### Partie obligatoire
- **Entrées** : Clés API pour Alphavantage, NewsAPI, et Twilio, ainsi que les numéros de téléphone à utiliser.
- **Récupération des données** : Requête API pour obtenir les prix boursiers et les actualités de l'entreprise.
- **Analyse** : Calcul de la différence de prix entre deux jours consécutifs et pourcentage de variation.
- **Envoi de notifications** : Envoi des 3 premières actualités pertinentes par SMS si la variation dépasse 1%.

#### Pourquoi ce projet est pertinent
**Trading News** permet de comprendre comment intégrer plusieurs API dans un programme Python et comment utiliser des outils comme Twilio pour automatiser l'envoi de notifications. Il permet également de manipuler des données financières et de travailler avec des calculs de pourcentage pour évaluer la performance d’une action. Ce projet est utile pour ceux qui souhaitent s'intéresser à l'automatisation du trading ou à la surveillance d'actualités financières en temps réel.
