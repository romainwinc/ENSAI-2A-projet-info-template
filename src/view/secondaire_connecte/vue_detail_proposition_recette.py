from view.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from view.session import Session
from dao.recette_favorite_dao import RecetteFavoriteDAO
from dao.recette_dao import RecetteDAO
from service.service_recette import ServiceRecette
from service.service_avis import ServiceAvis
from dao.avis_dao import AvisDAO


class VueDetailPropositionRecette(VueAbstraite):
    """Vue pour afficher les détails des propositions de recette sans ingredients non
    désirés et avec au moins un ingredients favoris et qui n'est pas déjà une recette
    favorite de l'utilisateur."""

    def choisir_menu(self):
        """Implémentation requise de la méthode abstraite, sans effet ici."""
        pass

    def afficher_propositions(self):
        """Affiche les propositions de recette pour un utilisateur.

        Parameters
        ----------
        recettes : list
            Liste de recettes à afficher.
        """
        id_utilisateur = Session().utilisateur.id_utilisateur
        r = []
        r = ServiceRecette(RecetteDAO(), RecetteFavoriteDAO()).proposition_recette(
            id_user=id_utilisateur
        )
        return r
