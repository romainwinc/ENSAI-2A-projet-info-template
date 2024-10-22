from dao.utilisateur_dao import UtilisateurDao
from models.utilisateur import Utilisateur
from datetime import datetime
from utils.securite import hash_password


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

    def se_connecter(self, pseudo, mdp) -> Utilisateur:
        """Se connecter à partir de pseudo et mdp"""
        return UtilisateurDao().se_connecter(pseudo, hash_password(mdp, pseudo))


if __name__ == "__main__":
    dao = UtilisateurDao()
    try:
        utilisateur = Utilisateur(
            nom_utilisateur="Antoine_Dupont",
            mot_de_passe="Totolebest",
            id_utilisateur=None,
            role="Connecté",
        )
        utilisateur2 = Utilisateur(
            nom_utilisateur="Jean", mot_de_passe="123", id_utilisateur=None, role="Professionel"
        )
        # ServiceUtilisateur(dao).creer_utilisateur(utilisateur2.nom_utilisateur, utilisateur2.mot_de_passe)
    except ValueError as e:
        print(e)

    def nom_utilisateur_deja_utilise(self, nom_utilisateur) -> bool:
        """Vérifie si le nom d'utilisateur est déjà utilisé
        Retourne True si le nom d'utilisateur existe déjà en BDD"""
        utilisateurs = UtilisateurDao().lister_tous()
        return utilisateur in [u.nom_utilisateur for u in utilisateurs]

    utilisateur = Utilisateur(
        nom_utilisateur="Antoine_Dupont",
        mot_de_passe="Totolebest",
        id_utilisateur=1,
        role="Connecté",
    )
    # ServiceUtilisateur(dao).changer_role_utilisateur(utilisateur.id_utilisateur, new_role="Admin")
    # ServiceUtilisateur(dao).supprimer_utilisateur(1)
