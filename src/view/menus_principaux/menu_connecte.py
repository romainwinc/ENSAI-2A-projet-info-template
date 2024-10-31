from InquirerPy import inquirer
from view.session import Session
from dao.ingredient_dao import IngredientDAO
from dao.ingredients_favoris_dao import IngredientsFavorisDAO
from dao.ingredients_non_desires_dao import IngredientsNonDesiresDAO
from dao.liste_de_courses_dao import ListeDeCoursesDAO
from service.service_ingredient import ServiceIngredient
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

        utilisateur_id = Session().utilisateur
        dao_ing = IngredientDAO()
        dao_ing_fav = IngredientsFavorisDAO()
        dao_ing_nd = IngredientsNonDesiresDAO()
        dao_liste_course = ListeDeCoursesDAO()
        ingredient_service = ServiceIngredient(dao_ing, dao_ing_fav, dao_ing_nd, dao_liste_course)

        match choix:
            case "Consulter mes recettes favorites":
                from view.secondaire_connecte.recettes_favorites import RecettesFavorites

                return RecettesFavorites()
                # recette_service.afficher_recettes_favorites(id_utilisateur)
                # return self
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
                ingredient_service.afficher_ingredients_liste_courses(utilisateur_id)

            case "Mon compte":
                from view.secondaire_connecte.mon_compte_connecte import MonCompteConnecte

                return MonCompteConnecte()

            case "Quitter":
                print("Retour au menu précédent.")
                return None
