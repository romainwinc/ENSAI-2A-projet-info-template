from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session


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
            message="Faites votre choix : ",
            choices=[
                "Se connecter",
                "Créer un compte",
                "Ré-initialiser la base de données",
                "Infos de session",
                "Quitter",
            ],
        ).execute()

        match choix:
            case "Quitter":
                pass

            case "Se connecter":
                from view.accueil.connexion_vue import ConnexionVue

                return ConnexionVue("Connexion à l'application")

            case "Créer un compte":
                from view.accueil.inscription_vue import InscriptionVue

                return InscriptionVue("Création de compte joueur")

            case "Infos de session":
                return AccueilVue(Session().afficher())

            # case "Ré-initialiser la base de données":
            #     succes = ResetDatabase().lancer()
            #     message = (
            #         f"Ré-initilisation de la base de données - {'SUCCES' if succes else 'ECHEC'}"
            #     )
            #     return AccueilVue(message)
