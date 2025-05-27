import time
import joblib
import numpy as np
import pyautogui
import cv2
from pynput import keyboard
import threading
import os

# Coordonnées de la région à capturer (ROI)
ROI_X = 1250
ROI_Y = 295
ROI_WIDTH = 250
ROI_HEIGHT = 300

# Taille des images d'entraînement
IMG_SIZE = (100, 30)

# Charge le modèle
model_path = os.path.join(os.path.dirname(__file__), "model", "dino_model.joblib")
model = joblib.load(model_path)
print("✅ Modèle chargé avec succès.")

running = True  # Flag de contrôle pour la boucle

def on_press(key):
    global running
    try:
        if key.char == 'q':
            print("👋 Touche 'q' détectée, arrêt du bot.")
            running = False
            return False  # Arrête le listener
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

def capture_roi():
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    roi = frame[ROI_Y:ROI_Y + ROI_HEIGHT, ROI_X:ROI_X + ROI_WIDTH]
    roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roi_resized = cv2.resize(roi_gray, IMG_SIZE)
    return roi_resized.flatten().reshape(1, -1)

print("🎮 Bot lancé. Appuie sur 'q' pour quitter.")
time.sleep(2)  # Temps pour basculer sur le jeu

while running:
    roi = capture_roi()
    prediction = model.predict(roi)[0]

    if prediction == 1:  # obstacle détecté
        pyautogui.press("space")  # saute
        print("⬆️ Saut !")

    time.sleep(0.05)  # Contrôle la vitesse de boucle