# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> SpeakPDF – Écoutez vos PDF à haute voix </p>

### <p align="center"> #Day91 </p>

### Aperçu

**SpeakPDF** est une application **Python** en ligne de commande qui transforme n’importe quel fichier **PDF** en **voix synthétique**.

Grâce à **PyPDF2** pour l'extraction de texte et **pyttsx3** pour la synthèse vocale, ce petit utilitaire vous permet d’écouter le contenu d’un document, simplement et rapidement.

### Compétences utilisées

* 🔹 **Manipulation de fichiers PDF** : lecture et extraction de texte avec PyPDF2.
* 🔹 **Synthèse vocale** : conversion du texte en parole avec pyttsx3.
* 🔹 **Programmation Python** : gestion des erreurs, traitement de fichiers, structure propre.
* 🔹 **Utilisation de la ligne de commande** : passage d'arguments via `sys.argv`.
* 🔹 **Scripts réutilisables** : code clair et modulaire pour une utilisation rapide.

### Mise en œuvre

#### Utilisation

```bash
python3 speakpdf.py your_file.pdf
```

* Le script ouvre le fichier PDF, en extrait le texte et le lit à voix haute.
* Si le PDF est vide ou non lisible, une alerte s’affiche.
* La voix est paramétrée pour être claire, à une vitesse de lecture modérée.

#### Logique du script

* **Lecture PDF** :

  * Ouverture en binaire (`rb`) avec `PdfReader`.
  * Extraction texte page par page.
* **Synthèse vocale** :

  * Initialisation de `pyttsx3`.
  * Lecture du texte dans le terminal (aucune interface graphique).

### Pourquoi ce projet est pertinent

**SpeakPDF** est un projet court, utile et facile à maintenir.
Il illustre comment utiliser **Python pour automatiser une tâche réelle** et intégrer plusieurs bibliothèques externes.

Un bon exercice pour pratiquer :

* la manipulation de fichiers,
* le traitement de texte brut,
* l’intégration de voix de synthèse.

##