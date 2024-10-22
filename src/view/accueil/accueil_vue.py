from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite


class AccueilVue(VueAbstraite):
    """Vue d'accueil de l'application"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nAccueil\n" + "-" * 50 + "\n")

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
                from view.accueil.connexion_vue import ConnexionVue

                return ConnexionVue()

            case "S'inscrire":
                from view.accueil.inscription_vue import InscriptionVue

                return InscriptionVue()

            case "Rechercher une recette":
                from view.secondaire_non_connecte.recherche_recette_vue import RechercheRecetteVue

                return RechercheRecetteVue()

            case "Quitter":
                print("Merci d'avoir utilisé Recipe-Makers. À bientôt !")
                exit()

        # match choix:
        #     case "Quitter":
        #         pass

        #     case "Se connecter":
        #         from view.accueil.connexion_vue import ConnexionVue

        #         return ConnexionVue("Connexion à l'application")

        #     case "Créer un compte":
        #         from view.accueil.inscription_vue import InscriptionVue

        #         return InscriptionVue("Création de compte joueur")

        #     case "Infos de session":
        #         return AccueilVue(Session().afficher())
