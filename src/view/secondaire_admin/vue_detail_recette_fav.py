from view.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from view.session import Session
from dao.recette_favorite_dao import RecetteFavoriteDAO
from dao.recette_dao import RecetteDAO
from service.service_recette import ServiceRecette


class DetailRecetteFav(VueAbstraite):
    """Vue pour afficher les détails d'une recette favorite."""

    def choisir_menu(self):
        """Implémentation requise de la méthode abstraite, sans effet ici."""
        pass

    def afficher(self):
        """Affiche les détails de la recette."""
        nom_recette = Session().recette
        utilisateur_id = Session().utilisateur.id_utilisateur
        recette_fav_dao = RecetteFavoriteDAO()
        recette_dao = RecetteDAO()
        recette_service = ServiceRecette(recette_dao, recette_fav_dao)

        recette = recette_service.rechercher_par_nom_recette(nom_recette)[0]

        print("\n" + "-" * 50 + "\nDétails de la Recette\n" + "-" * 50 + "\n")
        print(recette_service.afficher_recette(recette.id_recette))

        from view.menus_principaux.menu_administrateur import MenuAdministrateur

        choix = inquirer.select(
            message="Que souhaitez-vous faire ?",
            choices=[
                "Retour au menu principal",
                "Supprimer la recette de mes favoris",
            ],
            max_height=10,
        ).execute()

        match choix:
            case "Supprimer la recette de mes favoris":
                recette_service.supprimer_recette_favorite(recette.nom_recette, utilisateur_id)
                print("La recette a bien été retirée de vos favoris.")
                return self
            case "Retour au menu principal":
                Session().fermer_recette()
                return MenuAdministrateur()
