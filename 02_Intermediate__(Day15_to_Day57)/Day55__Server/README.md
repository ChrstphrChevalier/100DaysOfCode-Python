# <p align="center"> ![image](https://github.com/user-attachments/assets/a615bca9-bd69-4679-b79d-a0d9eaa996db) </p>

## <p align="center"> Higher Lower - Devinez un nombre en Flask </p>
### <p align="center"> #Day55 </p>

#### Aperçu
**Higher Lower** est un jeu web simple en Python utilisant le framework Flask. L'utilisateur doit deviner un nombre généré aléatoirement entre 0 et 9. Le programme lui indique si son essai est trop bas, trop haut, ou correct, avec des images GIF animées pour rendre l'expérience plus interactive et ludique.

#### Compétences acquises
- **Flask** : Création d'un serveur web basique avec Flask.
- **Génération de nombres aléatoires** : Utilisation de `random.randint()` pour générer un nombre secret.
- **Interaction avec l'utilisateur** : Gestion des entrées utilisateur via les URLs.
- **HTML et CSS** : Création de pages web dynamiques avec des réponses personnalisées.

#### Partie obligatoire
- **Route principale** (`/`) : Affiche un message demandant à l'utilisateur de deviner un nombre entre 0 et 9.
- **Route avec devinette** (`/<int:guess>`) : Vérifie si l'utilisateur a deviné le bon nombre, trop bas, ou trop haut, et retourne une réponse accompagnée d'une image GIF.
- **Gestion des erreurs** : Le programme gère les essais de manière dynamique et fournit une réponse appropriée selon la tentative.

#### Pourquoi ce projet est pertinent
Ce projet est un excellent moyen d'apprendre à interagir avec les utilisateurs à travers un serveur web Flask. Il permet également de comprendre les bases du développement web dynamique, ainsi que l'intégration d'éléments interactifs comme des images GIF. Ce jeu simple, mais amusant, peut être amélioré avec des fonctionnalités supplémentaires comme un compteur d'essais ou un message de félicitations après la victoire.
