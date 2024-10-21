from InquirerPy import inquirer

from utils.reset_database import ResetDatabase

from view.vue_abstraite import VueAbstraite
from view.session import Session


class MenuProfessionnelVue(VueAbstraite):
    """Vue d'accueil pour un professionnel"""

    def choisir_menu(self):
        """Choix du menu suivant pour un professionnel

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Professionnel\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter ses recettes favorites",
                "Consulter une recette",
                "Consulter ses notes ou ses avis",
                "Consulter ses ingrédients favoris ou ingrédients non désirés",
                "Proposer une recette",
                "Regarder la liste de courses",
                "Demander la suppression d'une recette",
                "Supprimer le compte",
                "Ré-initialiser la base de données",
                "Infos de session",
                "Quitter",
            ],
        ).execute()

        match choix:
            case "Quitter":
                pass

            case "Consulter ses recettes favorites":
                from view.professionnel.recettes_favorites_vue import RecettesFavoritesVue

                return RecettesFavoritesVue()

            case "Consulter une recette":
                from view.professionnel.consulter_recette_vue import ConsulterRecetteVue

                return ConsulterRecetteVue()

            case "Consulter ses notes ou ses avis":
                from view.professionnel.notes_avis_vue import NotesAvisVue

                return NotesAvisVue()

            case "Consulter ses ingrédients favoris ou ingrédients non désirés":
                from view.professionnel.ingredients_vue import IngredientsVue

                return IngredientsVue()

            case "Proposer une recette":
                from view.professionnel.proposer_recette_vue import ProposerRecetteVue

                return ProposerRecetteVue()

            case "Regarder la liste de course":
                from view.professionnel.liste_course_vue import ListeCourseVue

                return ListeCourseVue()

            case "Demander la suppression d'une recette":
                from view.professionnel.suppression_recette_vue import SuppressionRecetteVue

                return SuppressionRecetteVue()

            case "Supprimer le compte":
                from view.professionnel.supprimer_compte_vue import SupprimerCompteVue

                return SupprimerCompteVue()
