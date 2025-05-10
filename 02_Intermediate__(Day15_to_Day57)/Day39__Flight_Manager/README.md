# <p align="center"> ![image](https://github.com/user-attachments/assets/a615bca9-bd69-4679-b79d-a0d9eaa996db) </p>

## <p align="center"> Flight Manager - Gestionnaire de vols en Python </p>
### <p align="center"> #Day39 </p>

#### Aperçu
**Flight Manager** est un programme en Python qui recherche les vols les moins chers vers différentes destinations et envoie des notifications si un vol moins cher est disponible. Ce projet combine l'accès à des données externes, l'utilisation de l'API de recherche de vols, la gestion des données, et l'envoi de notifications via WhatsApp.

#### Compétences acquises
- **Python avancé** : Manipulation des dates, gestion des API, boucles et conditions.
- **Accès aux données** : Utilisation d'un gestionnaire de données pour récupérer et mettre à jour des informations dans Google Sheets.
- **Calculs de dates** : Manipulation des objets `datetime` pour définir des périodes de recherche.
- **Envoi de notifications** : Intégration de la fonctionnalité de notification via WhatsApp.
- **Optimisation des requêtes** : Introduction de délais entre les requêtes pour éviter les restrictions d'API.

#### Partie obligatoire
- **Récupération des données** : Accès aux données de destination depuis Google Sheets et récupération des codes IATA des villes.
- **Recherche de vols** : Vérification des vols disponibles pour chaque destination, à partir de la ville d'origine spécifiée.
- **Notification** : Envoi de notifications lorsque des vols moins chers que le prix actuel de la destination sont trouvés.
- **Mise à jour des données** : Mise à jour des codes IATA et des informations de destination dans Google Sheets.

#### Pourquoi ce projet est pertinent
**Flight Manager** est un projet pratique pour l'apprentissage de l'accès aux API externes, la manipulation de données complexes, et l'automatisation des notifications. Ce programme peut être intégré à de nombreux cas d'usage réels, comme la gestion des alertes de prix pour les voyages, ce qui en fait un projet utile et motivant. De plus, il permet d'explorer des concepts tels que la gestion de l'API, l'interaction avec les services tiers, et l'optimisation des performances avec des délais dans les requêtes.
