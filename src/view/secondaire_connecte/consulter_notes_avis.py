from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session
from service.service_avis import AvisService
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
                "Consulter mes notes",
                "Consulter mes avis",
                "Supprimer mes notes",
                "Supprimer mes avis",
            ],
        ).execute()

        match choix:
            case "Consulter mes notes":
                dao = AvisDAO()
                avis_service = AvisService(dao)
                utilisateur_id = Session().utilisateur
                avis_service.afficher_avis_utilisateur(utilisateur_id)

            case "Consulter mes avis":
                dao = AvisDAO()
                avis_service = AvisService(dao)
                utilisateur_id = Session().utilisateur
                avis_service.afficher_avis_utilisateur(utilisateur_id)

            case "Supprimer mes notes":
                dao = AvisDAO()
                avis_service = AvisService(dao)
                utilisateur_id = Session().utilisateur
                avis_service.supprimer_note_utilisateur(utilisateur_id)

            case "Supprimer mes avis":
                dao = AvisDAO()
                avis_service = AvisService(dao)
                utilisateur_id = Session().utilisateur
                avis_service.supprimer_avis_utilisateur(utilisateur_id)
