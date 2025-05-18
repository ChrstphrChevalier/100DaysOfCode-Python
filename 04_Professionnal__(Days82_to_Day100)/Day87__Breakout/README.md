# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> Breakout - Jeu de Casse-Briques en Python </p>

### <p align="center"> #Day87 </p>

### Aperçu

**Breakout** est un jeu de **casse-briques** développé en **Python** à l’aide du module **turtle**. Le joueur contrôle une raquette pour renvoyer une balle et détruire les blocs. La difficulté augmente progressivement avec la **vitesse de la balle**, et un système de **vies** a été ajouté pour rendre le jeu plus fun et challengeant. Le style graphique est simple, rétro et accessible à tous.

### Compétences Utilisées

- **Programmation & logique de jeu** : gestion de la balle, des collisions, du score et des conditions de victoire/défaite.
- **Utilisation de la bibliothèque `turtle`** : pour dessiner les éléments (balle, raquette, briques) et gérer l’animation en temps réel.
- **Gestion d’événements clavier** : contrôle fluide du paddle avec les flèches gauche/droite.
- **Système de progression** : augmentation progressive de la vitesse de la balle, remise à zéro des blocs après défaite, et suivi du score.
- **Implémentation d’un système de vies** : le joueur a 3 essais avant le game over, rendant le jeu plus stratégique.

### Mise en Œuvre

- **Interface utilisateur (graphique via `turtle`)** :
  - Paddle contrôlable à la base de l’écran.
  - Balle en mouvement constant, rebondissant sur les murs et les blocs.
  - Affichage en haut de l’écran du score et des vies restantes.

- **Logique de jeu** :
  - La balle rebondit sur les bords, le paddle, et les blocs.
  - Chaque bloc touché disparaît et augmente le score.
  - À chaque contact avec le paddle, la balle accélère légèrement.
  - Si la balle tombe en bas : une vie est perdue, la balle et le paddle sont reset.
  - Game Over après 3 vies perdues, ou message de victoire si tous les blocs sont détruits.

- **Design** :
  - Style rétro minimaliste en noir, blanc, rouge et couleurs de blocs.
  - Effet visuel de disparition des blocs et messages de fin stylisés en plein écran.
  - Contrôles intuitifs : flèches gauche/droite + touches `R` pour rejouer et `Q` pour quitter.

### Pourquoi ce projet est pertinent

**Breakout** est un projet parfait pour mettre en pratique les bases de la **programmation graphique** et de la **logique de jeu** avec Python. Il illustre des concepts fondamentaux : gestion d'événements, boucle de jeu, collisions, feedback visuel, et gestion de la difficulté.


##
