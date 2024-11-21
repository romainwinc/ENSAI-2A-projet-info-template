from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from dao.ingredient_dao import IngredientDAO
from dao.ingredients_favoris_dao import IngredientsFavorisDAO
from dao.ingredients_non_desires_dao import IngredientsNonDesiresDAO
from dao.liste_de_courses_dao import ListeDeCoursesDAO
from service.service_ingredient import ServiceIngredient
from view.session import Session


class AjoutIngredientListeCousrses(VueAbstraite):
    """Vue pour ajouter un ingrédient à sa liste de courses.

    Permet à l'administrateur de rechercher un ingrédient.
    """

    def choisir_menu(self):
        """Affiche le menu pour rechercher un ingrédient à ajouter à sa liste de courses."""
        print("\n" + "-" * 50 + "\nRecherche d'ingrédient\n" + "-" * 50 + "\n")

        # Choix du type de recherche (par nom ou par ingrédient)
        type_recherche = inquirer.select(
            message="Choisissez le type de recherche :",
            choices=[
                "Recherche par nom de l'ingrédient",
                "Retour au menu à la liste de course",
            ],
            max_height=10,
        ).execute()

        match type_recherche:
            case "Recherche par nom de l'ingrédient":
                self.rechercher_ingredient()
                return self
            case "Retour au menu à la liste de course":
                from view.secondaire_admin.liste_courses import ListeCourses

                return ListeCourses()

    def rechercher_ingredient(self):
        """Recherche un ingrédient par nom."""
        nom_ingredient = inquirer.text(message="Entrez le nom de l'ingredient :").execute()
        ingredient_dao = IngredientDAO()
        favoris_dao = IngredientsFavorisDAO()
        non_desires_dao = IngredientsNonDesiresDAO()
        liste_courses_dao = ListeDeCoursesDAO()
        ingredient_service = ServiceIngredient(
            ingredient_dao, favoris_dao, non_desires_dao, liste_courses_dao
        )
        ingredients = ingredient_service.rechercher_par_nom_ingredient(nom_ingredient)
        utilisateur_id = Session().utilisateur.id_utilisateur

        i = []  # Liste pour stocker les noms des ingredients trouvées

        if ingredients:
            for ingredient in ingredients:
                i.append(ingredient.nom_ingredient)
        else:
            print("Aucun ingredient trouvé.")

        # Afficher le menu avec les noms des ingrédientd trouvées ou une option de retour
        choix_menu = i + ["Retour au menu ingrédient"]
        choix = inquirer.select(
            message="Sélectionnez un ingrédient pour l'ajouter à la liste de course :",
            choices=choix_menu,
        ).execute()

        if choix in i:
            # Trouver l'ingrédient correspondante
            ingredient_selectionne = next(
                (ingredient for ingredient in ingredients if ingredient.nom_ingredient == choix),
                None,
            )
            if ingredient_selectionne:
                if ingredient_service.ajouter_ingredients_liste_courses(
                    utilisateur_id, ingredient_selectionne.nom_ingredient
                ):
                    print("L'ingrédient a bien été ajoutée à votre liste de course.")
                else:
                    inquirer.select(
                        message="",
                        choices=["Suivant"],
                    ).execute()
                return self
        else:
            # Retourner à la vue de recherche
            return self
