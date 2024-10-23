from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session


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
            choices=["Déconnexion", "Supprimer mon compte", "Retour au menu professionnel"],
        ).execute()

        match choix:
            case "Retour au menu professionnel":
                from view.menus_principaux.menu_professionnel_vue import MenuProfessionnelVue

                return MenuProfessionnelVue("Retour au menu")

            case "Déconnexion":
                Session().deconnexion()
                from view.menu_non_connecte import MenuNonConnecte

                return MenuNonConnecte()

            case "Supprimer mon compte":
                pass
