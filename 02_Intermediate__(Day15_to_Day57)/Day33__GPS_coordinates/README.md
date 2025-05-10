# <p align="center"> ![image](https://github.com/user-attachments/assets/a615bca9-bd69-4679-b79d-a0d9eaa996db) </p>

## <p align="center"> ISS Overhead & GPS Coordinates - Suivi de la Station Spatiale Internationale et coordonnées GPS </p>
### <p align="center"> #Day33 </p>

#### Aperçu
**ISS Overhead & GPS Coordinates** est un projet Python combinant deux fonctionnalités : le suivi en temps réel de la Station Spatiale Internationale (ISS) et l'obtention des coordonnées GPS de l'utilisateur. Le programme envoie une alerte par e-mail lorsque l'ISS passe au-dessus de votre position, et permet de récupérer les coordonnées géographiques de votre appareil.

#### Compétences acquises
- **API en Python** : Utilisation d'APIs externes (Open Notify, Sunrise-Sunset).
- **Gestion d'email** : Envoi d'alertes par e-mail avec SMTP.
- **Manipulation de données JSON** : Traitement des réponses des APIs.
- **Conversion d'heures** : Transformation de données horaires pour déterminer le jour et la nuit.
- **Géolocalisation** : Récupération de la position GPS de l'utilisateur via geocoder.

#### Partie obligatoire
1. **Suivi ISS** : Utilisation de l'API Open Notify pour récupérer les coordonnées de l'ISS et les comparer avec la latitude et la longitude de l'utilisateur.
2. **Vérification de la nuit** : L'API Sunrise-Sunset est utilisée pour déterminer si l'heure actuelle correspond à la nuit, afin d'envoyer l'alerte uniquement la nuit.
3. **Envoi d'alerte par e-mail** : Si l'ISS est au-dessus de l'utilisateur et qu'il fait nuit, un e-mail est envoyé pour informer l'utilisateur.
4. **Récupération des coordonnées GPS** : Le module `geocoder` est utilisé pour obtenir les coordonnées géographiques de l'utilisateur.
   
#### Pourquoi ce projet est pertinent
Ce projet combine plusieurs concepts utiles dans le monde réel, tels que l'interaction avec des APIs, l'envoi d'e-mails automatisés, et la géolocalisation. Il démontre comment intégrer des données externes pour créer un programme réactif et utile. En plus d’être une introduction pratique à la manipulation d'APIs, ce projet développe des compétences en automatisation et en interaction avec l'environnement de l'utilisateur.
