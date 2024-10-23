from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite


class MenuUtilisateurInscriptionVue(VueAbstraite):
    """Vue du menu d'inscription utilisateur

    Permet à un nouvel utilisateur de s'inscrire avec un nom d'utilisateur et un mot de passe.
    """

    def choisir_menu(self):
        """Affiche le menu d'inscription de l'utilisateur et gère l'inscription.

        Return
        ------
        vue
            Retourne la vue suivante une fois l'utilisateur inscrit.
        """
        print("\n" + "-" * 50 + "\nInscription Utilisateur\n" + "-" * 50 + "\n")

        # Demande un nom d'utilisateur
        nom_utilisateur = inquirer.text(
            message="Choisissez un nom d'utilisateur : ",
            validate=lambda x: len(x) >= 3,
            invalid_message="Le nom d'utilisateur doit contenir au moins 3 caractères.",
        ).execute()

        # Demande un mot de passe
        mot_de_passe = inquirer.secret(
            message="Choisissez un mot de passe : ",
            validate=lambda x: len(x) >= 6,
            invalid_message="Le mot de passe doit contenir au moins 6 caractères.",
        ).execute()

        # Confirme le mot de passe et vérifie qu'il correspond
        inquirer.secret(
            message="Confirmez votre mot de passe : ",
            validate=lambda x: x == mot_de_passe,
            invalid_message="Les mots de passe ne correspondent pas.",
        ).execute()

        # Simule l'inscription (enregistrement dans une base de données ou vérification)
        if self.inscrire_utilisateur(nom_utilisateur, mot_de_passe):
            print(f"Bienvenue, {nom_utilisateur} ! Vous êtes maintenant inscrit.")
            from view.menu_principal_vue import MenuPrincipalVue

            return MenuPrincipalVue()
        else:
            print("Erreur lors de l'inscription. Veuillez réessayer.")
            return self

    def inscrire_utilisateur(self, nom_utilisateur, mot_de_passe):
        """Simule l'enregistrement d'un nouvel utilisateur dans le système.

        Parameters
        ----------
        nom_utilisateur : str
            Le nom d'utilisateur choisi par l'utilisateur.
        mot_de_passe : str
            Le mot de passe choisi par l'utilisateur.

        Return
        ------
        bool
            Retourne True si l'inscription réussit, False sinon.
        """
        # Ici, tu pourrais ajouter l'utilisateur dans une base de données ou appeler un service.
        # Cet exemple retourne True directement pour simuler une inscription réussie.
        print(f"Inscription réussie pour l'utilisateur: {nom_utilisateur}")
        return True  # Simule une réussite d'inscription
