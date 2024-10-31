from view.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from view.session import Session
from dao.recette_favorite_dao import RecetteFavoriteDAO
from dao.recette_dao import RecetteDAO
from service.service_recette import ServiceRecette


class VueDetailRecette(VueAbstraite):
    """Vue pour afficher les détails d'une recette."""

    def choisir_menu(self):
        """Implémentation requise de la méthode abstraite, sans effet ici."""
        pass

    def afficher(self):
        """Affiche les détails de la recette."""
        recette = Session().recette
        print("\n" + "-" * 50 + "\nDétails de la Recette\n" + "-" * 50 + "\n")
        print(f"{recette}")

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

        utilisateur_id = Session().utilisateur.id_utilisateur
        recette_fav_dao = RecetteFavoriteDAO()
        recette_dao = RecetteDAO()
        recette_service = ServiceRecette(recette_dao, recette_fav_dao)

        match choix:
            case "Ajouter la recette à mes favoris":
                recette_service.ajouter_recette_favorite(recette.nom_recette, utilisateur_id)
                print("La recette a bien été ajoutée à vos favoris.")
                return self
            case "Ajouter un avis":
                from view.secondaire_connecte.vue_ajouter_avis import VueAjouterAvis

                vue_avis = VueAjouterAvis()
                vue_avis.afficher()
                return vue_avis
            case "Retour à la recherche":
                Session().fermer_recette()
                return RechercheRecetteConnecte()
