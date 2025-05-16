# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> Tic Tac Toe - Jeu de Morpion Interactif </p>

### <p align="center"> #Day84 </p>

### Aperçu

**Tic Tac Toe** est une application de bureau développée en **Python** avec la bibliothèque **Tkinter**, offrant une expérience interactive du classique jeu de morpion. Ce projet permet de jouer en mode **solo** (contre une IA simple) ou en mode **local** (deux joueurs). Les joueurs peuvent personnaliser leurs noms, couleurs, et l'application gère les scores, les matchs nuls, et propose des options pour rejouer ou revenir au menu principal.

### Compétences Utilisées

- **Développement d'interface graphique** : Utilisation de **Tkinter** pour créer une interface utilisateur intuitive avec des boutons, des labels, et des entrées personnalisables.
- **Logique de jeu** : Implémentation d'une logique de morpion avec détection de victoire, match nul, et gestion des tours des joueurs.
- **Programmation orientée objet** : Structuration du code en classes (**TicTacToeApp**, **GameLogic**, **PlayerSetupScreen**, **Player**) pour une modularité et une maintenabilité accrues.
- **IA simple** : Développement d'une intelligence artificielle basique pour le mode solo, jouant aléatoirement sur les cases vides.
- **Gestion des entrées utilisateur** : Personnalisation des noms et couleurs des joueurs, avec attribution aléatoire des symboles (**X** ou **O**).

### Mise en Œuvre

- **Interface utilisateur** : Création d’un menu principal avec des options pour le mode **solo** (contre IA) ou **local** (deux joueurs). Les joueurs peuvent entrer leurs noms et choisir leurs couleurs via une interface de configuration.
- **Logique de jeu** : Le plateau 3x3 est représenté par une grille de boutons interactifs. La logique vérifie les conditions de victoire (lignes, colonnes, diagonales) ou de match nul, met à jour les scores, et passe au joueur suivant.
- **Mode solo** : L’IA choisit aléatoirement une case vide après un délai de 500 ms, simulant un tour de jeu.
- **Fonctionnalités supplémentaires** : Boutons pour **rejouer** (réinitialisation du plateau) et **retourner au menu principal**. Affichage dynamique des scores et du statut du joueur actuel.
- **Personnalisation** : Les joueurs peuvent choisir parmi plusieurs couleurs (**bleu**, **rouge**, **vert**, **violet**), et l’IA reçoit un nom aléatoire parmi une liste prédéfinie.

### Pourquoi ce projet est pertinent

**Tic Tac Toe** démontre une maîtrise des bases du **développement d'applications de bureau** avec **Python** et **Tkinter**, en combinant une interface utilisateur graphique, une logique de jeu robuste, et une IA simple. Ce projet illustre des compétences en **programmation orientée objet**, **gestion d’événements**, et **interaction utilisateur**. Il est idéal pour les débutants souhaitant apprendre à créer des applications interactives ou pour les développeurs cherchant à explorer **Tkinter**.

Le projet peut évoluer avec des améliorations comme une IA plus intelligente (utilisant l’algorithme **Minimax**), une sauvegarde des scores dans une base de données, ou une interface graphique plus stylisée avec des thèmes personnalisables.


