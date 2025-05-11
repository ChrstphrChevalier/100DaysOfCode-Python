# <p align="center"> ![image](https://github.com/user-attachments/assets/9d1cc291-e667-4ba6-976a-6b88f5a24776) </p>

## <p align="center"> Git, GitHub et le contrôle de version </p>
### <p align="center"> #Day70 </p>

### Présentation

- Sujets : Résumé de Git, GitHub et le contrôle de version
- Commandes Git, Création d'un dépôt distant, Création de fichiers (.gitignore), Branchement, Fusion, Clonage, Forking, Requêtes Pull et Push

### Liens

- URL de la solution : [Git, GitHub et le contrôle de version](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day70)
- Aucun exercice, sauf le dossier Projet à Pratiquez quelques commandes.

### Références
- [GitHub GitIgnore](github.com/gitHub/gitignore) est un dépôt appartenant à l'équipe GitHub pour Git Ignore, une collection prédéfinie de modèles Git Ignore utiles.
- [Dépôts adaptés aux débutants](https://github.com/MunGell/awesome-for-beginners)
- [Dépôt de jeux de mots](https://github.com/ritik48/Wordle-Game)
- [Exercices Git](https://learngitbranching.js.org/) Relevez les défis ici pour approfondir vos connaissances de Git, notamment le cherry-picking, le rebase de Git, et bien plus encore.

### Notes
Commandes Git (Windows)
- ```git status```
- ```git init```
- ```git add .```
- ```git commit -m```
- ```git push``` Envoie vers GitHub
- ```git push origin main -u``` Envoie vers GitHub
- ```git rm --cached -r .``` Utilisez ceci pour supprimer des fichiers de ma zone de préparation / annuler la dernière étape.
- ```git log``` Cela vous permet de voir les commits que vous avez effectués.
- ```clear``` (pour vider le terminal)
- Pour quitter l'opération « git log », appuyez sur la touche « q ».

Créer un dépôt distant
- ```git remote add <nom> <url>```
- ```git push -u <nom distant> <nom de la branche>``` Pousse le dépôt local vers le dépôt distant.

Pour créer un fichier :
- ```touch nom-du-fichier.type-de-fichier```

Pour créer un fichier GitIgnore :
- ```touch .gitignore```
- ```code .gitignore``` (Ouvrir GitIgnore pour Windows)

Pour cloner un dépôt
- ```git clone url```

Pour créer une BRANCHE
- git branch nom-de-la-branche
- git branch (Utilisez ceci pour voir sur quelle branche vous vous trouvez)

Pour fusionner les branches
- git merge nom-de-la-branche
- Étapes :
1. Retourner à la branche principale
git checkout main
2. Fusionner
git merge nom-de-la-branche
Remarque : si VIM s’ouvre, saisissez « :q! » (pour enregistrer et quitter)

Pour basculer vers une BRANCHE
- git checkout nom-de-la-branche

GIT CLONE vs. FORKING
- Git clone récupère l'intégralité du dépôt, puis le clone dans votre environnement de travail local. Git clone est utile avec une équipe de confiance disposant des droits de lecture et d'écriture. Elle peut travailler dessus en local, le pousser et résoudre les conflits.
- Le fork consiste à copier/dupliquer un dépôt distant hébergé sur GitHub et à conserver la copie sur votre propre compte GitHub, où vous pouvez y apporter des modifications. Une fois le fork d'un dépôt distant créé, vous pouvez en faire ce que vous voulez.
- Le fork permet à un utilisateur externe de faire ce qu'il veut : ajouter des fonctionnalités, améliorer la base de code, ajouter du code, etc.

PULL REQUESTS
- Si un utilisateur externe souhaite que le créateur original du dépôt intègre ses modifications, il peut effectuer une pull request. Le propriétaire original décide d'intégrer ou non ces demandes, autrement dit de les fusionner.

vs PUSH REQUESTS
- Vous pouvez utiliser votre propre dépôt ou une copie de dépôt.
