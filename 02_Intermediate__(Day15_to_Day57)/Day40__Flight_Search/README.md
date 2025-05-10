# <p align="center"> ![image](https://github.com/user-attachments/assets/a615bca9-bd69-4679-b79d-a0d9eaa996db) </p>

## <p align="center"> Flight Search - Recherche de vol </p>
### <p align="center"> #Day40 </p>

#### Aperçu
**Flight Search** est une application Python qui permet de rechercher les vols les moins chers entre une ville d'origine et plusieurs destinations, en utilisant les données d'un Google Sheet. Le programme récupère les codes aéroport des destinations, effectue une recherche de vols directs, puis recherche des vols avec escales si aucun vol direct n'est disponible. Enfin, il envoie des notifications par WhatsApp et email aux clients si le prix d'un vol est inférieur à un seuil défini.

#### Compétences acquises
- **Gestion des dates et heures** : Utilisation des modules `datetime` et `timedelta`.
- **API Google Sheets** : Manipulation des données à partir de Google Sheets avec la classe `DataManager`.
- **Recherche d'informations** : Interrogation d'API externes pour la recherche de vols (directs et avec escales).
- **Notifications** : Envoi d'emails et de messages WhatsApp avec des informations sur les vols.
- **Programmation orientée objet** : Utilisation de classes pour organiser le code (ex. `FlightSearch`, `NotificationManager`).

#### Partie obligatoire
- **Entrées** : Données des destinations et des codes aéroport depuis Google Sheets.
- **Traitements** : Recherche de vols directs et indirects, comparaison des prix avec un prix minimal défini.
- **Sorties** : Notifications envoyées aux clients si un vol est disponible à un prix inférieur à celui du seuil.
- **Robustesse** : Gestion des erreurs, comme l'absence de vol direct.

#### Pourquoi ce projet est pertinent
Le projet **Flight Search** est un excellent moyen d'appliquer des concepts avancés de Python, tels que l'utilisation de dates et d'API externes, ainsi que de mettre en pratique des compétences en gestion des notifications et en manipulation de données. Ce projet est utile pour les applications dans le secteur du voyage, offrant des alertes en temps réel sur les opportunités de vol à bas prix.
