import tkinter as tk

class GameLogic:
    def __init__(self, root, players, return_to_menu_callback):
        self.root = root
        self.players = players
        self.return_to_menu_callback = return_to_menu_callback
        self.current_player_index = 0
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.buttons = []
        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.status_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text=self.get_score_text(), font=("Helvetica", 12))
        self.score_label.pack()

        self.create_board()
        self.update_status()

    def create_board(self):
        for row in range(3):
            button_row = []
            for col in range(3):
                btn = tk.Button(self.frame, text="", width=6, height=3,
                                font=("Helvetica", 20),
                                command=lambda r=row, c=col: self.play(r, c))
                btn.grid(row=row, column=col)
                button_row.append(btn)
            self.buttons.append(button_row)

        tk.Button(self.root, text="Rejouer", command=self.reset_board).pack(pady=5)
        tk.Button(self.root, text="Menu principal", command=self.return_to_menu).pack(pady=5)

    def get_score_text(self):
        return f"{self.players[0].name}: {self.players[0].score} | {self.players[1].name}: {self.players[1].score}"

    def update_status(self):
        current = self.players[self.current_player_index]
        self.status_label.config(text=f"{current.name} ({current.symbol}) joue...")

    def play(self, row, col):
        if self.board[row][col] != "":
            return
        current = self.players[self.current_player_index]
        self.board[row][col] = current.symbol
        self.buttons[row][col].config(text=current.symbol, fg=current.color)
        if self.check_winner(current.symbol):
            current.score += 1
            self.status_label.config(text=f"{current.name} a gagné !")
            self.score_label.config(text=self.get_score_text())
            self.disable_buttons()
        elif all(cell != "" for row in self.board for cell in row):
            self.status_label.config(text="Match nul !")
        else:
            self.current_player_index = 1 - self.current_player_index
            self.update_status()
            self.root.after(500, self.play_bot_if_needed)

    def play_bot_if_needed(self):
        current = self.players[self.current_player_index]
        if current.is_bot:
            # IA simple : joue au hasard
            empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ""]
            if empty_cells:
                import random
                row, col = random.choice(empty_cells)
                self.play(row, col)



    def check_winner(self, symbol):
        b = self.board
        for i in range(3):
            if all(b[i][j] == symbol for j in range(3)) or all(b[j][i] == symbol for j in range(3)):
                return True
        if all(b[i][i] == symbol for i in range(3)) or all(b[i][2-i] == symbol for i in range(3)):
            return True
        return False

    def disable_buttons(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")

    def reset_board(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for btn in row:
                btn.config(text="", state="normal")
        self.update_status()

    def return_to_menu(self):
        self.destroy()
        self.return_to_menu_callback()

    def destroy(self):
        self.frame.destroy()
        self.status_label.destroy()
        self.score_label.destroy()
