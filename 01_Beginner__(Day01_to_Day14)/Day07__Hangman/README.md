# <p align="center"> ![image](https://github.com/user-attachments/assets/8739a22b-0609-419e-b357-a4ef81b3ce05) </p>

## <p align="center"> Hangman - Jeu du Pendu </p>
### <p align="center"> #Day07 </p>

#### Aperçu
**Hangman** est une implémentation classique du jeu du pendu où l'utilisateur doit deviner un mot lettre par lettre. Si l'utilisateur devine correctement, la lettre est révélée. Sinon, une partie du dessin du pendu apparaît. L'utilisateur a un nombre limité de tentatives (6), et le jeu se termine lorsque soit le mot est deviné, soit le nombre de tentatives atteint zéro.

#### Compétences acquises
- **Manipulation des chaînes de caractères** : masque des lettres du mot et gestion des lettres déjà devinées.
- **Gestion de l’entrée utilisateur** : prise en charge des entrées de l'utilisateur et conversion en minuscules.
- **Utilisation de bibliothèques externes** : importation de fichiers pour la gestion du logo du jeu et des mots à deviner.
- **Structure de données** : utilisation de listes pour afficher les lettres et suivre l'état de la partie.
- **Boucles et conditions** : gestion du déroulement du jeu à travers une boucle `while` et des conditions pour la victoire, la défaite et les tentatives restantes.

#### Fonctionnement du jeu
1. Le programme choisit un mot aléatoire à partir de la liste `hangman_words.word_list`.
2. L'utilisateur doit deviner le mot en proposant des lettres, une à une.
3. Si la lettre proposée est dans le mot, elle est révélée à sa position. Sinon, une partie du pendu est dessinée.
4. Le jeu continue tant qu'il reste des tentatives (lives > 0) et que le mot n'est pas entièrement deviné.
5. Le jeu se termine avec un message de victoire si le mot est deviné ou un message de défaite si les tentatives sont épuisées.

#### Dépendances
- `hangman_art.py` : contient les graphiques pour dessiner le pendu et le logo.
- `hangman_words.py` : contient la liste de mots à deviner.

#### Exemple d'exécution
```plaintext
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    

Guess a letter: e
Right
_ e _ _ _
You have 6 lives left
Guess a letter: t
Wrong
You have 5 lives left
...
```

#### Pourquoi ce projet est pertinent
Le projet **Hangman** permet de pratiquer la gestion des conditions de jeu et de renforcer la logique autour des entrées et sorties utilisateur dans un programme interactif. Ce jeu est une base pour explorer la création de jeux textuels ou de programmes avec une interface utilisateur simple.

