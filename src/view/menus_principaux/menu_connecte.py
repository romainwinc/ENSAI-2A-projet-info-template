from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite


class MenuUtilisateurConnecte(VueAbstraite):
    """Vue du menu d'un utilisateur connecté (qui n'a pas de rôle spécial
    comme administrateur ou profeissionnel)

    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'utilisateur
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Principal\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter mes recettes favorites",
                "Chercher une recette",
                "Consulter mes notes et avis",
                "Mes ingrédients favoris et non-désirés",
                "Proposer une recette",
                "Regarder ma liste de course",
                "Mon compte",
            ],
        ).execute()

        match choix:
            case "Consulter mes recettes favorites":
                from service.service_consultation import consulter_recette_favorite

                consulter_recette_favorite()
            case "Chercher une recette":
                from service.service_consultation import chercher_recette

                chercher_recette()
            case "Consulter mes notes et avis":
                from view.consulter_notes_avis import ConsulterNotesAvis

                return ConsulterNotesAvis()
            case "Mes ingrédients favoris et non-désirés":
                from view.ingredients_favoris_et_non_desires import IngredientsFavorisEtNonDesires

                return IngredientsFavorisEtNonDesires()
            case "Proposer une recette":
                from service.demande import proposer_recette

                proposer_recette()
            case "Regarder ma liste de course":
                from service.utilisateur import afficher_liste_de_course

                afficher_liste_de_course()
            case "Mon compte":
                from view.mon_compte_connecte import MonCompteConnecte

                return MonCompteConnecte()
