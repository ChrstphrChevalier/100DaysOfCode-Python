# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> Space Invaders - Jeu d'arcade revisité en Python avec Pygame </p>

### <p align="center"> #Day95 </p>

### Aperçu

**Space Invaders** est un **jeu d'arcade classique** réimplémenté en **Python** avec la bibliothèque **Pygame**. Ce projet reproduit l'expérience du célèbre shoot'em up où le joueur contrôle un vaisseau spatial, affronte des vagues d'ennemis aux couleurs variées et défend ses vies en tirant des projectiles. Le jeu gère la **gestion des collisions**, le **mouvement dynamique des ennemis**, la **gestion des vies**, ainsi que des **animations fluides**.

- Lancement : `python3 main.py`
- Assets graphiques : `assets/player.png`, `assets/bullet.png`, `assets/red.png`, `assets/yellow.png`, `assets/green.png`
- Principaux modules : `game.py`, `player.py`, `enemy.py`, `bullet.py`

### Compétences Utilisées

- **Développement de jeux avec Pygame** : Création de la fenêtre, gestion des événements, rendu graphique et mise à jour des objets.
- **Programmation orientée objet (POO)** : Conception modulaire avec classes Player, Enemy, Bullet, Game pour une architecture claire et maintenable.
- **Gestion des collisions** : Détection précise des collisions entre projectiles et ennemis pour gérer les interactions et la destruction.
- **Animations et déplacements dynamiques** : Ennemis se déplaçant horizontalement, changeant de direction, et descendant progressivement pour augmenter la difficulté.
- **Gestion des entrées utilisateur** : Contrôle du vaisseau via clavier (touches gauche/droite, tir avec espace).
- **Système de vies** : Compte à rebours des vies du joueur avec affichage visuel.
- **Chargement et gestion d’assets graphiques** : Images PNG transparentes pour vaisseau, balles et ennemis colorés (rouge, jaune, vert).
- **Organisation du code** : Structure claire avec dossier `src/` et gestion des ressources dans `assets/`.

### Mise en œuvre

- **Initialisation du jeu (`game.py`)** :
  - Configuration de la fenêtre (taille, titre).
  - Création des instances Player, Bullet, et groupe d'Ennemis.
  - Boucle principale avec gestion des événements, mise à jour et rendu.

- **Classe Player (`player.py`)** :
  - Gestion du déplacement horizontal dans les limites de l’écran.
  - Tir de projectiles avec limitation (une balle active à la fois).
  - Chargement de l’image du vaisseau.

- **Classe Enemy (`enemy.py`)** :
  - Gestion du mouvement horizontal avec changement de direction aux bords.
  - Descente progressive après chaque rebond sur un bord.
  - Ennemis de différentes couleurs (rouge, jaune, vert) pour variété visuelle.
  - Chargement des images correspondantes aux couleurs.

- **Classe Bullet (`bullet.py`)** :
  - Déplacement vertical vers le haut.
  - Détection de collision avec les ennemis.
  - Réinitialisation après tir ou collision.

### Pourquoi ce projet est pertinent

Ce **clone de Space Invaders** est un excellent exercice pour comprendre et maîtriser :

- Le **développement de jeux 2D en Python avec Pygame**,
- La **programmation événementielle** et la gestion des entrées utilisateur,
- L’**architecture orientée objet** appliquée à un projet ludique,
- La **gestion des collisions et animations dynamiques**,
- L’importation et la gestion des ressources graphiques pour un rendu propre.

Ce projet pose une base solide pour évoluer vers des jeux plus complexes, intégrant :

- Système de scores et niveaux,
- Sons et musiques intégrés,
- Effets visuels avancés,
- Intelligence artificielle pour ennemis.

Idéal pour tout développeur Python souhaitant allier **programmation ludique** et **concepts fondamentaux de la game dev**.

##