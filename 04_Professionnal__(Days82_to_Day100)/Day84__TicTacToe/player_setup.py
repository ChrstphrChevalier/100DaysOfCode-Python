import tkinter as tk
from utils import assign_symbols, get_random_bot_name

class PlayerSetupScreen:
    def __init__(self, root, mode, start_game_callback):
        self.root = root
        self.mode = mode
        self.start_game_callback = start_game_callback
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=40)

        self.entries = []
        self.colors = []

        if mode == "solo":
            self.setup_solo()
        elif mode == "local":
            self.setup_local()

    def setup_solo(self):
        self.create_entry("Votre nom :", 0)
        self.create_color_choice(0)
        self.create_start_button()

    def setup_local(self):
        self.create_entry("Nom joueur 1 :", 0)
        self.create_color_choice(0)
        self.create_entry("Nom joueur 2 :", 1)
        self.create_color_choice(1)
        self.create_start_button()

    def create_entry(self, label, index):
        tk.Label(self.frame, text=label, font=("Helvetica", 12)).pack()
        entry = tk.Entry(self.frame)
        entry.pack(pady=5)
        self.entries.append(entry)

    def create_color_choice(self, index):
        tk.Label(self.frame, text="Choisissez la couleur :", font=("Helvetica", 10)).pack()
        var = tk.StringVar(value="blue")
        self.colors.append(var)
        for color in ["blue", "red", "green", "purple"]:
            tk.Radiobutton(self.frame, text=color, variable=var, value=color).pack(anchor="w")

    def create_start_button(self):
        tk.Button(self.frame, text="Commencer", command=self.start_game).pack(pady=20)

    def start_game(self):
        players = []

        if self.mode == "solo":
            name = self.entries[0].get().strip() or "Joueur"
            color = self.colors[0].get()
            bot_name = get_random_bot_name()
            bot_color = "black" if color != "black" else "gray"

            players = [
                {"name": name, "is_bot": False, "color": color},
                {"name": bot_name, "is_bot": True, "color": bot_color},
            ]

        elif self.mode == "local":
            for i in range(2):
                name = self.entries[i].get().strip() or f"Joueur {i+1}"
                color = self.colors[i].get()
                players.append({"name": name, "is_bot": False, "color": color})

        players = assign_symbols(players)
        self.destroy()
        self.start_game_callback(players)

    def destroy(self):
        self.frame.destroy()
