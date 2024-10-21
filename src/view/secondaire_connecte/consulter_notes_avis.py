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
                pass

            case "Consulter mes avis":

                dao = AvisDAO()
                avis_service = AvisService(dao)
                avis_service.afficher_avis_utilisateur(Session().utilisateur)
            case "Supprimer mes notes":
                pass

            case "Supprimer mes avis":
                utilisateur_id = Session().utilisateur
                # Récupérer les avis de l'utilisateur
                avis_list = self.service_avis.recuperer_avis_par_utilisateur(utilisateur_id)

                if avis_list:
                    # Afficher les avis disponibles avec leur ID pour que l'utilisateur sache quel ID choisir
                    print("\nVoici vos avis :\n")
                    for avis in avis_list:
                        print(
                            f"ID: {avis.id}, Titre: {avis.titre}, Commentaire: {avis.commentaire}"
                        )

                    # Demander à l'utilisateur d'entrer l'ID de l'avis à supprimer
                    avis_id = inquirer.text(
                        message="Entrez l'ID de l'avis que vous souhaitez supprimer :",
                    ).execute()

                    # Valider que l'ID est bien dans la liste des avis de l'utilisateur
                    avis_ids = [str(avis.id) for avis in avis_list]
                    if avis_id in avis_ids:
                        # Supprimer l'avis si l'ID est valide
                        self.avis_service.supprimer_avis(int(avis_id))
                        print(f"L'avis avec l'ID {avis_id} a été supprimé.")
                    else:
                        print("L'ID fourni ne correspond à aucun de vos avis.")
                else:
                    print("Vous n'avez aucun avis à supprimer.")
