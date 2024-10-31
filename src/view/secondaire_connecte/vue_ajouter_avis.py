from view.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from view.session import Session
from service.service_avis import ServiceAvis
from datetime import datetime
from dao.avis_dao import AvisDAO


class VueAjouterAvis(VueAbstraite):
    """Vue pour ajouter un avis pour une recette."""

    def choisir_menu(self):
        """Non utilisé dans cette vue."""
        pass

    def afficher(self):
        """Affiche les prompts pour ajouter un avis et soumet les informations."""
        print("\n" + "-" * 50 + "\nAjouter un Avis\n" + "-" * 50 + "\n")

        # Collecte des informations d'avis
        nom_auteur = Session().utilisateur.nom_utilisateur
        id_utilisateur = Session().utilisateur.id_utilisateur
        id_recette = Session().recette.id_recette
        titre_avis = inquirer.text(message="Entrez le titre de l'avis :").execute()
        commentaire = inquirer.text(message="Entrez votre commentaire :").execute()
        note = inquirer.select(
            message="Notez la recette sur 5 :", choices=[0, 1, 2, 3, 4, 5]
        ).execute()
        date_publication = datetime.now().strftime("%Y-%m-%d")  # Date actuelle au format AAAA-MM-JJ

        # Appel à la méthode ajouter_avis dans ServiceAvis
        dao = AvisDAO()
        service_avis = ServiceAvis(dao)
        service_avis.ajouter_avis(
            id_recette=id_recette,
            id_utilisateur=id_utilisateur,
            titre_avis=titre_avis,
            nom_auteur=nom_auteur,
            date_publication=date_publication,
            commentaire=commentaire,
            note=note,
        )

        print("\nMerci ! Votre avis a été ajouté avec succès.")

        # Retourner à la vue de recherche
        Session().fermer_recette()
        from view.secondaire_connecte.recherche_recette import RechercheRecetteConnecte

        return RechercheRecetteConnecte()
