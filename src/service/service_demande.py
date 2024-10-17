from dao import demande_dao
from models import demande


class DemandeService:
    def __init__(self, demande_dao):
        self.demande_dao = demande_dao

    def creer_demande(
        self, id_utilisateur, type_demande, attribut_modifie, attribut_corrige, commentaire_demande
    ):
        """Crée une nouvelle demande et la stocke dans la base de données."""
        id_demande = self.demande_dao.add_demande(
            id_utilisateur, type_demande, attribut_modifie, attribut_corrige, commentaire_demande
        )
        return Demande(
            id_demande,
            id_utilisateur,
            type_demande,
            attribut_modifie,
            attribut_corrige,
            commentaire_demande,
        )

    def recuperer_demande(self, demande_id):
        """Récupère une demande par son ID."""
        demande_data = self.demande_dao.get_demande_by_id(demande_id)
        if demande_data:
            return Demande(*demande_data)
        return None

    def modifier_demande(self, demande_id, **kwargs):
        """Modifie les attributs d'une demande existante."""
        self.demande_dao.update_demande(demande_id, **kwargs)

    def supprimer_demande(self, demande_id):
        """Supprime une demande de la base de données."""
        self.demande_dao.delete_demande(demande_id)

    def afficher_demande(self, demande_id):
        """Affiche les détails d'une demande."""
        demande = self.recuperer_demande(demande_id)
        if demande:
            demande.afficher_demande()
        else:
            print("Demande non trouvée.")
