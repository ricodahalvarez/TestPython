import random

def jouer():
    nombre_mystere = random.randint(1, 100)
    essais_restants = 5
    print("J'ai choisi un nombre entre 1 et 100. Pouvez-vous le deviner ? Vous avez 5 essais.")

    while essais_restants > 0:
        essai = input("Entrez votre essai : ")
        
        # Vérification si l'entrée est un nombre
        if essai.isdigit():
            essai = int(essai)
        else:
            print("Veuillez entrer un nombre valide.")
            continue
        
        if essai == nombre_mystere:
            print(f"Bravo ! Vous avez trouvé le nombre mystère : {nombre_mystere}.")
            break
        elif essai < nombre_mystere:
            print("Trop petit !")
        else:
            print("Trop grand !")
        
        essais_restants -= 1
        print(f"Il vous reste {essais_restants} essai(s).")

    if essais_restants == 0:
        print(f"Dommage ! Le nombre mystère était {nombre_mystere}.")
        
if __name__ == "__main__":
    jouer()
