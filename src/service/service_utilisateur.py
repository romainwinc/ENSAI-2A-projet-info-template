from dao.utilisateur_dao import UtilisateurDao
from models.utilisateur import Utilisateur
from datetime import datetime


class ServiceUtilisateur:
    def __init__(self, utilisateur_dao):
        self.utilisateur_dao = utilisateur_dao

    def creer_utilisateur(self, nom, mdp) -> Utilisateur:
        """Crée un nouvel utilisateur et le stocke dans la base de données."""
        if not utilisateur.mot_de_passe:  # Vérifie si le mot de passe est vide
            raise ValueError("Le mot de passe ne peut pas être vide.")

        grade = "Connecté"
        date_inscrit = datetime.now()
        nouvel_utilisateur = Utilisateur(
            nom_utilisateur=nom, mot_de_passe=mdp, role=grade, date_inscription=date_inscrit
        )
        return nouvel_utilisateur if UtilisateurDao().add_user(nouvel_utilisateur) else None

    def changer_role_utilisateur(self, id_utilisateur: str, new_role: str):
        """Change le role d'un utilisateur"""
        self.utilisateur_dao.update_user(id_utilisateur, new_role)

    def supprimer_utilisateur(self, id_utilisateur):
        """Supprime un compte utilisateur"""
        self.utilisateur_dao.delete_user(id_utilisateur)

    def demande_de_changement_de_role(self, id_utilisateur: str, dde_role: str):
        return None  # la fonction n'est pas encore créer car il manque des attribus pour pouvoir la faire


if __name__ == "__main__":
    dao = UtilisateurDao()
    try:
        utilisateur = Utilisateur(
            nom_utilisateur="Antoine_Dupont",
            mot_de_passe="Totolebest",
            id_utilisateur=None,
            role="Connecté",
        )
        ServiceUtilisateur(dao).creer_utilisateur(
            utilisateur.nom_utilisateur, utilisateur.mot_de_passe
        )
    except ValueError as e:
        print(e)

    # ServiceUtilisateur(dao).changer_role_utilisateur(utilisateur, "Admin")
