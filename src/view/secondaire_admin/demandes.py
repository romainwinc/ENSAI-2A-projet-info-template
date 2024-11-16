from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from service.service_demande import ServiceDemande
from dao.demande_dao import DemandeDAO
from service.service_utilisateur import ServiceUtilisateur
from dao.utilisateur_dao import UtilisateurDao
from service.service_recette import ServiceRecette
from dao.recette_dao import RecetteDAO
from dao.recette_favorite_dao import RecetteFavoriteDAO


class Demandes(VueAbstraite):
    """Vue du menu d'un administrateur pour consulter et traiter les demandes"""

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nGestion des demandes\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Demandes de changement de rôle",
                "Demandes de suppression de recette",
                "Retour au menu principal",
            ],
        ).execute()

        match choix:
            case "Demandes de changement de rôle":
                self.traiter_demande_role()
                return self

            case "Demandes de suppression de recette":
                self.traiter_demande_suppression_recette()
                return self

            case "Retour au menu principal":
                from view.menus_principaux.menu_administrateur import MenuAdministrateur

                return MenuAdministrateur()

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
                print(demande_selectionnee)
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

    def traiter_demande_suppression_recette(self):
        dao_demande = DemandeDAO()
        demande_service = ServiceDemande(dao_demande)
        dao_recette = RecetteDAO()
        dao_recette_fav = RecetteFavoriteDAO()
        recette_service = ServiceRecette(dao_recette, dao_recette_fav)
        liste = []

        demandes = demande_service.recuperer_demandes_with_recette()

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
                print(demande_selectionnee)
                if demande_selectionnee:
                    demande_service.afficher_demande(demande_selectionnee["id_demande"])
                    # Demander à l'utilisateur s'il souhaite accepter ou refuser la demande
                    action = inquirer.select(
                        message="Que voulez-vous faire avec cette demande ?",
                        choices=["Accepter", "Refuser"],
                    ).execute()

                    if action == "Accepter":
                        recette_service.supprimer_recette(
                            demande_selectionnee["attribut_modifie"],
                        )
                        print(f"La demande {demande_selectionnee['id_demande']} a été acceptée.")

                    elif action == "Refuser":
                        # Traiter le refus
                        print(f"La demande {demande_selectionnee['id_demande']} a été refusée.")
                    demande_service.supprimer_demande(demande_selectionnee["id_demande"])
            else:
                return self
        else:
            inquirer.select(
                message="",
                choices=["Retour au menu principal"],
            ).execute()
