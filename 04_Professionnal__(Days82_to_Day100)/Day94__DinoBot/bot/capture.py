import os
import cv2
import numpy as np
import pyautogui
from pynput import keyboard
from datetime import datetime

ROI_X = 1250
ROI_Y = 295
ROI_WIDTH = 250
ROI_HEIGHT = 300

SAVE_DIR = "../data"

def get_next_index(label: str) -> int:
    os.makedirs(SAVE_DIR, exist_ok=True)
    existing = [f for f in os.listdir(SAVE_DIR) if f.startswith(label)]
    return len(existing)

def capture_roi(label: str, index: int):
    # Capture tout l'écran
    screenshot = pyautogui.screenshot()

    # Convertit l'image PIL en array NumPy 3D (Hauteur / Largeur / BGR)
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Découpe la région d'intérêt (ROI)
    roi = frame[ROI_Y:ROI_Y + ROI_HEIGHT, ROI_X:ROI_X + ROI_WIDTH]

    # Crée le dossier de sauvegarde si besoin
    os.makedirs(SAVE_DIR, exist_ok=True)

    # Génère un nom de fichier avec label et index
    filename = f"{label}_{index}.png"
    filepath = os.path.join(SAVE_DIR, filename)

    # Sauvegarde l'image
    cv2.imwrite(filepath, roi)
    print(f"[INFO] Image sauvegardée : {filepath}")

pressed_keys = set()  # Pour suivre les touches déjà pressées

def collect_data():
    print("[INFO] Appuie sur 'o' (obstacle), 'n' (no_obstacle), 'q' pour quitter.")

    def on_press(key):
        try:
            if key.char in pressed_keys:
                return
            pressed_keys.add(key.char)

            if key.char == 'o':
                index = get_next_index("obstacle")
                capture_roi("obstacle", index)
            elif key.char == 'n':
                index = get_next_index("no_obstacle")
                capture_roi("no_obstacle", index)
            elif key.char == 'q':
                print("[INFO] Fin de la collecte.")
                return False
        except AttributeError:
            pass

    def on_release(key):
        try:
            if key.char in pressed_keys:
                pressed_keys.remove(key.char)
        except AttributeError:
            pass

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()