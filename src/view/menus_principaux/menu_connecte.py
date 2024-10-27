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
                "Ma liste de course",
                "Mon compte",
                "Quitter",
            ],
            max_height=15,
        ).execute()

        match choix:
            case "Consulter mes recettes favorites":
                from service.secondaire_connecte.service_consultation import (
                    consulter_recette_favorite,
                )

                consulter_recette_favorite()
            case "Chercher une recette":
                from view.secondaire_connecte.recherche_recette import RechercheRecetteConnecte

                return RechercheRecetteConnecte()
            case "Consulter mes notes et avis":
                from view.secondaire_connecte.consulter_notes_avis import ConsulterNotesAvis

                return ConsulterNotesAvis()
            case "Mes ingrédients favoris et non-désirés":
                from view.secondaire_connecte.ingredients_favoris_et_non_desires import (
                    IngredientsFavorisEtNonDesires,
                )

                return IngredientsFavorisEtNonDesires()
            case "Proposer une recette":
                from service.demande import proposer_recette

                proposer_recette()

            case "Ma liste de course":
                from view.session import Session
                from dao.ingredient_dao import IngredientDAO
                from service.service_ingredient import IngredientService

                utilisateur_id = Session().utilisateur
                dao = IngredientDAO()
                ingredient_service = IngredientService(dao)
                ingredient_service.afficher_ingredients_liste_courses(utilisateur_id)

            case "Mon compte":
                from view.secondaire_connecte.mon_compte_connecte import MonCompteConnecte

                return MonCompteConnecte()

            case "Quitter":
                print("Retour au menu précédent.")
                return None
