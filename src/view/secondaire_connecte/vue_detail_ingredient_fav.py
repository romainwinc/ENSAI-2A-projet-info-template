from view.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from view.session import Session
from dao.ingredient_dao import IngredientDAO
from dao.ingredients_favoris_dao import IngredientsFavorisDAO
from dao.ingredients_non_desires_dao import IngredientsNonDesiresDAO
from dao.liste_de_courses_dao import ListeDeCoursesDAO
from service.service_ingredient import ServiceIngredient


class DetailIngredientFav(VueAbstraite):
    """Vue pour afficher les détails d'un ingredient favoris."""

    def choisir_menu(self):
        """Implémentation requise de la méthode abstraite, sans effet ici."""
        pass

    def afficher(self):
        """Affiche les détails de l'ingredient."""
        nom_ingredient = Session().ingredient

        utilisateur_id = Session().utilisateur.id_utilisateur
        ingredient_dao = IngredientDAO()
        favoris_dao = IngredientsFavorisDAO()
        non_desires_dao = IngredientsNonDesiresDAO()
        liste_courses_dao = ListeDeCoursesDAO()
        ingredient_service = ServiceIngredient(
            ingredient_dao, favoris_dao, non_desires_dao, liste_courses_dao
        )

        ingredient = ingredient_service.rechercher_par_nom_ingredient(nom_ingredient)[0]

        print("\n" + "-" * 50 + "\nDétails de l'ingrédient\n" + "-" * 50 + "\n")
        print(f"{ingredient}")

        from view.secondaire_connecte.ingredients_fav_et_nd import IngredientsFavEtND

        choix = inquirer.select(
            message="Que souhaitez-vous faire ?",
            choices=[
                "Retour au menu ingrédient",
                "Supprimer l'ingrédient de mes favoris",
            ],
        ).execute()

        match choix:
            case "Supprimer l'ingrédient de mes favoris":
                ingredient_service.supprimer_ingredients_favoris(
                    utilisateur_id, ingredient.nom_ingredient
                )
                inquirer.select(
                    message="",
                    choices=["OK"],
                ).execute()
                return self
            case "Retour au menu ingrédient":
                Session().fermer_ingredient()
                return IngredientsFavEtND()
