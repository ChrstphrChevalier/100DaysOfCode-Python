import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.base import BaseEstimator
import joblib
import os

def train_model(X: np.ndarray, y: np.ndarray) -> BaseEstimator:
    # Split des données
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Modèle
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Évaluation
    y_pred = model.predict(X_test)
    print("📊 Rapport de classification :\n", classification_report(y_test, y_pred))

    # Sauvegarde du modèle
    model_dir = os.path.join(os.path.dirname(__file__), "..", "model")
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "dino_model.joblib")
    joblib.dump(model, model_path)
    print(f"✅ Modèle sauvegardé ici : {model_path}")

    return model
