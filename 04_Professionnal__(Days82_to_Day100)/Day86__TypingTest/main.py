import tkinter as tk
from tkinter import ttk
import time
import random

PHRASES = [
    "Un algorithme est une suite d'instructions pour résoudre un problème.",
    "La mémoire RAM permet de stocker des données temporairement.",
    "L'adresse IP identifie un appareil sur un réseau.",
    "Python est un langage interprété et multi-paradigme.",
    "Un bug est une erreur dans un programme informatique.",
    "Git est un système de gestion de versions décentralisé.",
    "Une API permet la communication entre deux logiciels.",
    "Linux est un système d'exploitation libre et open-source.",
    "La compilation transforme du code source en code machine.",
    "Un serveur web fournit des pages web aux clients.",
    "Un conteneur Docker isole une application et ses dépendances.",
    "L'UDP est un protocole réseau sans vérification de réception.",
    "HTTPS chiffre les échanges entre client et serveur.",
    "Le HTML structure le contenu d'une page web.",
    "Le CSS permet de styliser les éléments HTML.",
    "Une fonction est un bloc de code réutilisable.",
    "Un tableau est une structure de données indexée.",
    "La complexité algorithmique mesure la performance d'un algorithme.",
    "Un firewall filtre le trafic réseau entrant et sortant.",
    "Un hash est une empreinte unique d'une donnée.",
    "L'encapsulation est un principe fondamental de la POO.",
    "Un thread permet l'exécution parallèle de tâches.",
    "Une base de données stocke et organise les données.",
    "SQL est un langage pour manipuler des bases de données.",
    "L'injection SQL est une faille de sécurité critique.",
    "La boucle for est utilisée pour répéter des actions.",
    "Une classe est un modèle pour créer des objets.",
    "Un système binaire est basé sur les chiffres 0 et 1.",
    "SSH permet d'accéder à un serveur à distance en toute sécurité.",
    "Le protocole TCP assure une transmission fiable des données.",
    "L'open source permet la consultation et la modification du code.",
    "JSON est un format léger d'échange de données.",
    "Un IDE est un environnement de développement intégré.",
    "Les permissions contrôlent l'accès aux fichiers sous Linux.",
    "Le chiffrement protège les données contre les accès non autorisés.",
    "L'intelligence artificielle simule des comportements humains.",
    "Une boucle infinie peut bloquer un programme.",
    "Un commit enregistre des modifications dans un dépôt Git.",
    "Un réseau local relie plusieurs machines dans une zone restreinte.",
    "La virtualisation permet d'exécuter plusieurs OS sur une seule machine.",
    "Un protocole réseau définit les règles de communication.",
    "Un DNS traduit un nom de domaine en adresse IP.",
    "Le cloud computing permet d'utiliser des ressources à distance.",
    "Un token d’authentification vérifie l’identité d’un utilisateur.",
    "Un opérateur logique permet de combiner des conditions.",
    "Un framework accélère le développement logiciel.",
    "Le kernel est le cœur du système d’exploitation.",
    "La récursivité est une fonction qui s'appelle elle-même.",
    "Un pointeur contient l'adresse d'une variable.",
    "Le garbage collector libère automatiquement la mémoire inutilisée."
]

class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Test de Vitesse de Frappe")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 10))
        self.style.configure("TLabel", font=("Arial", 11))
        self.style.configure("TEntry", font=("Arial", 11))

        self.start_time = None
        self.best_wpm = 0
        self.running = False
        self.phrase = random.choice(PHRASES)

        self.frame = ttk.Frame(root, padding=20)
        self.frame.pack(expand=True)

        self.label_text = ttk.Label(self.frame, text=self.phrase, wraplength=560, font=("Arial", 12, "italic"))
        self.label_text.pack(pady=(0, 10))

        self.entry = tk.Text(self.frame, height=4, width=70, font=("Arial", 12), wrap="word")
        self.entry.pack(pady=5)
        self.entry.bind("<KeyPress>", self.start_timer)

        self.timer_label = ttk.Label(self.frame, text="Temps : 0.0s")
        self.timer_label.pack(pady=(10, 0))

        self.result = ttk.Label(self.frame, text="", font=("Arial", 12, "bold"))
        self.result.pack(pady=5)

        self.best_label = ttk.Label(self.frame, text="🏆 Meilleur score : 0 WPM")
        self.best_label.pack(pady=(0, 15))

        self.button = ttk.Button(self.frame, text="Recommencer", command=self.reset)
        self.button.pack()

    def start_timer(self, event):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            self.update_timer()
            self.check_typing()

    def update_timer(self):
        if self.running:
            elapsed = time.time() - self.start_time
            self.timer_label.config(text=f"Temps : {elapsed:.1f}s")
            self.root.after(100, self.update_timer)

    def check_typing(self):
        if not self.running:
            return

        typed = self.entry.get("1.0", tk.END).strip()
        if typed == self.phrase:
            self.running = False
            elapsed = time.time() - self.start_time
            wpm = round(len(self.phrase.split()) / (elapsed / 60))
            self.result.config(text=f"✅ Terminé ! Vitesse : {wpm} mots/minute.")
            if wpm > self.best_wpm:
                self.best_wpm = wpm
                self.best_label.config(text=f"🏆 Meilleur score : {self.best_wpm} WPM")
        else:
            self.root.after(100, self.check_typing)

    def reset(self):
        self.running = False
        self.start_time = None
        self.phrase = random.choice(PHRASES)
        self.label_text.config(text=self.phrase)
        self.entry.delete("1.0", tk.END)
        self.result.config(text="")
        self.timer_label.config(text="Temps : 0.0s")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
