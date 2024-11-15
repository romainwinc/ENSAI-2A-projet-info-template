from datetime import datetime
from dao.avis_dao import AvisDAO
from models.avis import Avis


class ServiceAvis:
    def __init__(self, avis_dao: AvisDAO()):
        self.avis_dao = avis_dao

    def afficher_avis_par_recette(self, id_recette):
        """Affiche tous les avis pour une recette donnée."""
        avi = self.avis_dao.get_avis_by_recette_id(id_recette)
        avis = []
        for i in range(len(avi)):
            avis.append(
                Avis(
                    id_avis=avi[i]["id_avis"],
                    id_recette=avi[i]["id_recette"],
                    id_utilisateur=avi[i]["id_utilisateur"],
                    titre_avis=avi[i]["titre_avis"],
                    nom_auteur=avi[i]["nom_auteur"],
                    date_publication=avi[i]["date_publication"],
                    commentaire=avi[i]["commentaire"],
                    note=avi[i]["note"],
                )
            )
        if not avis:
            print("Aucun avis trouvé pour cette recette.")
            return

        for a in avis:
            print(self._afficher_avis(a))

    def afficher_avis_par_utilisateur(self, id_utilisateur):
        """Affiche tous les avis d'un utilisateur donné."""
        avi = self.avis_dao.get_avis_by_user_id(id_utilisateur)
        avis = []
        for i in range(len(avi)):
            avis.append(
                Avis(
                    id_avis=avi[i]["id_avis"],
                    id_recette=avi[i]["id_recette"],
                    id_utilisateur=avi[i]["id_utilisateur"],
                    titre_avis=avi[i]["titre_avis"],
                    nom_auteur=avi[i]["nom_auteur"],
                    date_publication=avi[i]["date_publication"],
                    commentaire=avi[i]["commentaire"],
                    note=avi[i]["note"],
                )
            )
        if not avis:
            print("Aucun avis trouvé.")
            return

        for a in avis:
            print(self._afficher_avis(a))
        return avis

    def _afficher_avis(self, avis: Avis):
        """Affiche les détails d'un avis."""

        print(f"Avis numéro: {avis.id_avis}")
        print(f"Pour la recette: {avis.id_recette}")
        print(f"Titre: {avis.titre_avis}")
        print(f"Auteur: {avis.nom_auteur}")
        print(f"Date de publication: {avis.date_publication}")
        print(f"Commentaire: {avis.commentaire}")
        print(f"Note: {avis.note}/5")
        print("-" * 40)  # Ligne de séparation

    def afficher_notes_par_utilisateur(self, id_utilisateur):
        """Affiche tous les avis d'un utilisateur donné."""
        avi = self.avis_dao.get_avis_by_user_id(id_utilisateur)
        avis = []
        for i in range(len(avi)):
            avis.append(
                Avis(
                    id_avis=avi[i]["id_avis"],
                    id_recette=avi[i]["id_recette"],
                    id_utilisateur=avi[i]["id_utilisateur"],
                    titre_avis=avi[i]["titre_avis"],
                    nom_auteur=avi[i]["nom_auteur"],
                    date_publication=avi[i]["date_publication"],
                    commentaire=avi[i]["commentaire"],
                    note=avi[i]["note"],
                )
            )
        if not avis:
            print("Aucune note trouvée.")
            return

        for a in avis:
            print(self._afficher_notes(a))
        return avis

    def _afficher_notes(self, avis: Avis):
        """Affiche les notes."""

        print(f"Recette: {avis.id_recette}")
        print(f"Note: {avis.note}/5")
        print("-" * 40)

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
        result = self.avis_dao.update_avis(avis_id, **kwargs)
        print(f"Avis avec ID {avis_id} mis à jour.")
        return result


if __name__ == "__main__":
    dao = AvisDAO()
    print(
        ServiceAvis(dao).ajouter_avis(
            id_recette=1,
            id_utilisateur=11,
            titre_avis="Test",
            nom_auteur="Kobe",
            date_publication=datetime.now(),
            commentaire="Bon",
            note=5,
        )
    )
    # ServiceAvis(dao).supprimer_avis(2)
    # ServiceAvis(dao).modifier_avis(avis_id=3, note=9)
    # avis1 = Avis(
    #     id_recette=1,
    #     id_utilisateur=8,
    #     titre_avis="Test",
    #     nom_auteur="Tata",
    #     date_publication=datetime.now(),
    #     commentaire="Bon",
    #     note=9,
    #     id_avis=3,
    # )
    # ServiceAvis(dao)._afficher_avis(avis1)
    # ServiceAvis(dao).afficher_avis_par_recette(1)
    ServiceAvis(dao).afficher_avis_par_utilisateur(8)
