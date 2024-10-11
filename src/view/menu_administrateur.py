from InquirerPy import inquirer


class MenuAdministrateurVue:
    """Vue du menu de l'administrateur

    Permet à l'administrateur de gérer ses recettes, avis, ingrédients, etc.
    """

    def choisir_menu(self):
        """Affiche le menu de l'administrateur et gère ses choix.

        Return
        ------
        vue
            Retourne la vue choisie par l'administrateur dans le terminal.
        """
        print("\n" + "-" * 50 + "\nMenu Administrateur\n" + "-" * 50 + "\n")

        # Affichage du menu et demande de choix à l'administrateur
        choix = inquirer.select(
            message="Que voulez-vous faire ?",
            choices=[
                "Consulter mes recettes favorites",
                "Consulter une recette",
                "Consulter mes notes/avis",
                "Consulter mes ingrédients favoris ou non désirés",
                "Proposer une recette",
                "Regarder la liste de course",
                "Consulter les demandes de suppression de recette",
                "Gestion de compte",
                "Quitter",
            ],
        ).execute()

        # Gestion des choix de l'administrateur avec 'match case'
        match choix:
            case "Consulter mes recettes favorites":
                from view.recettes_favorites_vue import RecettesFavoritesVue

                return RecettesFavoritesVue()

            case "Consulter une recette":
                from view.consulter_recette_vue import ConsulterRecetteVue

                return ConsulterRecetteVue()

            case "Consulter mes notes/avis":
                from view.notes_avis_vue import NotesAvisVue

                return NotesAvisVue()

            case "Consulter mes ingrédients favoris ou non désirés":
                from view.ingredients_vue import IngredientsVue

                return IngredientsVue()

            case "Proposer une recette":
                from view.proposer_recette_vue import ProposerRecetteVue

                return ProposerRecetteVue()

            case "Regarder la liste de course":
                from view.liste_course_vue import ListeCourseVue

                return ListeCourseVue()

            case "Consulter les demandes de suppression de recette":
                from view.demandes_suppression_vue import DemandesSuppressionVue

                return DemandesSuppressionVue()

            case "Gestion de compte":
                from view.gestion_compte_vue import GestionCompteVue

                return GestionCompteVue()

            case "Quitter":
                print("Merci d'avoir utilisé l'application. À bientôt !")
                exit()
