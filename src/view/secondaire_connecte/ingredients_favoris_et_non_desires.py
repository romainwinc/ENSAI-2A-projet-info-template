from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session


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
            choices=["Consulter mes ingrédients favoris", "Consulter mes ingrédients non-désirés"],
        ).execute()

        match choix:
            case "Consulter mes ingrédients favoris":
                consulter_ingrédients_favoris()

            case "Consulter mes ingrédients non-désirés":
                consulter_ingrédients_non_desires()
