from datetime import datetime
from dao.avis_dao import AvisDAO
from models.avis import Avis
from InquirerPy import inquirer


class ServiceAvis:
    def __init__(self):
        self.avis_dao = AvisDAO()

    def afficher_avis_par_recette(self, id_recette):
        """Affiche tous les avis pour une recette donnée."""
        avis = self.avis_dao.get_avis_by_recette_id(id_recette)
        if not avis:
            print("Aucun avis trouvé pour cette recette.")
            return

        for a in avis:
            self._afficher_avis(a)

    def afficher_avis_par_utilisateur(self, id_utilisateur):
        """Affiche tous les avis d'un utilisateur donné."""
        avis = self.avis_dao.get_avis_by_user_id(id_utilisateur)
        if not avis:
            print("Aucun avis trouvé pour cet utilisateur.")
            return

        for a in avis:
            self._afficher_avis(a)

    def _afficher_avis(self, avis):
        """Affiche les détails d'un avis."""
        # Conversion des données de l'avis en objet Avis
        avis_obj = Avis(
            id_avis=avis["id_avis"],
            titre_avis=avis["titre_avis"],
            id_utilisateur=avis["id_utilisateur"],
            nom_auteur=avis["nom_auteur"],
            date_publication=avis["date_publication"],
            commentaire=avis["commentaire"],
            note=avis["note"],
        )
        print(f"Avis numéro: {avis_obj.id_avis}")
        print(f"Pour la recette: {avis_obj.id_recette}")  # Affiche l'ID de la recette
        print(f"Titre: {avis_obj.titre_avis}")  # titre_avis
        print(f"Auteur: {avis_obj.nom_auteur}")  # nom_auteur
        print(
            f"Date de publication: {avis_obj.date_publication.strftime('%d/%m/%Y')}"
        )  # date_publication
        print(f"Commentaire: {avis_obj.commentaire}")  # commentaire
        print(f"Note: {avis_obj.note or 'Non noté'}")  # note
        print("-" * 40)  # Ligne de séparation

    def ajouter_avis(
        self,
        id_recette,
        id_utilisateur,
        titre_avis,
        nom_auteur,
        date_publication,
        commentaire,
        note,
    ):
        """Ajoute un nouvel avis et retourne l'ID de l'avis ajouté."""
        return self.avis_dao.add_avis(
            id_recette, id_utilisateur, titre_avis, nom_auteur, date_publication, commentaire, note
        )

    def supprimer_avis(self, avis_id):
        """Supprime un avis par son ID."""
        self.avis_dao.delete_avis(avis_id)
        print(f"Avis avec ID {avis_id} supprimé.")

    def modifier_avis(self, avis_id, **kwargs):
        """Modifie un avis."""
        self.avis_dao.update_avis(avis_id, **kwargs)
        print(f"Avis avec ID {avis_id} mis à jour.")


if __name__ == "__main__":
    dao = AvisDAO()
    AvisService(dao).creer_avis(1)
