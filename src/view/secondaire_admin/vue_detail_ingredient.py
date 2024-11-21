from view.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from view.session import Session
from dao.ingredient_dao import IngredientDAO
from dao.ingredients_favoris_dao import IngredientsFavorisDAO
from dao.ingredients_non_desires_dao import IngredientsNonDesiresDAO
from dao.liste_de_courses_dao import ListeDeCoursesDAO
from service.service_ingredient import ServiceIngredient


class VueDetailIngredient(VueAbstraite):
    """Vue pour afficher les détails d'un ingrédient."""

    def choisir_menu(self):
        """Implémentation requise de la méthode abstraite, sans effet ici."""
        pass

    def afficher(self):
        """Affiche les détails de l'ingrédient."""
        ingredient = Session().ingredient
        print("\n" + "-" * 50 + "\nDétails de l'ingrédient'\n" + "-" * 50 + "\n")
        print(f"{ingredient}")

        # Permet de revenir au menu principal ou à la recherche
        from view.secondaire_admin.recherche_ingredient import RechercheIngredientAdmin

        choix = inquirer.select(
            message="Que souhaitez-vous faire ensuite ?",
            choices=[
                "Ajouter l'ingrédient à mes favoris",
                "Ajouter l'ingrédient à mes non-désirés",
                "Ajouter l'ingrédient à ma liste de course",
                "Retour à la recherche",
            ],
            max_height=10,
        ).execute()

        utilisateur_id = Session().utilisateur.id_utilisateur
        ingredient_dao = IngredientDAO()
        favoris_dao = IngredientsFavorisDAO()
        non_desires_dao = IngredientsNonDesiresDAO()
        liste_courses_dao = ListeDeCoursesDAO()
        ingredient_service = ServiceIngredient(
            ingredient_dao, favoris_dao, non_desires_dao, liste_courses_dao
        )

        match choix:
            case "Ajouter l'ingrédient à mes favoris":
                if ingredient_service.ajouter_ingredients_favoris(
                    utilisateur_id, ingredient.nom_ingredient
                ):
                    print("L'ingrédient a bien été ajoutée à vos favoris.")
                else:
                    inquirer.select(
                        message="",
                        choices=["Suivant"],
                    ).execute()
                return self
            case "Ajouter l'ingrédient à mes non-désirés":
                if ingredient_service.ajouter_ingredients_non_desires(
                    utilisateur_id, ingredient.nom_ingredient
                ):
                    print("L'ingrédient a bien été ajoutée à vos non-désirés.")
                else:
                    inquirer.select(
                        message="",
                        choices=["Suivant"],
                    ).execute()
                return self

            case "Ajouter l'ingrédient à ma liste de course":
                if ingredient_service.ajouter_ingredients_liste_courses(
                    utilisateur_id, ingredient.nom_ingredient
                ):
                    print("L'ingrédient a bien été ajoutée à votre liste de course.")
                else:
                    inquirer.select(
                        message="",
                        choices=["Suivant"],
                    ).execute()
                return self

            case "Retour à la recherche":
                Session().fermer_ingredient()
                return RechercheIngredientAdmin()
