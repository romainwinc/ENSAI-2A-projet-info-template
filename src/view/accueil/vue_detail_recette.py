from view.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from models.recette import Recette
from view.session import Session
from dao.avis_dao import AvisDAO
from service.service_avis import ServiceAvis


class VueDetailRecette(VueAbstraite):
    """Vue pour afficher les détails d'une recette pour un utilisateur non-connecté."""

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

        choix = inquirer.select(
            message="Que souhaitez-vous faire ensuite ?",
            choices=[
                "Voir les avis de la recette",
                "Retour à la recherche",
            ],
            max_height=10,
        ).execute()

        match choix:
            case "Voir les avis de la recette":
                recette_id = Session().recette.id_recette
                dao = AvisDAO()
                avis_service = ServiceAvis(dao)
                avis_service.afficher_avis_par_recette(recette_id)
                inquirer.select(
                    message="",
                    choices=["Retour"],
                ).execute()
                return self
            case "Retour à la recherche":
                Session().fermer_recette()
                return RechercheRecetteNonConnecte()  # Retour à la vue de recherche
