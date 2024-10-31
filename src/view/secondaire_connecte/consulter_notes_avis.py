from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session
from service.service_avis import ServiceAvis
from dao.avis_dao import AvisDAO


class ConsulterNotesAvis(VueAbstraite):
    """Vue du menu d'un utilisateur pour regarder ses notes et avis
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

        print("\n" + "-" * 50 + "\nMes Notes et Avis\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter mes avis",
                "Supprimer mes avis",
                "Consulter mes notes",
                "Modifier mes notes",
                "Retour au menu principal",
            ],
        ).execute()

        utilisateur_id = Session().utilisateur.id_utilisateur
        dao = AvisDAO()
        avis_service = ServiceAvis(dao)

        match choix:
            case "Consulter mes notes":
                avis_service.afficher_notes_par_utilisateur(utilisateur_id)
                inquirer.select(
                    message="",
                    choices=["Suivant"],
                ).execute()
                return self

            case "Consulter mes avis":
                avis_service.afficher_avis_par_utilisateur(utilisateur_id)
                inquirer.select(
                    message="",
                    choices=["Suivant"],
                ).execute()
                return self

            case "Modifier mes notes":
                self.modifier_notes()
                return self

            case "Supprimer mes avis":
                self.supprimer_avis()
                return self

            case "Retour au menu principal":
                from view.menus_principaux.menu_connecte import MenuUtilisateurConnecte

                return MenuUtilisateurConnecte()

    def supprimer_avis(self):
        """Affiche les avis à supprimer."""
        utilisateur_id = Session().utilisateur.id_utilisateur
        dao = AvisDAO()
        avis_service = ServiceAvis(dao)
        liste = []  # Liste pour stocker les id des avis de la personne

        avis = avis_service.afficher_avis_par_utilisateur(utilisateur_id)

        if avis:
            for avi in avis:
                liste.append(avi.id_avis)

            # Afficher le menu avec les noms des recettes trouvées ou une option de retour
            choix_menu = liste + ["Retour au menu des avis et notes"]
            choix = inquirer.select(
                message="Sélectionnez l'avis que vous voulez supprimer :",
                choices=choix_menu,
            ).execute()

            if choix in liste:
                # Trouver la recette correspondante
                avis_selectionne = next((avi for avi in avis if avi.id_avis == choix), None)
                if avis_selectionne:
                    avis_service.supprimer_avis(avis_selectionne.id_avis)
            else:
                # Retourner à la vue de recherche
                return self
        else:
            inquirer.select(
                message="",
                choices=["Retour au menu des avis et notes"],
            ).execute()

    def modifier_notes(self):
        """Affiche les notes à modifier."""
        utilisateur_id = Session().utilisateur.id_utilisateur
        dao = AvisDAO()
        avis_service = ServiceAvis(dao)
        liste = []  # Liste pour stocker les id des avis de la personne

        avis = avis_service.afficher_avis_par_utilisateur(utilisateur_id)

        if avis:
            for avi in avis:
                liste.append(avi.id_avis)

            # Afficher le menu avec les noms des recettes trouvées ou une option de retour
            choix_menu = liste + ["Retour au menu des avis et notes"]
            choix = inquirer.select(
                message="Sélectionnez l'avis pour lequel vous voulez changer la note :",
                choices=choix_menu,
            ).execute()

            if choix in liste:
                nouvelle_note = inquirer.select(
                    message="Indiquer la nouvelle note que vous voulez attribuer",
                    choices=[0, 1, 2, 3, 4, 5],
                ).execute()
                # Trouver la recette correspondante
                avis_service.modifier_avis(choix, note=int(nouvelle_note))
                print("La note a été modifiée avec succès.")
            else:
                # Retourner à la vue de recherche
                return self
        else:
            inquirer.select(
                message="",
                choices=["Retour au menu des avis et notes"],
            ).execute()
