from datetime import datetime
from dao.avis_dao import AvisDAO
from models.avis import Avis
from InquirerPy import inquirer
from datetime import datetime


class ServiceAvis:
    def __init__(self, avis_dao):
        self.avis_dao = AvisDAO()

    def afficher_avis_par_recette(self, id_recette):
        """Affiche tous les avis pour une recette donnée."""
        avis = self.avis_dao.get_avis_by_recette_id(id_recette)
        if not avis:
            print("Aucun avis trouvé pour cette recette.")
            return

    def afficher_avis_par_utilisateur(self, id_utilisateur):
        """Affiche tous les avis d'un utilisateur donné."""
        avis = self.avis_dao.get_avis_by_user_id(id_utilisateur)
        if not avis:
            print("Aucun avis trouvé pour cet utilisateur.")
            return

        for a in avis:
            return self._afficher_avis(a)

    def _afficher_avis(self, avis: Avis):
        """Affiche les détails d'un avis."""

        print(f"Avis numéro: {avis.id_avis}")
        print(f"Pour la recette: {avis.id_recette}")
        print(f"Titre: {avis.titre_avis}")
        print(f"Auteur: {avis.nom_auteur}")
        print(f"Date de publication: {avis.date_publication}")
        print(f"Commentaire: {avis.commentaire}")
        print(f"Note: {avis.note}")
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
        return self.avis_dao.delete_avis(avis_id)
        print(f"Avis avec ID {avis_id} supprimé.")

    def modifier_avis(self, avis_id, **kwargs):
        """Modifie un avis."""
        return self.avis_dao.update_avis(avis_id, **kwargs)
        print(f"Avis avec ID {avis_id} mis à jour.")


if __name__ == "__main__":
    dao = AvisDAO()
    # ServiceAvis(dao).ajouter_avis(
    #     id_recette=1,
    #     id_utilisateur=8,
    #     titre_avis="Test",
    #     nom_auteur="Tata",
    #     date_publication=datetime.now(),
    #     commentaire="Bon",
    #     note=8,
    # )
    # ServiceAvis(dao).supprimer_avis(2)
    # ServiceAvis(dao).modifier_avis(avis_id=3, note=9)
    avis1 = Avis(
        id_recette=1,
        id_utilisateur=8,
        titre_avis="Test",
        nom_auteur="Tata",
        date_publication=datetime.now(),
        commentaire="Bon",
        note=9,
        id_avis=3,
    )
    # ServiceAvis(dao)._afficher_avis(avis1)
    ServiceAvis(dao).afficher_avis_par_recette(1)
