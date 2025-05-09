## <p align="center"> Escaping the Maze - Évasion du labyrinthe </p>
### <p align="center"> #Day06 </p>

#### Aperçu
**Escaping_the_Maze** est un projet d'algorithmie utilisant une simulation (avec [Reeborg's World](https://reeborg.ca/)) où un robot doit sortir d’un labyrinthe en appliquant une stratégie simple d’exploration murale (main droite).

#### Compétences acquises
- **Structures de contrôle** : `while`, `if/elif/else`.
- **Logique conditionnelle** : détection d'obstacles et de sorties (`front_is_clear()`, `right_is_clear()`, `at_goal()`).
- **Fonctions personnalisées** : création d’une fonction `turn_right()` à partir de `turn_left()`.
- **Pensée algorithmique** : application de la stratégie "main droite" pour naviguer dans un espace inconnu.

#### Partie obligatoire
- Détection du mur frontal → tourner à gauche.
- Tant que l'objectif n'est pas atteint :
  - Si le chemin à droite est libre → tourner à droite et avancer.
  - Sinon si le chemin devant est libre → avancer.
  - Sinon → tourner à gauche.
- Utilisation de la fonction `turn_right()` définie manuellement.

#### Pourquoi ce projet est pertinent
Ce projet développe la **logique d’exploration** et d’**adaptation à un environnement dynamique**. Il oblige à penser en termes d’actions séquentielles et de conditions, ce qui est fondamental en robotique, en intelligence artificielle et en résolution de problèmes complexes.
