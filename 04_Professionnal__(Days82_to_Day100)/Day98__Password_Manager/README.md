# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> Password_Manager - Gestionnaire de mots de passe CLI chiffré et sécurisé </p>

### <p align="center"> #Day98 </p>

### Aperçu

**Password_Manager** est une application **CLI en Python** conçue pour générer, chiffrer, stocker, récupérer et supprimer des mots de passe de manière sécurisée en utilisant le **chiffrement symétrique Fernet** et la bibliothèque **keyring** (gestionnaire de mots de passe du système).

* Lancement : `python3 cli.py <commande>`
* Commandes disponibles : `generate`, `get`, `delete`
* Technologies : `Python`, `cryptography`, `keyring`, `argparse`

### Compétences Utilisées

* 🔐 **Chiffrement avec Fernet** : sécurisation des mots de passe via `cryptography.fernet`.
* 🔑 **Stockage sécurisé avec keyring** : intégration avec le gestionnaire natif (macOS Keychain, Windows Credential Manager, Linux Secret Service...).
* 🧰 **Interface CLI avec argparse** : gestion simple, claire et rapide des commandes.
* 🛠️ **Structure modulaire** : code organisé en modules (`password_generator`, `crypto`, `keyring_manager`, `cli`).
* 📁 **Création automatique de fichiers secrets** : `.secret.key` généré au lancement si absent.
* 💡 **Pratiques de sécurité** : séparation des responsabilités, chiffrement avant stockage, clé externe.

### Mise en œuvre

* **password_generator.py** : génère un mot de passe aléatoire et sécurisé.
* **crypto.py** :
  * `encrypt_data()` : chiffre une donnée avec une clé secrète.
  * `decrypt_data()` : déchiffre une donnée chiffrée.
  * Gère le fichier `.secret.key` automatiquement.
* **keyring_manager.py** :
  * `save_password(service, username, encrypted_pwd)` : stocke le mot de passe chiffré.
  * `get_password(service, username)` : récupère un mot de passe chiffré.
  * `delete_password(service, username)` : supprime une entrée.
* **cli.py** :
  * `generate` : génère un mot de passe, le chiffre, le stocke.
  * `get` : récupère un mot de passe chiffré, le déchiffre.
  * `delete` : supprime un mot de passe du keyring.

### Pourquoi ce projet est pertinent

Ce projet démontre comment créer un **gestionnaire de mots de passe personnel et sécurisé** en ligne de commande, sans base de données externe, tout en respectant les **bonnes pratiques de sécurité** :

* Utilisation d’un **chiffrement symétrique robuste** (Fernet AES-128),
* **Stockage sécurisé** via le **keyring natif** du système,
* Organisation **modulaire et évolutive** du code,
* Excellente base pour ajouter :
  * Interface graphique (Tkinter, PyQt),
  * Export/Import,
  * Authentification,
  * Synchronisation cloud.

C’est un excellent projet pour approfondir **la sécurité, le chiffrement, l’organisation logicielle et l’expérience utilisateur via une interface CLI moderne**.

##