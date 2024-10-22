from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session


class ConnexionVue(VueAbstraite):
    """Vue de Connexion (saisie du nom d'utilisateur et mdp)"""

    def choisir_menu(self):
        # Demande à l'utilisateur de saisir nom d'utilisateur et mot de passe
        utilisateur = inquirer.text(message="Entrez votre nom d'utilisateur : ").execute()
        mdp = inquirer.secret(message="Entrez votre mot de passe :").execute()

        # Appel du service pour trouver le joueur
        from service.service_utilisateur import ServiceUtilisateur

        utilisateur = ServiceUtilisateur().se_connecter(utilisateur, mdp)

        # Si le joueur a été trouvé à partir des ses identifiants de connexion
        if utilisateur:
            message = (
                f"Vous êtes connecté sous l'utilisateur {utilisateur.nom_utilisateur} "
                f"en tant qu'utilisateur {utilisateur.nom_utilisateur}."
            )
            Session().connexion(utilisateur)

            from view.menu_joueur_vue import MenuJoueurVue

            return MenuJoueurVue(message)

        message = "Erreur de connexion (nom d'utilisateur ou mot de passe invalide)"
        from view.accueil.accueil_vue import AccueilVue

        return AccueilVue(message)
