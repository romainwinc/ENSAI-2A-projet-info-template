from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session


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
                "Consulter mes notes",
                "Consulter mes avis",
                "Supprimer mes notes",
                "Supprimer mes avis",
            ],
        ).execute()

        match choix:
            case "Consulter mes notes":
                pass

            case "Consulter mes avis":
                from service.service_avis import afficher_avis_utilisateur

                afficher_avis_utilisateur()
            case "Supprimer mes notes":
                pass

            case "Supprimer mes avis":
                from service.service_avis import supprimer_avis

                supprimer_avis()
