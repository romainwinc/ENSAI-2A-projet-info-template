from InquirerPy import inquirer


from view.vue_abstraite import VueAbstraite


class MenuProfessionnelVue(VueAbstraite):
    """Vue d'accueil pour un professionnel"""

    def choisir_menu(self):
        """Choix du menu suivant pour un professionnel

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Professionnel\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter mes recettes favorites",
                "Chercher une recette",
                "Consulter mes notes et avis",
                "Mes ingrédients favoris et non-désirés",
                "Soumettre une recette",
                "Afficher ma liste de course",
                "Demander la suppression d'une recette",
                "Mon compte",
                "Quitter",
            ],
        ).execute()

        match choix:
            case "Consulter mes recettes favorites":
                pass

            case "Chercher une recette":
                from view.secondaire_pro.consulter_recette import ConsulterRecette

                return ConsulterRecette()

            case "Consulter mes notes et avis":
                pass

            case "Mes ingrédients favoris et non-désirés":
                pass

            case "Soumettre une recette":
                pass

            case "Afficher ma liste de course":
                pass

            case "Demander la suppression d'une recette":
                pass

            case "Mon compte":
                from view.secondaire_pro import MonComptePro

                return MonComptePro()

            case "Quitter":
                print("Merci d'avoir utilisé Recipe-Makers. À bientôt !")
                exit()
