from view.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from view.session import Session
from service.service_demande import ServiceDemande
from dao.demande_dao import DemandeDAO


class DemandeSuppressionRecette(VueAbstraite):
    """Vue pour effectuer une demande poursupprimer une recette."""

    def choisir_menu(self):
        """
        Affiche les prompts pour ajouter une demande de suppression de recette
        """
        print(
            "\n"
            + "-" * 50
            + "\nEffectuer une demande de suppression de recette\n"
            + "-" * 50
            + "\n"
        )

        # Collecte des informations d'avis
        id_utilisateur = Session().utilisateur.id_utilisateur
        type_demande = "Suppression recette"
        attribut_modifie = int(
            inquirer.text(message="Entrez l'id de la recette à supprimer :").execute()
        )

        attribut_corrige = None
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
        from view.menus_principaux.menu_professionnel import MenuProfessionnel

        return MenuProfessionnel()
