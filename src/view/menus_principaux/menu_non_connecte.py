from InquirerPy import inquirer


class MenuNonConnecte:
    """Vue du menu de l'utilisateur

    Permet à l'utilisateur de choisir entre se connecter, s'inscrire, ou rechercher une recette.
    """

    def choisir_menu(self):
        """Affiche le menu principal de l'utilisateur et gère ses choix

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nMenu Utilisateur\n" + "-" * 50 + "\n")

        # Afficher le menu et demander à l'utilisateur de faire un choix
        choix = inquirer.select(
            message="Que voulez-vous faire ?",
            choices=[
                "Se connecter",
                "S'inscrire",
                "Rechercher une recette",
                "Quitter",
            ],
        ).execute()

        # Gestion des choix de l'utilisateur avec 'match case'
        match choix:
            case "Se connecter":
                from view.login_vue import LoginVue

                return LoginVue()

            case "S'inscrire":
                from view.signup_vue import SignupVue

                return SignupVue()

            case "Rechercher une recette":
                from view.recherche_recette_vue import RechercheRecetteVue

                return RechercheRecetteVue()

            case "Quitter":
                print("Merci d'avoir utilisé l'application. À bientôt !")
                exit()
