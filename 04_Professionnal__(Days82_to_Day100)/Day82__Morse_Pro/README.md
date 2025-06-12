# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> Morse Pro - Encodeur et Décodeur de Code Morse </p>

### <p align="center"> #Day82 </p>

### Aperçu

**Morse Pro** est une bibliothèque Python permettant d'encoder et de décoder des messages en code Morse de manière simple et rapide. Que ce soit pour des applications de communication, des projets éducatifs, ou simplement pour découvrir le code Morse, **Morse Pro** fournit une solution pratique à travers Python.

### Compétences Utilisés
- **Programmation Python** : Développement d'un module Python structuré avec gestion de fichiers et modules.
- **Traitement de texte** : Manipulation de chaînes de caractères pour convertir entre texte et code Morse.
- **Tests unitaires** : Mise en place de tests pour assurer la fiabilité du code (avec `unittest` ou `pytest`).
- **Packaging et distribution** : Création d'une bibliothèque Python publiée sur PyPI.

### Mise en Oeuvre
- **Encodage du texte** : Conversion du texte en une chaîne de code Morse, caractère par caractère.
- **Décodage du Morse** : Retour du code Morse à son texte d'origine, gestion des erreurs de formatage.
- **Tests** : Tests unitaires pour s'assurer que les fonctions d'encodage et de décodage fonctionnent correctement.

### Pourquoi ce projet est pertinent

**Morse Pro** est une démonstration idéale de l'application d'une logique simple à un problème pratique, tout en offrant une extension vers un projet plus complexe de programmation Python. Ce projet combine des aspects fondamentaux du développement logiciel, comme la gestion de modules et la gestion des erreurs, ce qui en fait un excellent outil d'apprentissage.

En plus d'être utile dans un contexte pédagogique, ce projet peut être intégré dans divers systèmes de communication ou applications nécessitant une interface texte simplifiée. La gestion du code Morse, bien que vieille, reste un concept fondamental dans l'histoire des communications.

---

[![PyPI version](https://badge.fury.io/py/morse-pro.svg)](https://pypi.org/project/morse-pro/)

---

### 🔧 Installation

```bash
pip3 install morse_pro
````

---

### 🚀 Usage

#### Depuis votre IDE :

```python
from morse.encoder import encode_to_morse
from morse.decoder import decode_from_morse

# Encoder du texte en code Morse
print(encode_to_morse("hello"))  # Sortie : .... . .-.. .-.. ---

# Décoder du code Morse en texte
print(decode_from_morse(".... . .-.. .-.. ---"))  # Sortie : hello
```

##
