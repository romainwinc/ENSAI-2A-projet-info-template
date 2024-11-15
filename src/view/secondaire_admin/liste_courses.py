from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session
from dao.ingredient_dao import IngredientDAO
from dao.ingredients_favoris_dao import IngredientsFavorisDAO
from dao.ingredients_non_desires_dao import IngredientsNonDesiresDAO
from dao.liste_de_courses_dao import ListeDeCoursesDAO
from service.service_ingredient import ServiceIngredient


class ListeCourses(VueAbstraite):
    """Vue pour afficher et modifier les ingrédients de la liste de courses
    d'un administrateur

    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'administrateur
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'administrateur

        Return
        ------
        vue
            Retourne la vue choisie par l'administrateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMa liste de courses\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter ma liste de courses",
                "Ajouter des ingrédients à ma liste de courses",
                "Retour au menu principal",
            ],
        ).execute()

        match choix:
            case "Consulter ma liste de courses":
                self.afficher_liste_courses()
                return self

            case "Ajouter des ingrédients à ma liste de courses":
                from view.secondaire_admin.ajout_ingredient_liste_courses import (
                    AjoutIngredientListeCousrses,
                )

                return AjoutIngredientListeCousrses()
            case "Retour au menu principal":
                from view.menus_principaux.menu_administrateur import MenuAdministrateur

                return MenuAdministrateur()

    def afficher_liste_courses(self):
        """Affiche les ingrédients de la liste de course."""
        id_utilisateur = Session().utilisateur.id_utilisateur
        ingredient_dao = IngredientDAO()
        favoris_dao = IngredientsFavorisDAO()
        non_desires_dao = IngredientsNonDesiresDAO()
        liste_courses_dao = ListeDeCoursesDAO()
        service_ingredient = ServiceIngredient(
            ingredient_dao, favoris_dao, non_desires_dao, liste_courses_dao
        )

        liste = service_ingredient.afficher_ingredients_liste_courses(id_utilisateur)

        # Vérifiez si l'utilisateur a des ingrédients dans sa liste de course
        if not liste:
            inquirer.select(
                message="",
                choices=["OK"],
            ).execute()
            return self

        # Afficher les ingredients de la liste de course
        choix_menu = liste + ["Retour au menu principal"]
        choix = inquirer.select(
            message=(
                "Sélectionnez un ingrédient pour plus de détails ou le "
                "supprimer de la liste de courses :"
            ),
            choices=choix_menu,
        ).execute()

        if choix in liste:
            # Afficher les détails de l'ingrédient sélectionné
            ingredient_selectionne = choix
            Session().ouvrir_ingredient(ingredient_selectionne)
            from view.secondaire_admin.vue_detail_ingredient_liste_courses import (
                DetailIngredientListeCourses,
            )

            return DetailIngredientListeCourses().afficher()
        else:
            # Retourner au menu précédent
            return self
