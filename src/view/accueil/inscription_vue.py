from InquirerPy import inquirer
from InquirerPy.validator import PasswordValidator


from view.vue_abstraite import VueAbstraite
from service.service_utilisateur import ServiceUtilisateur


class InscriptionVue(VueAbstraite):
    def choisir_menu(self):
        # Demande à l'utilisateur de saisir son nom d'utilisateur, mot de passe...
        nom_utilisateur = inquirer.text(message="Entrez votre nom d'utilsateur : ").execute()

        if ServiceUtilisateur().nom_utilisateur_deja_utilise(nom_utilisateur):
            from view.accueil.accueil_vue import AccueilVue

            return AccueilVue(f"Le nom d'utilisateur {nom_utilisateur} est déjà utilisé.")

        mdp = inquirer.secret(
            message="Entrez votre mot de passe : ",
            validate=PasswordValidator(
                length=8,
                cap=True,
                number=True,
                message="Au moins 8 caractères, incluant une majuscule et un chiffre",
            ),
        ).execute()

        # Appel du service pour créer le joueur
        utilisateur = ServiceUtilisateur().creer(nom_utilisateur, mdp)

        # Si l'utilisateur a été créé
        if utilisateur:
            message = (
                f"Votre compte {utilisateur.nom_utilisateur} a été créé. "
                "Vous pouvez maintenant vous connecter."
            )
        else:
            message = "Erreur de connexion (nom d'utilisateur ou mot de passe invalide)"

        from view.accueil.accueil_vue import AccueilVue

        return AccueilVue(message)
