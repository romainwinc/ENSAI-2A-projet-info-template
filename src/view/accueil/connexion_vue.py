from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session
from dao.utilisateur_dao import UtilisateurDao


class ConnexionVue(VueAbstraite):
    """Vue de Connexion (saisie du nom d'utilisateur et mdp)"""

    def choisir_menu(self):
        # Demande à l'utilisateur de saisir nom d'utilisateur et mot de passe
        utilisateur = inquirer.text(message="Entrez votre nom d'utilisateur : ").execute()
        mdp = inquirer.secret(message="Entrez votre mot de passe :").execute()

        # Appel du service pour trouver le joueur
        from service.service_utilisateur import ServiceUtilisateur

        utilisateur = ServiceUtilisateur(UtilisateurDao()).se_connecter(utilisateur, mdp)

        # Si le joueur a été trouvé à partir des ses identifiants de connexion
        if utilisateur:
            message = (
                f"Vous êtes connecté sous le nom {utilisateur.nom_utilisateur} "
                f"en tant qu'utilisateur {utilisateur.role}."
            )
            Session().connexion(utilisateur)

            if utilisateur.role == "Connecté":
                from view.menus_principaux.menu_connecte import MenuUtilisateurConnecte

                return MenuUtilisateurConnecte(message)

            elif utilisateur.role == "Professionnel":
                from view.menus_principaux.menu_professionnel import MenuProfessionnel

                return MenuProfessionnel(message)

            elif utilisateur.role == "Administrateur":
                from view.menus_principaux.menu_administrateur import MenuAdministrateur

                return MenuAdministrateur(message)

        message = "Erreur de connexion (nom d'utilisateur ou mot de passe invalide)"
        from view.accueil.accueil_vue import AccueilVue

        return AccueilVue(message)
