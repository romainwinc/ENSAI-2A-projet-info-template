from InquirerPy import inquirer


class MenuUtilisateurSeConnecter:
    """Vue du menu de connexion utilisateur

    Permet à l'utilisateur de se connecter avec un nom d'utilisateur et un mot de passe.
    """

    def choisir_menu(self):
        """Affiche le menu de connexion de l'utilisateur et gère la connexion.

        Return
        ------
        vue
            Retourne la vue suivante une fois l'utilisateur connecté.
        """
        print("\n" + "-" * 50 + "\nConnexion Utilisateur\n" + "-" * 50 + "\n")

        # Demande le nom d'utilisateur
        nom_utilisateur = inquirer.text(
            message="Entrez votre nom d'utilisateur : ",
            validate=lambda x: x != "",
            invalid_message="Le nom d'utilisateur ne peut pas être vide.",
        ).execute()

        # Demande le mot de passe
        mot_de_passe = inquirer.secret(
            message="Entrez votre mot de passe : ",
            validate=lambda x: x != "",
            invalid_message="Le mot de passe ne peut pas être vide.",
        ).execute()

        # Simuler la vérification des informations de connexion (exemple de validation)
        if self.verifier_connexion(nom_utilisateur, mot_de_passe):
            print(f"Bienvenue, {nom_utilisateur} ! Vous êtes maintenant connecté.")
            from view.menu_principal_vue import MenuPrincipalVue

            return MenuPrincipalVue()
        else:
            print("Nom d'utilisateur ou mot de passe incorrect.")
            return self

    def verifier_connexion(self, nom_utilisateur, mot_de_passe):
        """Simule la vérification des informations de connexion.

        Parameters
        ----------
        nom_utilisateur : str
            Le nom d'utilisateur entré par l'utilisateur.
        mot_de_passe : str
            Le mot de passe entré par l'utilisateur.

        Return
        ------
        bool
            Retourne True si les informations de connexion sont valides, False sinon.
        """
        # Ici, tu pourrais vérifier les informations dans une base de données
        # ou appeler un service pour authentifier l'utilisateur.
        # Cet exemple compare avec des informations fictives pour simplifier.
        utilisateur_valide = "admin"
        mot_de_passe_valide = "password123"

        return nom_utilisateur == utilisateur_valide and mot_de_passe == mot_de_passe_valide
