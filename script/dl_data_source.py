import requests

def dl_file(url, destination):
    response = requests.get(url, stream=True)
    with open(destination, "wb") as fichier:
        for chunk in response.iter_content(chunk_size=8192):  # Télécharge par blocs
            fichier.write(chunk)
    print("Fichier téléchargé avec succès !")

url_fonciere = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/fiscalite-locale-des-particuliers/exports/csv?lang=fr&timezone=Europe%2FParis&use_labels=true&delimiter=%3B"
destination_fonciere = "data/fonciere.csv"
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
dl_file(url_fonciere, destination_fonciere)

url_loyapp12_37m2 = "https://static.data.gouv.fr/resources/carte-des-loyers-indicateurs-de-loyers-dannonce-par-commune-en-2024/20241205-153048/pred-app12-mef-dhup.csv"
url_loyapp_52m2 = "https://static.data.gouv.fr/resources/carte-des-loyers-indicateurs-de-loyers-dannonce-par-commune-en-2024/20241205-153050/pred-app-mef-dhup.csv"
url_loyapp3_72m2 = "https://static.data.gouv.fr/resources/carte-des-loyers-indicateurs-de-loyers-dannonce-par-commune-en-2024/20241205-145658/pred-app3-mef-dhup.csv"
url_loymai_92m2 = "https://static.data.gouv.fr/resources/carte-des-loyers-indicateurs-de-loyers-dannonce-par-commune-en-2024/20241205-145700/pred-mai-mef-dhup.csv"
destination_loy_37m2 = "data/loyapp12_37m2.csv"
destination_loy_52m2 = "data/loyapp_52m2.csv"
destination_loy_72m2 = "data/loyapp3_72m2.csv"
destination_loy_92m2 = "data/loymai_92m2.csv"
'''
id_zone : Identifiant maille
INSEE_C : Code INSEE de la commune
LIBGEO : Nom de la commune
EPCI : Siren de l’EPCI
DEP : Code du département
REG : Code de la région
loypredm2 : Indicateur de loyer en €/m2
lwr.IPm2 upr.IPm2 : Respectivement borne basse et supérieure de l’intervalle de prédiction à 95% (€/m2)
TYPPRED : Niveau de la prédiction
nbobs_com : Nombre d’observations dans la commune
nbobs_mail : Nombre d’observations dans la maille
R2_adj : Coefficient de détermination ajusté du modèle hédonique servant à l’estimation de l’indicateur de loyer
'''
dl_file(url_loyapp12_37m2, destination_loy_37m2)
dl_file(url_loyapp_52m2, destination_loy_52m2)
dl_file(url_loyapp3_72m2, destination_loy_72m2)
dl_file(url_loymai_92m2, destination_loy_92m2)
