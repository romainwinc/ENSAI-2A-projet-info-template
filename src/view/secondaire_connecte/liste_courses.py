from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session
from dao.ingredient_dao import IngredientDAO
from service.service_ingredient import IngredientService


class ListeCourses(VueAbstraite):
    """Vue pour afficher et modifier les ingrédients de la liste de courses
    d'un utilisateur

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

        print("\n" + "-" * 50 + "\nMa liste de courses\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter ma liste de courses",
                "Supprimer des ingrédients de ma liste de courses",
                "Ajouter des ingrédients à ma liste de courses",
            ],
        ).execute()

        utilisateur_id = Session().utilisateur
        dao = IngredientDAO()
        ingredient_service = IngredientService(dao)

        match choix:
            case "Consulter ma liste de courses":
                ingredient_service.afficher_ingredients_liste_courses(utilisateur_id)

            case "Supprimer des ingrédients de ma liste de courses":
                ingredient_id = inquirer.text(
                    message="Entrez l'ID de l'ingrédient à supprimer de la liste de courses:"
                ).execute()
                ingredient_service.supprimer_ingredient_liste_courses(utilisateur_id, ingredient_id)

            case "Ajouter des ingrédients à ma liste de courses":
                ingredient_id = inquirer.text(
                    message="Entrez l'ID de l'ingrédient favori à ajouter à la liste de courses:"
                ).execute()
                ingredient_service.ajouter_ingredient_liste_courses(utilisateur_id, ingredient_id)
