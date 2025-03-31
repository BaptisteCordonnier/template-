def start_game():
    while True:
        commence = (
            input(
                "Voulez-vous commencer une nouvelle partie de Blackjack ? (oui/non) : "
            )
            .strip()
            .lower()
        )
        if commence == "oui":
            print("Super ! La partie va commencer.")
            return True
        elif commence == "non":
            print("D'accord, peut-être une autre fois !")
            return False
        else:
            print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")
