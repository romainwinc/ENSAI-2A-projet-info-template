from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session
from service.service_utilisateur import ServiceUtilisateur
from dao.utilisateur_dao import UtilisateurDao


class MonCompteConnecte(VueAbstraite):
    """Vue de la gestion du compte d'un utilisateur connecté (qui n'a pas de rôle spécial
    comme administrateur ou professionnel)

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

        print("\n" + "-" * 50 + "\nMon Compte\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Demande de compte professionnel ou administrateur",
                "Déconnexion",
                "Supprimer mon compte",
                "Retour au menu principal",
            ],
            max_height=10,
        ).execute()

        match choix:
            case "Demande de compte professionnel ou administrateur":
                from view.secondaire_connecte.demande_changer_role import DemandeChangerRole

                return DemandeChangerRole()

            case "Déconnexion":
                Session().deconnexion()
                from view.menu_non_connecte import MenuNonConnecte

                return MenuNonConnecte()

            case "Supprimer mon compte":
                id_utilisateur = Session().utilisateur.id_utilisateur
                ServiceUtilisateur(UtilisateurDao()).supprimer_utilisateur(id_utilisateur)
                Session().deconnexion()
                from view.menu_non_connecte import MenuNonConnecte

                return MenuNonConnecte()

            case "Retour au menu principal":
                from view.menus_principaux.menu_connecte import MenuUtilisateurConnecte

                return MenuUtilisateurConnecte("Retour au menu")
