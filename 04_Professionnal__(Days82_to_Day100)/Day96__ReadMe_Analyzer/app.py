from flask import Flask, render_template, request
import requests
import re

app = Flask(__name__)

GITHUB_RAW_URL = "https://raw.githubusercontent.com/{repo}/main/README.md"

def analyze_readme(content):
    word_count = len(re.findall(r'\w+', content))
    score = 0
    suggestions = []

    if word_count > 300:
        score += 1
    else:
        suggestions.append("Le README est trop court. Essayez d’atteindre au moins 300 mots.")

    if "## Installation" not in content and "# Installation" not in content:
        suggestions.append("Ajoutez une section `Installation` pour expliquer comment utiliser le projet.")
    else:
        score += 1

    if "## Usage" not in content and "# Usage" not in content:
        suggestions.append("Ajoutez une section `Usage` pour montrer comment lancer l’application.")
    else:
        score += 1

    if "## License" not in content and "# License" not in content:
        suggestions.append("Ajoutez une section `License` pour indiquer les droits d’utilisation.")
    else:
        score += 1

    if "## Contributing" not in content and "# Contributing" not in content:
        suggestions.append("Ajoutez une section `Contributing` pour guider les contributeurs.")
    else:
        score += 1

    return {
        "word_count": word_count,
        "score": score,
        "suggestions": suggestions
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    repo = ""
    if request.method == 'POST':
        repo = request.form.get('repo').strip()
        if '/' not in repo:
            error = "Format invalide. Utilise 'owner/repo'."
        else:
            url = GITHUB_RAW_URL.format(repo=repo)
            r = requests.get(url)
            if r.status_code == 200:
                content = r.text
                result = analyze_readme(content)
            else:
                error = f"Impossible de récupérer le README (status {r.status_code})"
    return render_template("index.html", result=result, error=error, repo=repo)

if __name__ == '__main__':
    app.run(debug=True)
