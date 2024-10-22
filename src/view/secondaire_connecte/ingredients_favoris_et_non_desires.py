from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session
from dao.ingredient_dao import IngredientDAO
from service.service_ingredient import IngredientService


class IngredientsFavorisEtNonDesires(VueAbstraite):
    """Vue du menu des ingrédient favoris et des ingrédients non-désirés pour
    un utilisateur connecté

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

        print("\n" + "-" * 50 + "\nMes ingredients favoris et non-désires\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter mes ingrédients favoris",
                "Consulter mes ingrédients non-désirés",
                "Supprimer des ingrédients favoris",
                "Supprimer des ingrédients non-désirés",
                "Ajouter des ingrédients favoris",
                "Ajouter des ingrédients non-désirés",
            ],
        ).execute()

        utilisateur_id = Session().utilisateur
        dao = IngredientDAO()
        ingredient_service = IngredientService(dao)

        match choix:
            case "Consulter mes ingrédients favoris":
                ingredient_service.recuperer_ingredients_favoris_utilisateur(utilisateur_id)

            case "Consulter mes ingrédients non-désirés":
                ingredient_service.recuperer_ingredients_non_desires_utilisateur(utilisateur_id)

            case "Supprimer des ingrédients favoris":
                ingredient_id = inquirer.text(
                    message="Entrez l'ID de l'ingrédient favori à supprimer :"
                ).execute()
                ingredient_service.supprimer_ingredient_favori(utilisateur_id, ingredient_id)

            case "Supprimer des ingrédients non-désirés":
                ingredient_id = inquirer.text(
                    message="Entrez l'ID de l'ingrédient non-désiré à supprimer :"
                ).execute()
                ingredient_service.supprimer_ingredient_non_desire(utilisateur_id, ingredient_id)

            case "Ajouter des ingrédients favoris":
                ingredient_id = inquirer.text(
                    message="Entrez l'ID de l'ingrédient favori à ajouter :"
                ).execute()
                ingredient_service.ajouter_ingredient_favori(utilisateur_id, ingredient_id)

            case "Ajouter des ingrédients non-désirés":
                ingredient_id = inquirer.text(
                    message="Entrez l'ID de l'ingrédient non-désiré à ajouter :"
                ).execute()
                ingredient_service.ajouter_ingredient_non_desire(utilisateur_id, ingredient_id)
