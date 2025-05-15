class Player:
    def __init__(self, name, is_bot=False, color="blue", symbol=None):
        self.name = name
        self.is_bot = is_bot
        self.color = color
        self.symbol = symbol
        self.score = 0
