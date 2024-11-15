from dao.consultation_dao import ConsultationDAO
from models.consultation import Consultation
from datetime import date


class ServiceConsultation:
    def __init__(self, consultation_dao: ConsultationDAO):
        self.consultation_dao = consultation_dao

    def creer_consultation(
        self, id_recette: int, id_utilisateur: int, date_consultation: date
    ) -> Consultation:
        """
        Crée une nouvelle consultation et la retourne.
        """
        self.consultation_dao.add_consultation(id_recette, id_utilisateur, date_consultation)
        return Consultation(id_recette, id_utilisateur, date_consultation)

    def recuperer_consultation(self, id_recette: int, id_utilisateur: int) -> Consultation | None:
        """
        Récupère une consultation par ID recette et ID utilisateur.
        """
        consultation_data = self.consultation_dao.get_consultation(id_recette, id_utilisateur)
        if consultation_data:
            return Consultation(**consultation_data)
        return None

    def rechercher_consultations_par_utilisateur(self, id_utilisateur: int) -> list[Consultation]:
        """
        Récupère toutes les consultations d'un utilisateur donné en utilisant le DAO.
        """
        consultations_data = self.consultation_dao.get_consultations_by_utilisateur(id_utilisateur)
        return [Consultation(**data) for data in consultations_data]

    def supprimer_consultation(self, id_recette: int, id_utilisateur: int) -> bool:
        """
        Supprime une consultation par son ID recette et ID utilisateur.
        """
        consultation_existante = self.consultation_dao.get_consultation(id_recette, id_utilisateur)
        if not consultation_existante:
            print(
                f"Consultation non trouvée pour Recette ID {id_recette} "
                f"et Utilisateur ID {id_utilisateur}."
            )
            return False
        self.consultation_dao.delete_consultation(id_recette, id_utilisateur)
        print(
            f"Consultation pour Recette ID {id_recette} et Utilisateur "
            f"ID {id_utilisateur} supprimée."
        )
        return True

    def afficher_consultation(self, id_recette: int, id_utilisateur: int) -> str:
        """
        Affiche une consultation formatée par ID recette et ID utilisateur.
        """
        consultation = self.recuperer_consultation(id_recette, id_utilisateur)
        if consultation:
            return consultation.__str__()
        return (
            f"Aucune consultation trouvée pour Recette ID {id_recette} "
            f"et Utilisateur ID {id_utilisateur}."
        )

    def afficher_consultations_par_utilisateur(self, id_utilisateur: int) -> list[str]:
        """
        Affiche toutes les consultations d'un utilisateur donné, formatées.
        """
        consultations = self.rechercher_consultations_par_utilisateur(id_utilisateur)
        if consultations:
            return [consultation.__str__() for consultation in consultations]
        return [f"Aucune consultation trouvée pour l'utilisateur {id_utilisateur}."]


if __name__ == "__main__":
    dao = ConsultationDAO()
    pass
    # Exemple de test des méthodes de ServiceConsultation (à décommenter pour tester)
    # print(ServiceConsultation(dao).creer_consultation(1, 1, date(2024, 1, 1)))
    # print(ServiceConsultation(dao).afficher_consultation(1, 1))
    # print(ServiceConsultation(dao).afficher_consultations_par_utilisateur(1))
