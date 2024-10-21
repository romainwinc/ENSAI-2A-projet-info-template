from datetime import datetime
from dao.avis_dao import AvisDAO
from models.avis import Avis


class AvisService:
    def __init__(self, avis_dao):
        self.avis_dao = avis_dao

    def creer_avis(
        self, id_recette, id_utilisateur, titre_avis, nom_auteur, commentaire, note=None
    ):
        """Crée un nouvel avis et le stocke dans la base de données."""
        date_publication = datetime.now()  # Utilisation de la date actuelle
        id_avis = self.avis_dao.add_avis(
            id_recette, id_utilisateur, titre_avis, nom_auteur, date_publication, commentaire, note
        )
        return Avis(
            id_avis, titre_avis, id_utilisateur, nom_auteur, date_publication, commentaire, note
        )

    def recuperer_avis_par_recette(self, id_recette):
        """Récupère tous les avis liés à une recette spécifique."""
        avis_data = self.avis_dao.get_avis_by_recette_id(id_recette)
        return [Avis(*avis) for avis in avis_data]  # Crée une liste d'objets Avis

    def recuperer_avis_par_utilisateur(self, id_utilisateur):
        """Récupère tous les avis postés par un utilisateur spécifique."""
        avis_data = self.avis_dao.get_avis_by_user_id(id_utilisateur)
        return [Avis(*avis) for avis in avis_data]

    def modifier_avis(self, avis_id, **kwargs):
        """Modifie les attributs d'un avis existant."""
        self.avis_dao.update_avis(avis_id, **kwargs)

    def supprimer_avis(self, avis_id):
        """Supprime un avis de la base de données."""
        self.avis_dao.delete_avis(avis_id)

    def afficher_avis(self, id_recette):
        """Affiche les avis liés à une recette."""
        avis_list = self.recuperer_avis_par_recette(id_recette)
        for avis in avis_list:
            print(avis)

    def afficher_avis_utilisateur(self, id_utilisateur):
        """Affiche les avis liés à une recette."""
        avis_list = self.recuperer_avis_par_utilisateur(id_utilisateur)
        for avis in avis_list:
            print(avis)


if __name__ == "__main__":
    dao = AvisDAO()
    AvisService(dao).creer_avis(1)
