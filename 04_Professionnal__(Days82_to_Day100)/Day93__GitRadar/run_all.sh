#!/bin/bash

echo "📥 [1/2] Scraping et export des données..."
python3 main.py

echo ""
echo "🚀 [2/2] Lancement du dashboard Streamlit..."
streamlit run streamlit_app.py
