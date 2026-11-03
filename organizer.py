import os
import shutil

def organizza_cartella(percorso_cartella):
    if not os.path.isdir(percorso_cartella):
        print(f"Il percorso '{percorso_cartella}' non è una cartella valida.")
        return

    categorie = {
        "Immagini": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
        "Documenti": [".pdf", ".docx", ".txt", ".odt", ".xlsx", ".pptx", ".csv"],
        "Archivi": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Video": [".mp4", ".mkv", ".avi", ".mov"],
        "Musica": [".mp3", ".wav", ".flac"],
        "Codice": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java"]
    }
    categoria_per_estensione = {
        estensione: categoria
        for categoria, estensioni in categorie.items()
        for estensione in estensioni
    }

    print(f"Organizzo: {percorso_cartella}")

    for filename in os.listdir(percorso_cartella):
        file_path = os.path.join(percorso_cartella, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        if not ext:
            continue

        categoria = categoria_per_estensione.get(ext, "Altro")
        cartella_destinazione = os.path.join(percorso_cartella, categoria)
        os.makedirs(cartella_destinazione, exist_ok=True)
        shutil.move(file_path, os.path.join(cartella_destinazione, filename))
        print(f"Spostato: {filename} -> {categoria}/")

    print("Fatto.")

if __name__ == "__main__":
    percorso = input("Inserisci il percorso della cartella da ordinare: ").strip().strip("'\"")
    organizza_cartella(percorso)