# <p align="center"> ![image](https://github.com/user-attachments/assets/284b5e6f-22e2-4e06-8fd3-a8d311c3dc31) </p>

## <p align="center"> Higher or Lower - Devine qui a le plus de followers </p>
### <p align="center"> #Day14 </p>

#### Aperçu
**Higher or Lower** est un jeu Python dans lequel l'utilisateur doit deviner quelle célébrité possède le plus de followers sur les réseaux sociaux parmi deux propositions. Chaque bonne réponse augmente le score, et le jeu continue jusqu'à la première erreur. Ce projet introduit les **structures de contrôle**, les **dictionnaires**, la **manipulation de listes**, et la **logique conditionnelle** dans un format interactif.

#### Compétences acquises
- **Manipulation de dictionnaires** : Accès aux données d'une célébrité (nom, description, pays, followers).
- **Randomisation** : Sélection aléatoire d'éléments sans répétition via `random.sample()` et `random.choice()`.
- **Logique conditionnelle** : Comparaison de valeurs, contrôle de flux avec if/else.
- **Fonctions** : Création d'une fonction personnalisée `switch()` pour gérer le remplacement des célébrités.
- **Boucle de jeu** : Maintien d'une session interactive continue jusqu'à erreur.
- **Nettoyage d'affichage** : Réinitialisation partielle de l’écran entre les tours.

#### Partie obligatoire
- **Affichage clair** : Présentation des célébrités comparées avec description et origine.
- **Input utilisateur** : Choix entre A ou B pour désigner la célébrité la plus populaire.
- **Comparaison des followers** : Vérification de la réponse selon les données du dictionnaire.
- **Mise à jour dynamique** : Remplacement des célébrités sans doublon et score incrémenté.
- **Fin de partie** : Message d'erreur et score final affiché si mauvaise réponse.

#### Pourquoi ce projet est pertinent
**Higher or Lower** est un excellent exercice pour renforcer la logique de décision et la gestion de données structurées avec des dictionnaires. Il initie à la création d'une boucle de jeu interactive et à la gestion d'erreurs utilisateur de manière intuitive. De plus, il montre comment structurer un projet en plusieurs fichiers (`art.py`, `stars.py`) pour un meilleur découpage du code.
