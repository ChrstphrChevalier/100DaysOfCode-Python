# <p align="center"> ![image](https://github.com/user-attachments/assets/a615bca9-bd69-4679-b79d-a0d9eaa996db) </p>

## <p align="center"> Hiding API - Prévision météo et notification </p>
### <p align="center"> #Day35 </p>

#### Aperçu
**Hiding API** est un projet en Python qui utilise l'API OpenWeatherMap pour récupérer des prévisions météorologiques et, si de la pluie est prévue, envoie une notification par SMS via Twilio. Ce projet met en œuvre des concepts de **requêtes HTTP**, de **gestion d'API**, et de **notifications par SMS**.

#### Compétences acquises
- **API Web** : Utilisation d'OpenWeatherMap pour récupérer des données météo.
- **Requêtes HTTP** : `requests.get()`, gestion des erreurs avec `raise_for_status()`.
- **JSON** : Extraction de données depuis une réponse JSON.
- **Twilio API** : Envoi de messages SMS via Twilio pour notifier d’un événement.
- **Contrôles logiques** : Analyse des conditions météo pour décider si une notification est nécessaire.

#### Partie obligatoire
- **Entrées** : Utilisation d'une clé API OpenWeatherMap et des identifiants Twilio.
- **Requêtes API** : Récupération des prévisions météo pour la localisation donnée.
- **Analyse** : Vérification des conditions météorologiques pour la possibilité de pluie.
- **Notification** : Envoi d'un message SMS via Twilio si la pluie est prévue.
- **Sécurité** : Masquage des clés API et identifiants sensibles.

#### Pourquoi ce projet est pertinent
Ce projet est une excellente manière d'apprendre à manipuler des API externes, notamment pour récupérer et traiter des données JSON. Il montre également comment intégrer des services tiers (comme Twilio) pour envoyer des notifications automatisées. Ce genre de projet est utile pour automatiser des tâches quotidiennes, et il constitue une base pour des applications plus complexes d'alertes ou de notifications personnalisées.
