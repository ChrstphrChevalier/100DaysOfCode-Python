from flask import Flask, request, render_template
from utils import extract_dominant_colors as edc
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.static_folder, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    colors = []
    filename = None

    if request.method == 'POST':
        file = request.files.get("image")
        num_colors = int(request.form.get("num_colors", 5))
        if file and file.filename != "":
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            colors = edc(filepath, n_colors=num_colors)
            filename = file.filename

    return render_template('index.html', colors=colors, image_path=filename)