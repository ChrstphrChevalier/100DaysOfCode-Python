import cv2
import numpy as np
import pyautogui
import time

# Coordonnées de départ (à ajuster après test)
ROI_X = 1250
ROI_Y = 295
ROI_WIDTH = 250
ROI_HEIGHT = 300

def live_preview():
    print("[INFO] Appuie sur 'q' pour quitter.")

    while True:
        # Capture de l'écran
        screenshot = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Découpe la zone
        roi = frame[ROI_Y:ROI_Y + ROI_HEIGHT, ROI_X:ROI_X + ROI_WIDTH]

        # Affiche la zone dans une petite fenêtre
        cv2.imshow("Region of Interest (ROI)", roi)

        # Quitte avec la touche 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    time.sleep(2)  # Petit délai pour switcher sur Chrome
    live_preview()
