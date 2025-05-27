import os
import cv2
import numpy as np

def load_dataset(data_path: str) -> tuple[np.ndarray, np.ndarray]:
    X = []
    y = []
    img_size = (100, 30)

    for label, folder in enumerate(["no_obstacle", "obstacle"]):
        folder_path = os.path.join(data_path, folder)
        for filename in os.listdir(folder_path):
            img_path = os.path.join(folder_path, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue  # image corrompue ou non lisible
            img_resized = cv2.resize(img, img_size)
            X.append(img_resized.flatten())
            y.append(label)

    return np.array(X), np.array(y)
