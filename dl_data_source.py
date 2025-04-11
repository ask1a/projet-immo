import requests

url = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/fiscalite-locale-des-particuliers/exports/csv?lang=fr&timezone=Europe%2FParis&use_labels=true&delimiter=%3B"
destination = "data/fonciere.csv"

# Télécharger le fichier
response = requests.get(url, stream=True)
with open(destination, "wb") as fichier:
    for chunk in response.iter_content(chunk_size=8192):  # Télécharge par blocs
        fichier.write(chunk)

print("Fichier téléchargé avec succès !")
