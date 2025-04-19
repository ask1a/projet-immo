import requests

url = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/fiscalite-locale-des-particuliers/exports/csv?lang=fr&timezone=Europe%2FParis&use_labels=true&delimiter=%3B"
destination = "data/fonciere.csv"
'''
Liste des acronymes
CA : Communauté d’agglomération
CC : Communauté de communes
CU : Communauté urbaine
MET : Métropole
TEOM : Taxe d’enlèvement des ordures ménagères
TFB : Taxe foncière sur les propriétés bâties
TFNB : Taxe foncière sur les propriétés non bâties
TH : Taxe d’habitation
THRS : Taxe d’habitation sur les résidences secondaires
THLV : Taxe d’habitation sur les logements vacants
'''
# Télécharger le fichier
response = requests.get(url, stream=True)
with open(destination, "wb") as fichier:
    for chunk in response.iter_content(chunk_size=8192):  # Télécharge par blocs
        fichier.write(chunk)

print("Fichier téléchargé avec succès !")
