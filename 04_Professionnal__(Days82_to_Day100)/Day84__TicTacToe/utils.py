import random

BOT_NAMES = [
    "Zorg", "Kira", "Neo", "Luna", "Orion", "Eve", "HAL", "Tron", "Echo", "Nova",
    "Sky", "Lex", "Byte", "Cortex", "Glitch", "Sage", "Vega", "Axel", "Nemo", "Kai"
]

def assign_symbols(players):
    symbols = ["X", "O"]
    random.shuffle(symbols)
    for i, p in enumerate(players):
        p["symbol"] = symbols[i]
    return players

def get_random_bot_name():
    return random.choice(BOT_NAMES)
