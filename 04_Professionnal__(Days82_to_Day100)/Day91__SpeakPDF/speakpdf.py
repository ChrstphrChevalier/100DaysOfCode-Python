import PyPDF2
import pyttsx3
import sys

def pdf_to_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
        return text
    except Exception as e:
        print(f"Erreur lors de la lecture du PDF : {e}")
        sys.exit(1)

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # vitesse de la voix
    engine.setProperty('volume', 1.0)  # volume (0.0 à 1.0)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation : python script.py fichier.pdf")
        sys.exit(1)

    pdf_file = sys.argv[1]
    contenu = pdf_to_text(pdf_file)

    if contenu.strip():
        print("Lecture en cours...")
        speak_text(contenu)
    else:
        print("Aucun texte lisible trouvé dans le PDF.")
