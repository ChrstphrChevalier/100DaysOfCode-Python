# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> TypingTest - Application de Vitesse de Frappe </p>

### <p align="center"> #Day86 </p>

### Aperçu

**TypingTest** est une application de bureau développée en **Python** avec **Tkinter**, conçue pour tester votre **vitesse de frappe en mots par minute (WPM)** à travers un panel de **phrases techniques liées à l’informatique**. L’utilisateur peut lancer un test, taper une phrase aléatoire, voir sa vitesse en temps réel et recommencer à volonté via une interface graphique épurée.

### Compétences Utilisées

- **Développement d'interface graphique** : Utilisation de **Tkinter** et **ttk** pour une interface utilisateur fluide, claire et responsive.
- **Gestion d’événements clavier** : Détection précise du premier caractère tapé pour lancer le timer automatiquement.
- **Mesure de performance** : Calcul du **WPM (Words Per Minute)** à partir du nombre de caractères tapés et du temps écoulé.
- **Sélection aléatoire de contenu** : Panel de plus de **50 phrases** techniques, toutes liées au domaine de l'informatique, pour garantir une variété de tests.
- **Expérience utilisateur** : Bouton de redémarrage, retour immédiat sur les performances, design propre et agréable à utiliser.

### Mise en Œuvre

- **Interface utilisateur** :
  - **Zone d'affichage** de la phrase à taper.
  - **Zone de saisie** qui se réinitialise à chaque test.
  - **Bouton "Restart"** pour relancer un test instantanément.
  - **Affichage dynamique** de la vitesse de frappe en WPM.

- **Logique de test** :
  - Le timer démarre automatiquement à la première frappe.
  - Le WPM est calculé dès que l’utilisateur termine la phrase correctement.
  - Une nouvelle phrase est proposée à chaque redémarrage, sans répétition immédiate.

- **Design moderne** :
  - Utilisation de `ttk.Style()` pour styliser les éléments graphiques.
  - Mise en page centrée, police lisible, couleurs douces et contraste suffisant pour le confort visuel.

### Pourquoi ce projet est pertinent

**TypingTest** est un projet simple, mais parfaitement adapté pour illustrer des compétences pratiques en **développement Python desktop**. Il mêle UX soignée, logique de performance en temps réel, et sélection intelligente de contenu.

Ce type d’application est idéal comme projet d’entraînement ou comme mini-défi de développement. Il peut facilement évoluer vers un outil plus complet : **mode contre-la-montre**, **statistiques de progression**, ou encore **sauvegarde des scores locaux**.

##
