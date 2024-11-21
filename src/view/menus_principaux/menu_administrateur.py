from InquirerPy import inquirer
from view.session import Session
from dao.recette_dao import RecetteDAO
from dao.recette_favorite_dao import RecetteFavoriteDAO
from service.service_recette import ServiceRecette
from view.vue_abstraite import VueAbstraite


class MenuAdministrateur(VueAbstraite):
    """Vue du menu de l'administrateur

    Permet à l'administrateur de gérer ses recettes, avis, ingrédients, etc.
    """

    def choisir_menu(self):
        """Affiche le menu de l'administrateur et gère ses choix.

        Return
        ------
        vue
            Retourne la vue choisie par l'administrateur dans le terminal.
        """
        print("\n" + "-" * 50 + "\nMenu Administrateur\n" + "-" * 50 + "\n")

        # Affichage du menu et demande de choix à l'administrateur
        choix = inquirer.select(
            message="Que voulez-vous faire ?",
            choices=[
                "Chercher une recette",
                "Consulter mes recettes favorites",
                "Consulter mes notes et avis",
                "Mes ingrédients favoris ou non-désirés",
                "Ma liste de course",
                "Gérer les demandes",
                "Mon compte",
                "Quitter",
            ],
            max_height=10,
        ).execute()

        # Gestion des choix de l'administrateur avec 'match case'
        match choix:
            case "Consulter mes recettes favorites":
                self.afficher_recette_fav()
                return self

            case "Chercher une recette":
                from view.secondaire_admin.recherche_recette import RechercheRecetteAdmin

                return RechercheRecetteAdmin()

            case "Consulter mes notes et avis":
                from view.secondaire_admin.consulter_notes_avis import ConsulterNotesAvis

                return ConsulterNotesAvis()

            case "Mes ingrédients favoris ou non-désirés":
                from view.secondaire_admin.ingredients_fav_et_nd import IngredientsFavEtND

                return IngredientsFavEtND()

            case "Proposer une recette":
                pass

            case "Ma liste de course":
                from view.secondaire_admin.liste_courses import ListeCourses

                return ListeCourses()

            case "Gérer les demandes":
                from view.secondaire_admin.demandes import Demandes

                return Demandes()

            case "Mon compte":
                from view.secondaire_admin.mon_compte_admin import MonCompteAdmin

                return MonCompteAdmin()

            case "Quitter":
                print("Merci d'avoir utilisé Recipe-Makers. À bientôt !")
                exit()

    def afficher_recette_fav(self):
        """Affiche les recettes favorites et l'administrateur peut sélectionner une recette."""
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
            from view.secondaire_admin.vue_detail_recette_fav import DetailRecetteFav

            return DetailRecetteFav().afficher()
        else:
            # Retourner au menu précédent
            return self
