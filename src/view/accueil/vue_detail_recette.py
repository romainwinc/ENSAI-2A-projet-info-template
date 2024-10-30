from view.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from models.recette import Recette


class VueDetailRecette(VueAbstraite):
    """Vue pour afficher les détails d'une recette."""

    def __init__(self, recette: Recette):
        """Initialise la vue avec la recette sélectionnée.

        Parameters
        ----------
        recette : Recette
            La recette dont on veut afficher les détails.
        """
        self.recette = recette

    def choisir_menu(self):
        """Implémentation requise de la méthode abstraite, sans effet ici."""
        pass

    def afficher(self):
        """Affiche les détails de la recette."""
        print("\n" + "-" * 50 + "\nDétails de la Recette\n" + "-" * 50 + "\n")
        print(f"{self.recette}")

        # Permet de revenir au menu principal ou à la recherche
        from view.accueil.rechercher_recette_non_connecte import RechercheRecetteNonConnecte

        inquirer.select(
            message="Que souhaitez-vous faire ensuite ?",
            choices=[
                "Retour à la recherche",
            ],
        ).execute()

        return RechercheRecetteNonConnecte()  # Retour à la vue de recherche
