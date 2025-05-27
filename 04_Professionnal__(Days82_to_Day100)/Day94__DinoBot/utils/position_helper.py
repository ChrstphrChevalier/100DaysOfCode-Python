# utils/position_helper.py
import pyautogui
import time

print("Tu as 5 secondes pour placer ta souris là où tu veux capturer (juste devant le dino)...")
time.sleep(5)

x, y = pyautogui.position()
print(f"Coordonnées du curseur : x={x}, y={y}")
