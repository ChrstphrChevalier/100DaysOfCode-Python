#!/bin/bash

# Création des sous-dossiers
mkdir -p morse tests

# Fichiers Python
touch morse/__init__.py
touch morse/encoder.py
touch morse/decoder.py
touch tests/test_encoder.py
touch tests/test_decoder.py
touch cli.py

# pyproject.toml vide (sera rempli plus tard)
touch pyproject.toml

# README
echo "# Morse Pro" > README.md

# .gitignore Python standard
cat <<EOF > .gitignore
__pycache__/
*.pyc
*.pyo
*.pyd
.env
.venv/
env/
venv/
dist/
build/
*.egg-info/
EOF

# Initialisation Git
git init

echo "✅ Arborescence du projet créée dans Day82__Morse_Pro."
