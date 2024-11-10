from InquirerPy import inquirer
from view.session import Session
from dao.recette_dao import RecetteDAO
from dao.recette_favorite_dao import RecetteFavoriteDAO
from service.service_recette import ServiceRecette
from view.vue_abstraite import VueAbstraite


class MenuUtilisateurConnecte(VueAbstraite):
    """Vue du menu d'un utilisateur connecté (qui n'a pas de rôle spécial
    comme administrateur ou profeissionnel)

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

        print("\n" + "-" * 50 + "\nMenu Principal\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter mes recettes favorites",
                "Chercher une recette",
                "Consulter mes notes et avis",
                "Mes ingrédients favoris et non-désirés",
                "Proposer une recette",
                "Ma liste de course",
                "Mon compte",
                "Quitter",
            ],
            max_height=15,
        ).execute()

        match choix:
            case "Consulter mes recettes favorites":
                self.afficher_recette_fav()
                return self
            case "Chercher une recette":
                from view.secondaire_connecte.recherche_recette import RechercheRecetteConnecte

                return RechercheRecetteConnecte()
            case "Consulter mes notes et avis":
                from view.secondaire_connecte.consulter_notes_avis import ConsulterNotesAvis

                return ConsulterNotesAvis()
            case "Mes ingrédients favoris et non-désirés":
                from view.secondaire_connecte.ingredients_fav_et_nd import IngredientsFavEtND

                return IngredientsFavEtND()
            case "Proposer une recette":
                from service.demande import proposer_recette

                proposer_recette()

            case "Ma liste de course":
                from view.secondaire_connecte.liste_courses import ListeCourses

                return ListeCourses()

            case "Mon compte":
                from view.secondaire_connecte.mon_compte_connecte import MonCompteConnecte

                return MonCompteConnecte()

            case "Quitter":
                print("Retour au menu précédent.")
                return None

    def afficher_recette_fav(self):
        """Affiche les recettes favorites et l'utilisateur peut sélectionner une recette."""
        id_utilisateur = Session().utilisateur.id_utilisateur
        dao_recette = RecetteDAO()
        dao_recette_fav = RecetteFavoriteDAO()
        service_recette = ServiceRecette(dao_recette, dao_recette_fav)

        favoris = service_recette.afficher_recettes_favorites(id_utilisateur)

        # Vérifiez si l'utilisateur a des recettes favorites
        if not favoris:
            inquirer.select(
                message="",
                choices=["OK"],
            ).execute()
            return self

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
            return self
