def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : Division par zéro"

def calculatrice():
    print("\nBienvenue dans la calculatrice !")
    print("Choisissez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choix = int(input("Entrez le numéro de l'opération (1/2/3/4) : "))
        if choix not in [1, 2, 3, 4]:
            print("Erreur : Choix invalide.")
            return

        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))

        if choix == 1:
            print(f"Résultat : {addition(a, b)}")
        elif choix == 2:
            print(f"Résultat : {soustraction(a, b)}")
        elif choix == 3:
            print(f"Résultat : {multiplication(a, b)}")
        elif choix == 4:
            print(f"Résultat : {division(a, b)}")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    while True:
        calculatrice()
        continuer = input("Voulez-vous effectuer un autre calcul ? (oui/non) : ").lower()
        if continuer != "oui":
            print("Merci d'avoir utilisé la calculatrice. Au revoir !")
            break
