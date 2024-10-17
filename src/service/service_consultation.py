from datetime import date
from dao import consultation_dao
from models import consultation


class ConsultationService:
    def __init__(self, consultation_dao):
        self.consultation_dao = consultation_dao

    def creer_consultation(self, id_recette, id_utilisateur):
        """Crée une nouvelle consultation et la stocke dans la base de données."""
        date_consultation = date.today()  # Utilise la date actuelle pour la consultation
        self.consultation_dao.add_consultation(id_recette, id_utilisateur, date_consultation)
        return Consultation(id_recette, id_utilisateur, date_consultation)

    def recuperer_consultations_par_utilisateur(self, id_utilisateur):
        """Récupère toutes les consultations d'un utilisateur spécifique."""
        consultations_data = self.consultation_dao.get_consultations_by_user_id(id_utilisateur)
        return [Consultation(*consultation) for consultation in consultations_data]

    def modifier_consultation(self, id_recette, id_utilisateur, **kwargs):
        """Modifie les attributs d'une consultation existante."""
        self.consultation_dao.update_consultation(id_recette, id_utilisateur, **kwargs)

    def supprimer_consultation(self, id_recette, id_utilisateur):
        """Supprime une consultation de la base de données."""
        self.consultation_dao.delete_consultation(id_recette, id_utilisateur)

    def afficher_consultations_utilisateur(self, id_utilisateur):
        """Affiche les consultations d'un utilisateur spécifique."""
        consultations_list = self.recuperer_consultations_par_utilisateur(id_utilisateur)
        for consultation in consultations_list:
            consultation.afficher_consultation()
