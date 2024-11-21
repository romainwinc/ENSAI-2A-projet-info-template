from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session
from service.service_utilisateur import ServiceUtilisateur
from dao.utilisateur_dao import UtilisateurDao


class MonCompteAdmin(VueAbstraite):
    """Vue de la gestion du compte d'un administrateur
    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'administrateur
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'administrateur

        Return
        ------
        vue
            Retourne la vue choisie par l'administrateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMon Compte\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Déconnexion",
                "Supprimer mon compte",
                "Retour au menu administrateur",
            ],
            max_height=10,
        ).execute()

        match choix:

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

            case "Retour au menu administrateur":
                from view.menus_principaux.menu_administrateur import MenuAdministrateur

                return MenuAdministrateur("Retour au menu")
