# <p align="center"> ![image](https://github.com/user-attachments/assets/973b6d5f-7202-4b73-a622-498e2766e50b) </p>

## <p align="center"> Write or Die – Écrivez sans vous arrêter... ou perdez tout </p>

### <p align="center"> #Day90 </p>

### Aperçu

**Write or Die** est une application web minimaliste et stimulante développée avec **Flask**.
Elle vous pousse à écrire sans interruption : **si vous arrêtez de taper pendant 5 secondes, votre texte disparaît**.

Construite avec **Python**, **Flask**, **HTML/CSS** et **JavaScript**, cette application offre une interface épurée pour tester votre discipline d’écriture dans une ambiance sérieuse… et impitoyable.

### Compétences utilisées

* 🔹 **Développement web avec Flask** : gestion des routes et rendu de template.
* 🔹 **Intégration HTML/CSS** : mise en page responsive, typographie lisible.
* 🔹 **Programmation JavaScript** : minuterie active qui efface le texte en cas d’inactivité.
* 🔹 **Logique Python** : structure backend simple et efficace.
* 🔹 **Architecture modulaire** : séparation du code frontend (HTML/JS/CSS) et backend (Flask).

### Mise en œuvre

#### Interface utilisateur

* **Page principale (`index.html`)** :

  * Zone de texte pleine largeur et grande hauteur.
  * Message d’instruction clair : tapez ou tout sera perdu.
  * Design responsive pour une utilisation mobile ou desktop.

* **Fonctionnalité principale** :

  * **Timer de 5 secondes** déclenché à chaque frappe.
  * Si aucune saisie n’est détectée avant la fin du décompte : **le texte est effacé** automatiquement.

#### Logique backend

* **Routes Flask** :

  * `GET /` : sert la page HTML principale.

*Pas de base de données ni de stockage : l’expérience est volontairement volatile.*

#### Design

* **Interface minimaliste** :

  * Fond sobre, typographie simple.
  * Zone d’écriture centrale, large, bien visible.
* **Interactions** :

  * JavaScript détecte l’activité clavier (`input`).
  * Le minuteur redémarre à chaque saisie.
  * Alertes et effacement si inactivité prolongée.

### Pourquoi ce projet est pertinent

**Write or Die** est un projet court mais percutant.
Il démontre la capacité à concevoir une **expérience utilisateur dynamique** avec une logique **JavaScript** côté client et une structure **Flask** propre côté serveur.

Parfait pour explorer :

* la réactivité en frontend,
* l’intégration HTML/JS avec un backend Python,
* les limites de l’expérience utilisateur volontairement frustrante mais motivante.

Un excellent exercice pour tester ses compétences en **web app minimaliste**, **timing frontend** et **design UX ciblé**.

##