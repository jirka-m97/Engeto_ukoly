# Popis projektu
Tento projekt slouží k extrahování výsledků voleb z roku 2017. Uživateli umožňuje procházet výsledky hlasování v rámci jednotlivých obcí uživatelem zvoleného libovolného okresu. Výstupem je *.csv soubor, který je možné dále analyzovat. 

# Instalace knihoven
Tento volně dostupný open-source projekt vyžaduje stažení knihoven, které jsou souhrně zmíněny v dokumentu "requirements.txt". Pro vytvoření virtuálního prostředí je možné knihovny souhrně stáhnout pomocí následující zápisu v konzoli VS Code:

pip install -r requirements.txt

Po stažení všech potřebných knihoven je projekt připraven pro použití uživatelem.

# Ukázka projektu
(pro okres Prostějov)
Upozornění: Zkotrolujte, že máte aktivované virtuální prostředí, kód by nemusel fungovat dle Vašich představ.

## Spuštění
Projekt "main.py" je standardně spouštěn z příkazového řádku a vyžaduje 2 povinné systémové argumenty. Prvním je URL adresa zvoleného okresu a druhým je název *.csv souboru, do kterého budou uložena vyextrahovaná data.  


- Zápis do příkazové řádky:
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "vysledky_voleb_prostejov.csv" 

## Průběh
Správný průběh kódu je možné identifikovat pomocí následujícího výpisu v terminálu:

Stahuji data z webové stránky: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103.
Vyextrahovaná data ukládám do souboru: vysledky_voleb_prostejov.csv.
Ukončuji proces extrahování.

## Ukázka části výstupu kódu
code,location,registered,envelopes,valid,Občanská demokratická strana,...
506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18,0,5,32,0,0,6,0,0,1,1,15,0
589268,Bedihošť,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34,0,6,140,0,0,26,0,0,0,0,82,1
589276,Bílovice-Lutotín,431,279,275,13,0,0,32,0,8,40,1,0,4,0,0,30,0,3,83,0,0,22,0,0,0,1,38,0
...









