# Hlavička projektu
"""
Mach_projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jiří Mach
email: machi@vscht.cz
"""

# Import zdrojových textů
import task_template
"""
Import textů ze souboru "task_template.py"
(pozor, soubor se zdrojovými texty musí být ve stejné složce
jako "Mach_projekt_1.py"); 
následný výběr konkrétního textu pomocí indexování
"""

# Nastavení proměnných
words_uppper = 0
words_title = 0
words_lower = 0
words_num = 0
sum_num = 0
occurence = 0
words_dict = {}
dashed_line_len = 40

# Definice vlastních funkcí
def dashed_line():
    print("-"*dashed_line_len)
    
# Registrovaní uživatelé
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

# Textový analyzátor - hlavní kód 
print(5*"#", " TEXT ANALYZER ", 5*"#")
dashed_line()

# Vstupy od uživatele - jméno a heslo
user_name = input("Username: ")
password = input("Password: ")
dashed_line()

# Kontrola zaregistrování uživatele
if user_name in users.keys() and password in users.values():
    print(f"Welcome to the app, {user_name}.\nWe have 3 texts to be analyzed.")
    dashed_line()
else:
    print("Unregistered user, terminating the program...")
    exit()

# Volba textu určeného k analýze
user_number = input("Enter a number btw. 1 and 3 to select: ") # Pozor, input vždy vrací str!
dashed_line()
numbers = [1, 2, 3] # Správná čísla - pro indexaci nutno o jedno zmenšit!

if user_number.isdigit():
    user_number = int(user_number)
    if user_number not in numbers:
        print("The numeric value entered is not correct.")
        exit()
    else:
        print("The selected text will be processed.")
        dashed_line()
else:
    print("The entered value is not a numeric value.")
    exit()

# Načtení textu dle volby uživatele
text = task_template.TEXTS[user_number - 1]
words = text.split()
words = [word_w.rstrip(",.!?;#@_") for word_w in words]

# Analýza textu 
for word in words:
    if word.isupper() and not word.istitle():
        words_uppper += 1
    elif word.istitle():
        words_title += 1
    elif word.islower():
        words_lower += 1
    elif word.isdigit():
        words_num += 1
        numbers = int(word)
        sum_num += numbers

for word in words:
    word_len = len(word)
    words_dict[word_len] = words_dict.get(word_len, 0) + 1

# Výpis výsledků analýzy vybraného textu
print(f"There are {len(words)} words in the selected text.") 
print(f"There are {words_title} titlecase words.") 
print(f"There are {words_uppper} uppercase words.")
print(f"There are {words_lower} lowercase words.")
print(f"There are {words_num} numeric strings.")
print(f"The sum of all the numbers is {sum_num}.")
dashed_line()

col_width = max(words_dict.values()) + 1

print(f"LEN|{'OCCURRENCES'.center(col_width)}|NR.")
dashed_line()

for word_len, word_occur in sorted(words_dict.items()):
    word_occur_grapical = "*"*int(word_occur)
    print(f"{word_len:3}|{word_occur_grapical:<{col_width}}|{word_occur}")