# Hlavička projektu
"""
Mach_projekt_3_main.py: třetí projekt do Engeto Online Python Akademie

author: Jiří Mach
email: machi@vscht.cz
"""

### WEB SCRAPER ###
# Import knihoven 
import os
import csv
import sys
from requests import get
from bs4 import BeautifulSoup as bs

# Definice uživatelských funkcí
def html2text(url: str):
    """Načte HTML obsah stránky s obcemi vybraného regionu NEBO samotné obce a převede jej do textové podoby."""
    response = get(url)
    return bs(response.text, features="html.parser")

def region_name(html: str) -> str:
    """Extrahuje název vybraného regionu."""
    return html.select_one("#publikace > h3:nth-child(3)").text.strip()

def city_data_extractor(html: str) -> list:
    """Extrahuje kódy obcí zvoleného regionu, jejich URL adresy a názvy. Ukládá je do podoby listů."""
    city_codes = [code.text for code in html.select("td.cislo > a")]
    city_urls = [os.path.join(url_base, city_url["href"]) for city_url in html.select("td.cislo > a")]
    city_names = [name.text.strip() for name in html.select("td.overflow_name")]
    return city_codes, city_urls, city_names

def party_scraper(table_num: int):
    """Scrapuje názvy politických stran a počet příslušných hlasů"""
    for l in range(3, 16): 
        css_selector_votes = f"#inner > div:nth-child({table_num}) > table > tr:nth-child({l}) > td:nth-child(3)"
        css_selector_party = f"#inner > div:nth-child({table_num}) > table > tr:nth-child({l}) > td.overflow_name"
        party_votes_s = city_html.select_one(css_selector_votes)                       
        valid_party_s = city_html.select_one(css_selector_party)
    
        if valid_party_s and party_votes_s:
            party_name = valid_party_s.text.replace("\xa0", " ").strip() 
            party_votes = party_votes_s.text.replace("\xa0", " ").strip()  

            if party_name not in city_data:
                city_data[party_name] = party_votes
                party_names[party_name] = None  

def city_info_collector() -> dict:
    """Vrací slovník naplnění informacemi o obci - kód, název, počet voličů, počet obálek a počet validních hlasů"""
    return {
    "code": city_codes[i],
    "location": city_names[i],
    "registered": city_html.select_one("#ps311_t1 > tr:nth-child(3) > td:nth-child(4)").text.replace("\xa0", ""),
    "envelopes": city_html.select_one("#ps311_t1 > tr:nth-child(3) > td:nth-child(5)").text.replace("\xa0", ""),
    "valid": city_html.select_one("#ps311_t1 > tr:nth-child(3) > td:nth-child(8)").text.replace("\xa0", "")
}

def city_info_writer():
    """Zapisuje vyscrapovaná data o obcích vybraného regionu do CSV souboru."""
    with open(csv_filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()  # Zapisuje hlavičku
        writer.writerows(region_votes_info)  # Zapisuje data

# Definice základních proměnných 
region_votes_info = []
party_names = dict()
url_base = "https://www.volby.cz/pls/ps2017nss/"

# HLAVNÍ ČÁST KÓDU
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Nesprávný zápis názvu skriptu nebo systémových argumentů.\nPoužij následující zápis: python <název_skriptu>.py '<URL>' '<název_CSV_souboru>'")
        sys.exit(1)

    # Hlavní URL adresa webu, uživatelský input přes systémové argumenty
    url = sys.argv[1]
    csv_filename = csv_file = sys.argv[2]

    print(f"Stahuji data z webové stránky: {url}.")

    # Získání odpovědi serveru v podobě HTML struktury zvoleného "hlavního" regionu, např. Prostějov
    region_html = html2text(url)

    # Scrapování názvu regionu
    region = region_name(region_html)

    # Scrapování kódů, URL adres a názvů obcí zvoleného regionu 
    city_codes, city_urls, city_names = city_data_extractor(region_html)

    # Scrapování dat pro jednotlivá města zvoleného regionu
    for i in range(len(city_urls)):
    # for i in range(1):
        city_html = html2text(city_urls[i])
                
        city_data = city_info_collector()

        # Politické strany a hlasy z první a druhé tabulky
        party_scraper(1) 
        party_scraper(2)

        # Přidání výsledků města do seznamu
        region_votes_info.append(city_data)

    # Zapsání vyscrapovaných informací o obcích zvoleného regionu do CSV souboru.
    fieldnames = ["code", "location", "registered", "envelopes", "valid"] + list(party_names.keys())
    city_info_writer()

    print(f"Vyextrahovaná data ukládám do souboru: {csv_file}.")
    print("Ukončuji proces extrahování.") 