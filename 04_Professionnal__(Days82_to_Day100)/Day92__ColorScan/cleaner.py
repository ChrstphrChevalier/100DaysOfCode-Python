import os, time

UPLOAD_FOLDER = os.path.join("static", "uploads")
LIFETIME = 60 * 60 * 24  # 24h en secondes

for f in os.listdir(UPLOAD_FOLDER):
    path = os.path.join(UPLOAD_FOLDER, f)
    if os.path.isfile(path):
        if time.time() - os.path.getmtime(path) > LIFETIME:
            os.remove(path)
