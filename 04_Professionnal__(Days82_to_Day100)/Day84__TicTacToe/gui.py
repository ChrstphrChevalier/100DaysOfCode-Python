import tkinter as tk
from player_setup import PlayerSetupScreen
from game_logic import GameLogic
from player import Player

class TicTacToeApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x500")
        self.players = []
        self.current_screen = None
        self.menu_screen()

    def menu_screen(self):
        self.clear_screen()
        frame = tk.Frame(self.window)
        frame.pack(pady=100)

        tk.Label(frame, text="Tic Tac Toe", font=("Helvetica", 20)).pack(pady=20)

        tk.Button(frame, text="Solo (vs IA)", width=20, command=lambda: self.start_setup("solo")).pack(pady=10)
        tk.Button(frame, text="Local (2 joueurs)", width=20, command=lambda: self.start_setup("local")).pack(pady=10)

        self.current_screen = frame

    def start_setup(self, mode):
        self.clear_screen()
        self.current_screen = PlayerSetupScreen(self.window, mode, self.launch_game)

    def launch_game(self, players):
        self.clear_screen()
        self.players = [Player(**p) for p in players]
        self.current_screen = GameLogic(self.window, self.players, self.menu_screen)

    def clear_screen(self):
        if self.current_screen:
            if isinstance(self.current_screen, tk.Frame):
                self.current_screen.destroy()
            else:
                self.current_screen.destroy()
        for widget in self.window.winfo_children():
            widget.destroy()

    def run(self):
        self.window.mainloop()
