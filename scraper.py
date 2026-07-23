from pathlib import Path
import requests

def get_teryt_doc():
    """Otwiera i przygotowuje plik źródłowy z danymi TERYT do dalszego przetwarzania."""
    source_teryt = open('C:\\Users\\Artur\\Downloads\\TERC_23-07-2026.csv', 'r', encoding='utf-8')
    teryt_data = source_teryt.read()
    source_teryt.close()
    return teryt_data

def extract_teryt(source_teryt_doc):
    """Ekstrahuje odpowiednie dane TERYT z pliku źródłowego i zwraca je w formie Stringa"""
    teryt_doc_separated = source_teryt_doc.splitlines()
    for field in teryt_doc_separated:
        if 'Wrocław' in field:
            teryt_value = field.split(';')[0] + field.split(';')[1]
            return teryt_value
    return None

def update_url_with_teryt(teryt_code):
    """Aktualizuje URL z danymi transakcji cenowych, dodając do niego odpowiedni kod TERYT."""
    url = 'https://opendata.geoportal.gov.pl/InneDane/latest_exports/rcn_transakcje_ceny/GPKG/_transakcje_ceny.gpkg.zip'
    updated_url = url.replace('GPKG/', f'GPKG/{teryt_code}')
    return updated_url

teryt_doc_name = update_url_with_teryt(extract_teryt(get_teryt_doc())).split('GPKG/')[1]

teryt_info = requests.get(update_url_with_teryt(extract_teryt(get_teryt_doc())))
print(teryt_info)