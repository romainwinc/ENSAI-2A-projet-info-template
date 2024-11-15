from view.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from view.session import Session
from service.service_demande import ServiceDemande
from dao.demande_dao import DemandeDAO


class DemandeChangerRole(VueAbstraite):
    """Vue pour effectuer une demande pour passer professionnel."""

    def afficher(self):
        """Non utilisé dans cette vue."""
        pass

    def choisir_menu(self):
        """
        Affiche les prompts pour ajouter une demande de passage professionnel et soumet les
        informations.
        """
        print(
            "\n"
            + "-" * 50
            + "\nEffectuer une demande pour passer professionnel\n"
            + "-" * 50
            + "\n"
        )

        # Collecte des informations d'avis
        id_utilisateur = Session().utilisateur.id_utilisateur
        type_demande = inquirer.select(
            message="Que souhaitez-vous faire ?",
            choices=["Passer administrateur", "Abandonner le role de professionnel"],
        ).execute()
        attribut_modifie = "role"
        if type_demande == "Abandonner le role de professionnel":
            attribut_corrige = "Connecté"
        elif type_demande == "Passer administrateur":
            attribut_corrige = "Administrateur"
        commentaire_demande = inquirer.text(message="Entrez un commentaire :").execute()

        dao = DemandeDAO()
        service_demande = ServiceDemande(dao)
        service_demande.creer_demande(
            id_utilisateur=id_utilisateur,
            type_demande=type_demande,
            attribut_modifie=attribut_modifie,
            attribut_corrige=attribut_corrige,
            commentaire_demande=commentaire_demande,
        )

        print("\nMerci ! Votre demande a été prise en compte et va être traitée.")
        from view.secondaire_pro.mon_compte_pro import MonComptePro

        return MonComptePro()
