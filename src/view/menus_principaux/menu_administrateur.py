from InquirerPy import inquirer
from view.session import Session
from dao.recette_dao import RecetteDAO
from dao.recette_favorite_dao import RecetteFavoriteDAO
from service.service_recette import ServiceRecette
from service.service_demande import ServiceDemande
from dao.demande_dao import DemandeDAO
from view.vue_abstraite import VueAbstraite
from service.service_utilisateur import ServiceUtilisateur
from dao.utilisateur_dao import UtilisateurDao


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
                "Consulter mes recettes favorites",
                "Consulter une recette",
                "Consulter mes notes et avis",
                "Mes ingrédients favoris ou non-désirés",
                "Ma liste de course",
                "Proposer une recette",
                "Consulter les demandes de changement de role",
                "Consulter les demandes de suppression de recette",
                "Mon compte",
                "Quitter",
            ],
        ).execute()

        # Gestion des choix de l'administrateur avec 'match case'
        match choix:
            case "Consulter mes recettes favorites":
                self.afficher_recette_fav()
                return self

            case "Consulter une recette":
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

            case "Consulter les demandes de suppression de recette":
                pass

            case "Consulter les demandes de changement de role":
                self.traiter_demande_role()
                return self

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

    def traiter_demande_role(self):
        dao_demande = DemandeDAO()
        demande_service = ServiceDemande(dao_demande)
        dao_utilisateur = UtilisateurDao()
        utilisateur_service = ServiceUtilisateur(dao_utilisateur)
        liste = []

        demandes = demande_service.recuperer_demandes_with_role()

        if demandes:
            for demande in demandes:
                liste.append(demande["id_demande"])

            print(liste)

            choix_menu = liste + ["Retour au menu principal"]
            choix = inquirer.select(
                message="Sélectionnez la demande que vous voulez traiter :",
                choices=choix_menu,
            ).execute()

            if choix in liste:
                demande_selectionnee = next(
                    (demande for demande in demandes if demande["id_demande"] == choix), None
                )
                if demande_selectionnee:
                    demande_service.afficher_demande(demande_selectionnee["id_demande"])
                    # Demander à l'utilisateur s'il souhaite accepter ou refuser la demande
                    action = inquirer.select(
                        message="Que voulez-vous faire avec cette demande ?",
                        choices=["Accepter", "Refuser"],
                    ).execute()

                    if action == "Accepter":
                        utilisateur_service.changer_role_utilisateur(
                            demande_selectionnee["id_utilisateur"],
                            demande_selectionnee["attribut_corrige"],
                        )
                        print(f"La demande {demande_selectionnee['id_demande']} a été acceptée.")

                    elif action == "Refuser":
                        # Traiter le refus
                        print(f"La demande {demande_selectionnee['id_demande']} a été refusée.")
                    demande_service.supprimer_demande(demande_selectionnee["id_demande"])
            else:
                # Retourner à la vue principal
                return self
        else:
            inquirer.select(
                message="",
                choices=["Retour au menu principal"],
            ).execute()
