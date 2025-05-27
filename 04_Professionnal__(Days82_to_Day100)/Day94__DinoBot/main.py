import os
import argparse
import numpy as np
from bot.capture import collect_data
from bot.preprocess import load_dataset
from bot.trainer import train_model

def main():
    parser = argparse.ArgumentParser(description="DinoBot - collecte ou entraînement")
    parser.add_argument(
        "mode",
        choices=["collect", "train"],
        help="Mode d'exécution : collect pour capturer des images, train pour entraîner le modèle"
    )
    args = parser.parse_args()

    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, "data")

    if args.mode == "collect":
        print("[INFO] Mode collecte activé.")
        collect_data()

    elif args.mode == "train":
        print("[INFO] Mode entraînement activé.")
        X, y = load_dataset(data_path)
        print(f"✅ Dataset chargé avec {X.shape[0]} images")
        print(f"🧠 Shape X : {X.shape}")
        print(f"🏷️ Labels : {np.unique(y, return_counts=True)}")

        model = train_model(X, y)

if __name__ == "__main__":
    main()
