from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session
from service.service_utilisateur import ServiceUtilisateur
from dao.utilisateur_dao import UtilisateurDao


class MonComptePro(VueAbstraite):
    """Vue de la gestion du compte d'un utilisateur professionnel

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
        """Choix du menu suivant de l'utilisateur professionnel

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMon Compte\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Demande de compte administrateur ou abandonner le role de professionnel",
                "Déconnexion",
                "Supprimer mon compte",
                "Retour au menu professionnel",
            ],
            max_height=10,
        ).execute()

        match choix:
            case "Demande de compte administrateur ou abandonner le role de professionnel":
                from view.secondaire_pro.demande_changer_role import DemandeChangerRole

                return DemandeChangerRole()

            case "Retour au menu professionnel":
                from view.menus_principaux.menu_professionnel import MenuProfessionnel

                return MenuProfessionnel("Retour au menu")

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
