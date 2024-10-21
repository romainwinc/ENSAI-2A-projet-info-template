from InquirerPy import inquirer

from View.vue_abstraite import VueAbstraite
from View.session import Session


class MonCompteConnecte(VueAbstraite):
    """Vue de la gestion du compte d'un utilisateur connecté (qui n'a pas de rôle spécial
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

        print("\n" + "-" * 50 + "\nMon Compte\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=["Demande de compte professionnel", "Déconnexion", "Supprimer mon compte"],
        ).execute()

        match choix:
            case "Demande de compte professionnel":
                pass

            case "Déconnexion":
                Session().deconnexion()
                from View.menu_non_connecte import MenuNonConnecte

                return MenuNonConnecte()

            case "Supprimer mon compte":
                pass
