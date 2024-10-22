from dao.utilisateur_dao import UtilisateurDao
from models.utilisateur import Utilisateur
from datetime import datetime


class ServiceUtilisateur:
    def __init__(self, utilisateur_dao):
        self.utilisateur_dao = utilisateur_dao

    def creer_utilisateur(self, utilisateur: Utilisateur):
        """Crée un nouvel utilisateur et le stocke dans la base de données."""
        if not utilisateur.mot_de_passe:  # Vérifie si le mot de passe est vide
            raise ValueError("Le mot de passe ne peut pas être vide.")

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
    try:
        utilisateur = Utilisateur(
            id_utilisateur=None,  # ID sera généré par la base de données
            nom_utilisateur="Antoine_Dupont",
            mot_de_passe="",  # Mot de passe vide pour tester la validation
            role="Connecté",  # Ceci devrait être géré dans le service
            date_inscription=datetime.now(),
        )
        ServiceUtilisateur(dao).creer_utilisateur(utilisateur)
    except ValueError as e:
        print(e)
