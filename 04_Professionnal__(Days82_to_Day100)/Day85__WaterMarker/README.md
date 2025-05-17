# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> WaterMarker - Application de Filigrane d'Images </p>

### <p align="center"> #Day85 </p>

### Aperçu

**WaterMarker** est une application de bureau développée en **Python** avec **Tkinter** et **Pillow**, permettant de **télécharger une image**, de **choisir un texte personnalisé**, d’y **ajouter un filigrane** à la position souhaitée, avec des **options de couleur et taille du texte**. Le résultat peut être **prévisualisé** et **enregistré** sur l’ordinateur.

### Compétences Utilisées

- **Développement d'interface graphique** : Utilisation de **Tkinter** pour créer une interface utilisateur fluide et intuitive (boutons, menus déroulants, canvas de prévisualisation).
- **Manipulation d’images avec Pillow** : Redimensionnement, ajout de texte, gestion des polices, couleurs et positionnement dynamique sur les images.
- **Programmation orientée objet** : Séparation claire entre les modules (interface, logique de traitement, configuration), améliorant la maintenabilité.
- **Gestion des fichiers** : Ouverture d’images via une boîte de dialogue et sauvegarde locale du résultat modifié.
- **Expérience utilisateur** : Retour visuel immédiat des modifications apportées au filigrane, prévisualisation et feedback utilisateur.

### Mise en Œuvre

- **Interface utilisateur** : 
  - Bouton pour **charger une image**.
  - Entrée pour **le texte du filigrane**.
  - Menus déroulants pour **la position** du filigrane, **la couleur du texte**, et **la taille du texte**.
  - Canvas de **prévisualisation** qui redimensionne automatiquement l’image pour éviter les débordements.
  - Bouton **"Appliquer"** pour voir les modifications et bouton **"Sauvegarder"** pour enregistrer le résultat.

- **Logique de traitement** : 
  - Redimensionnement de l’image source pour un affichage optimal dans l’interface.
  - Calcul dynamique de la position du texte selon l’option choisie (haut, bas, centre, coins…).
  - Application du filigrane en conservant la qualité de l’image.

- **Personnalisation** : 
  - Choix entre plusieurs couleurs (**noir**, **blanc**, **rouge**, **bleu**, etc.).
  - Sélection de tailles de texte prédéfinies (par exemple **20**, **40**, **60**, etc.).
  - Positionnement flexible (**haut gauche**, **centre**, **bas droite**, etc.).

### Pourquoi ce projet est pertinent

**WaterMarker** illustre parfaitement les bases du **développement d'applications de bureau avec Python**, combinant une interface utilisateur graphique, une manipulation d’images avancée et une personnalisation en temps réel. Il démontre des compétences essentielles en **programmation orientée objet**, **gestion d’événements**, **traitement d’images** et **design UX minimaliste**.

C’est un projet utile, concret et facilement réutilisable pour des cas d’usage réels (publication sur réseaux sociaux, protection de photos, etc.). Il peut évoluer vers un outil plus avancé avec des **logos en filigrane**, **glisser-déposer d’image**, ou l’export vers plusieurs formats (**PNG, JPG, PDF**).

##
