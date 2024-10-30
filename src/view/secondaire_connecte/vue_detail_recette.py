from view.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from models.recette import Recette
from view.session import Session
from dao.recette_favorite_dao import RecetteFavoriteDAO
from dao.recette_dao import RecetteDAO
from service.service_recette import ServiceRecette


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
        from view.secondaire_connecte.recherche_recette import RechercheRecetteConnecte

        choix = inquirer.select(
            message="Que souhaitez-vous faire ensuite ?",
            choices=[
                "Ajouter la recette à mes favoris",
                "Ajouter un avis",
                "Retour à la recherche",
            ],
        ).execute()

        utilisateur_id = Session().utilisateur
        recette_fav_dao = RecetteFavoriteDAO()
        recette_dao = RecetteDAO()
        recette_service = ServiceRecette(recette_dao, recette_fav_dao)

        match choix:
            case "Ajouter la recette à mes favoris":
                recette_service.ajouter_recette_favorite(self.recette.nom_recette, utilisateur_id)
                print("La recette a bien été ajoutée à vos favoris.")
                return self
            case "Ajouter un avis":
                pass
            case "Retour à la recherche":
                return RechercheRecetteConnecte()
