from InquirerPy import inquirer

from view.session import Session
from dao.recette_dao import RecetteDAO
from dao.recette_favorite_dao import RecetteFavoriteDAO
from service.service_recette import ServiceRecette
from view.vue_abstraite import VueAbstraite


class MenuProfessionnel(VueAbstraite):
    """Vue d'accueil pour un professionnel"""

    def choisir_menu(self):
        """Choix du menu suivant pour un professionnel

        Return
        ------
        view
            Retourne la vue choisie par le professionnel dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Professionnel\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Chercher une recette",
                "Consulter mes recettes favorites",
                "Consulter mes notes et avis",
                "Mes ingrédients favoris et non-désirés",
                "Ma liste de course",
                "Créer une recette",
                "Demander la suppression d'une recette",
                "Mon compte",
                "Quitter",
            ],
            max_height=10,
        ).execute()

        match choix:
            case "Consulter mes recettes favorites":
                self.afficher_recette_fav()
                return self

            case "Chercher une recette":
                from view.secondaire_pro.recherche_recette import RechercheRecettePro

                return RechercheRecettePro()

            case "Consulter mes notes et avis":
                from view.secondaire_pro.consulter_notes_avis import ConsulterNotesAvis

                return ConsulterNotesAvis()

            case "Mes ingrédients favoris et non-désirés":
                from view.secondaire_pro.ingredients_fav_et_nd import IngredientsFavEtND

                return IngredientsFavEtND()

            case "Créer une recette":
                from view.secondaire_pro.creer_recette import CreerRecette

                vue_creer_recette = CreerRecette()
                return vue_creer_recette

            case "Ma liste de course":
                from view.secondaire_pro.liste_courses import ListeCourses

                return ListeCourses()

            case "Demander la suppression d'une recette":
                from view.secondaire_pro.demande_suppression_recette import (
                    DemandeSuppressionRecette,
                )

                return DemandeSuppressionRecette()

            case "Mon compte":
                from view.secondaire_pro.mon_compte_pro import MonComptePro

                return MonComptePro()

            case "Quitter":
                print("Merci d'avoir utilisé Recipe-Makers. À bientôt !")
                exit()

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
            from view.secondaire_pro.vue_detail_recette_fav import DetailRecetteFav

            return DetailRecetteFav().afficher()
        else:
            # Retourner au menu précédent
            return self
