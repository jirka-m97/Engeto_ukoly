# Hlavička projektu
"""
Mach_projekt_2_BullsCows_final.py: druhý projekt do Engeto Online Python Akademie

author: Jiří Mach
email: machi@vscht.cz
"""

# Import knihoven (není nutné dodávat soubor requirements.txt, jedná se o builtin knihovny)
import time
import random

# Definice funkcí
def dashed_line(dashed_line_len: int) -> str:
    """
    Funkce vytváří, a zároveň vypisuje čárkovanou dělící čáru o zadané délce.
    """
    print("-" * dashed_line_len) # zde používám "print()" namísto return, abych nemusel při volání používat print()

def number_validation(guess_num: str, length: int=4) -> bool:
    """
    Funkce ověřuje, zda je zadané číslo validní, tedy:
    je dlouhé právě 4 znaky, neobsahuje duplicity, nezačíná nulou a neobsahuje písmeno či speciální znak.
    """
    if len(guess_num) != length:
        print("Your number has less or more than 4 digits.")
        return False  
    if len(guess_num) != len(set(guess_num)):
        print("Your number contains duplicities.")
        return False  
    if guess_num.startswith("0"):
        print("Your number starts with '0'.")
        return False  
    if not guess_num.isdigit():
        print("Your number contains non-numeric characters.")
        return False  
    return True

def generate_secret_number(length: int=4) -> str:
    """
    Funkce generuje náhodné čtyřmístné tajné číslo s unikátními číslicemi (0-9), které je uživatelem hádáno.
    """
    rand_num = set()

    while len(rand_num) < length: 
        num = random.randint(0, 9)
        rand_num.add(num)

    secret_number = list(rand_num)

    # Kontrola, zda první číslice není nula, pokud je, náhrada za jinou unikátní číslici
    if secret_number[0] == 0:
        # print("nula na počátku") # pouze pro ověření funčnosti kontroly!
        available_unique_digits = set(range(1, 10)) - rand_num
        replacement = random.choice(list(available_unique_digits))
        secret_number[0] = replacement  
        rand_num.add(replacement)  
        rand_num.remove(0)  
    return "".join(map(str, rand_num))

def main():
    # Nastavení proměnných
    dashed_line_len = 47
    bulls = 0
    counter = 0

    # Úvodní text
    print(5 * "#", " BULLS & COWS GAME ", 5 * "#")
    dashed_line(dashed_line_len)
    print("Hi there!")
    dashed_line(dashed_line_len)
    print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
    dashed_line(dashed_line_len)

    # Generování tajného čísla s unikátními číslicemi
    start = time.time()
    secret_number = generate_secret_number()
    # print(f"Secret number: {secret_number}") # pouze pro kontrolu
    # dashed_line(dashed_line_len)

    while bulls < 4:
        bulls = 0
        cows = 0

        # Vstupy od uživatele
        guess_num = input("Enter a number: ") # POZOR, input je v podobě STR!!!
        dashed_line(dashed_line_len)

        # Kontrola správné podoby čísla
        if not number_validation(guess_num):
            print("The input number is invalid. Exiting...")
            break
        else:
            print("The input number is valid.")

        for number in guess_num:
            if number in secret_number:
                if secret_number.index(number) == guess_num.index(number):
                    bulls += 1
                elif secret_number.index(number) != guess_num.index(number):
                    cows += 1

        if bulls == 1 and cows == 1:
            print(f"{bulls} bull, {cows} cow")
        elif bulls == 1 and cows > 1: 
            print(f"{bulls} bull, {cows} cows")
        elif bulls > 1 and cows == 1:
            print(f"{bulls} bulls, {cows} cow")
        else:
            print(f"{bulls} bulls, {cows} cows") 

        counter += 1
        dashed_line(dashed_line_len)

    else:
        print(f"Correct, you've guessed the right number in {counter} guesses!")
        dashed_line(dashed_line_len)
        print("That's amazing!")

    end = time.time()
    game_duration = round(end - start, 2)
    print(f"The game lasted: {game_duration} s.")

if __name__ == "__main__":
    main()
