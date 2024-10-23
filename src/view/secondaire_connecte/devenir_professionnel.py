from InquirerPy import inquirer


class DemandeCompteProfessionnelVue:
    """Vue pour un utilisateur connecté souhaitant faire une demande de compte professionnel.

    L'utilisateur doit fournir une justification pour devenir un professionnel.
    """

    def __init__(self, nom_utilisateur):
        self.nom_utilisateur = nom_utilisateur

    def choisir_menu(self):
        """Affiche le menu pour faire une demande de compte professionnel.

        Return
        ------
        vue
            Retourne la vue suivante après soumission de la demande.
        """
        print(
            f"\n"
            + "-" * 50
            + f"\nDemande de compte professionnel pour {self.nom_utilisateur}\n"
            + "-" * 50
            + "\n"
        )

        # Demande à l'utilisateur d'expliquer pourquoi il souhaite devenir professionnel
        raison_demande = inquirer.text(
            message="Expliquez pourquoi vous souhaitez devenir professionnel : ",
            validate=lambda x: len(x) >= 10,
            invalid_message="Votre explication doit contenir au moins 10 caractères.",
        ).execute()

        # Simule la soumission de la demande
        if self.soumettre_demande(raison_demande):
            print(f"Merci {self.nom_utilisateur}, votre demande a été soumise avec succès.")
            from view.menu_principal_vue import MenuPrincipalVue

            return MenuPrincipalVue()  # Redirection vers le menu principal
        else:
            print("Une erreur est survenue lors de la soumission de la demande.")
            return self

    def soumettre_demande(self, raison_demande):
        """Simule la soumission de la demande de compte professionnel.

        Parameters
        ----------
        raison_demande : str
            La raison pour laquelle l'utilisateur souhaite devenir professionnel.

        Return
        ------
        bool
            Retourne True si la demande a été soumise avec succès, False sinon.
        """
        # Ici, tu pourrais ajouter la logique d'enregistrement dans une base de données
        print("\nDemande soumise avec succès !")
        print(f"Raison de la demande : {raison_demande}")
        return True  # Simule une réussite de soumission
