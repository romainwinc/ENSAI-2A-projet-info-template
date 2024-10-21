from InquirerPy import inquirer


class MenuGestionCompteVue:
    """Vue de gestion de compte réservée aux administrateurs

    Permet à l'administrateur de gérer les comptes des utilisateurs.
    """

    def choisir_menu(self):
        """Affiche le menu de gestion de compte et gère les choix de l'administrateur.

        Return
        ------
        vue
            Retourne la vue choisie par l'administrateur dans le terminal.
        """
        print("\n" + "-" * 50 + "\nMenu Gestion de Compte\n" + "-" * 50 + "\n")

        # Affichage du menu et demande de choix à l'administrateur
        choix = inquirer.select(
            message="Que voulez-vous faire ?",
            choices=[
                "Créer un compte",
                "Accepter une demande de compte professionnel",
                "Supprimer un compte",
                "Quitter",
            ],
        ).execute()

        # Gestion des choix de l'administrateur avec 'match case'
        match choix:
            case "Créer un compte":
                from view.creer_compte_vue import CreerCompteVue

                return CreerCompteVue()

            case "Accepter une demande de compte professionnel":
                from view.accepter_demande_vue import AccepterDemandeVue

                return AccepterDemandeVue()

            case "Supprimer un compte":
                from view.supprimer_compte_vue import SupprimerCompteVue

                return SupprimerCompteVue()

            case "Quitter":
                print("Retour au menu précédent.")
                return None
