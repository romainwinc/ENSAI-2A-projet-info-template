from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from dao.ingredient_dao import IngredientDAO
from dao.ingredients_favoris_dao import IngredientsFavorisDAO
from dao.ingredients_non_desires_dao import IngredientsNonDesiresDAO
from dao.liste_de_courses_dao import ListeDeCoursesDAO
from service.service_ingredient import ServiceIngredient
from view.session import Session


class RechercheIngredientPro(VueAbstraite):
    """Vue pour rechercher un ingrédient.

    Permet au professionnel de rechercher un ingrédient.
    """

    def choisir_menu(self):
        """Affiche le menu pour rechercher un ingrédient.

        Return
        ------
        vue
            Retourne la vue suivante en fonction de la recherche du professionnel.
        """
        print("\n" + "-" * 50 + "\nRecherche d'ingrédient\n" + "-" * 50 + "\n")

        # Choix du type de recherche (par nom ou par ingrédient)
        type_recherche = inquirer.select(
            message="Choisissez le type de recherche :",
            choices=[
                "Recherche par nom de l'ingrédient",
                "Retour au menu Ingrédient",
            ],
        ).execute()

        match type_recherche:
            case "Recherche par nom de l'ingrédient":
                self.rechercher_ingredient()
                return self
            case "Retour au menu Ingrédient":
                from view.secondaire_pro.ingredients_fav_et_nd import IngredientsFavEtND

                return IngredientsFavEtND()

    def rechercher_ingredient(self):
        """Recherche un ingrédient par nom."""
        nom_ingredient = inquirer.text(message="Entrez le nom de l'ingredient :").execute()
        ingredient_dao = IngredientDAO()
        favoris_dao = IngredientsFavorisDAO()
        non_desires_dao = IngredientsNonDesiresDAO()
        liste_courses_dao = ListeDeCoursesDAO()
        ingredients = ServiceIngredient(
            ingredient_dao, favoris_dao, non_desires_dao, liste_courses_dao
        ).rechercher_par_nom_ingredient(nom_ingredient)

        i = []  # Liste pour stocker les noms des ingredients trouvées

        if ingredients:
            for ingredient in ingredients:
                i.append(ingredient.nom_ingredient)
        else:
            print("Aucun ingredient trouvé.")

        # Afficher le menu avec les noms des ingrédientd trouvées ou une option de retour
        choix_menu = i + ["Retour au menu ingrédient"]
        choix = inquirer.select(
            message="Sélectionnez un ingrédient pour plus de détails ou retournez au menu :",
            choices=choix_menu,
        ).execute()

        if choix in i:
            # Trouver l'ingrédient correspondante
            ingredient_selectionne = next(
                (ingredient for ingredient in ingredients if ingredient.nom_ingredient == choix),
                None,
            )
            if ingredient_selectionne:
                Session().ouvrir_ingredient(ingredient_selectionne)
                from view.secondaire_pro.vue_detail_ingredient import (
                    VueDetailIngredient,
                )

                return VueDetailIngredient(ingredient_selectionne).afficher()
        else:
            # Retourner à la vue de recherche
            return self
