from dao.utilisateur_dao import UtilisateurDao
from models.utilisateur import Utilisateur
from datetime import datetime
from models.utilisateur import Utilisateur


class ServiceUtilisateur:
    def __init__(self, utilisateur_dao):
        self.utilisateur_dao = utilisateur_dao

    def creer_utilisateur(self, utilisateur: Utilisateur):
        """Crée un nouvel utilisateuret le stock dans la base de donnée"""
        grade = "Connecté"
        date_inscrit = datetime.now()
        id_utilisateur = self.utilisateur_dao.add_user(
            utilisateur.id_utilisateur, utilisateur.nom_utilisateur, utilisateur.mot_de_passe
        )
        return Utilisateur(
            id_utilisateur,
            utilisateur.nom_utilisateur,
            utilisateur.mot_de_passe,
            grade,
            date_inscrit,
        )


if __name__ == "__main__":
    dao = UtilisateurDao()
    ServiceUtilisateur(dao).creer_utilisateur("Antoine_Dupont", "Totolebest")
