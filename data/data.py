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


def main():
    if start_game():
        # Ajoute ici le code pour démarrer le jeu
        print("Le jeu commence...")
        # Exemple : initialiser les cartes, distribuer les mains, etc.
    else:
        print("Au revoir !")


if __name__ == "__main__":
    main()
