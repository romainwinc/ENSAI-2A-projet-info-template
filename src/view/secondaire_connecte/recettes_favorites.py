from view.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from dao.recette_favorite_dao import RecetteFavoriteDAO
from dao.recette_dao import RecetteDAO
from service.service_recette import ServiceRecette
from view.session import Session
from view.menus_principaux.menu_connecte import MenuUtilisateurConnecte


class RecettesFavorites(VueAbstraite):
    """Vue pour afficher les recettes favorites d'un utilisateur."""

    def choisir_menu(self):
        """Implémentation requise de la méthode abstraite."""
        return self.afficher()

    def afficher(self):
        """Affiche les recettes favorites et permet à l'utilisateur de sélectionner une recette."""
        id_utilisateur = Session().utilisateur.id_utilisateur
        dao_recette = RecetteDAO()
        dao_recette_fav = RecetteFavoriteDAO()
        service_recette = ServiceRecette(dao_recette, dao_recette_fav)

        favoris = service_recette.afficher_recettes_favorites(id_utilisateur)

        # Vérifiez si l'utilisateur a des recettes favorites
        if not favoris:
            print("Pas de favoris")
            return MenuUtilisateurConnecte()

        # Afficher les recettes favorites
        choix_menu = favoris + ["Retour au menu principal"]
        choix = inquirer.select(
            message="Sélectionnez une recette pour plus de détails ou retournez au menu :",
            choices=choix_menu,
        ).execute()

        if choix in favoris:
            # Afficher les détails de la recette sélectionnée
            recette_selectionnee = choix
            Session().ouvrir_recette(recette_selectionnee)
            from view.secondaire_connecte.vue_detail_recette_fav import DetailRecetteFav

            return DetailRecetteFav().afficher()
        else:
            # Retourner au menu précédent
            return MenuUtilisateurConnecte("Redirection vers le menu")
