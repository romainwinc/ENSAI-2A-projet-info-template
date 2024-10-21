from dao.utilisateur_dao import UtilisateurDao
from models.utilisateur import Utilisateur
from datetime import datetime

class ServiceUtilisateur:
    def __init__(self, utilisateur_dao):
        self.utilisateur_dao = utilisateur_dao

    def creer_utilisateur(
        self, nom_utilisateur, mot_de_passe,
    ):
        """ Crée un nouvel utilisateuret le stock dans la base de donnée"""
        date_inscrit = datetime.now()
        id_utilisateur = self.utilisateur_dao.add_user()
        return Utilisateur(
            id_utilisateur, nom_utilisateur, mot_de_passe, role= "Non connecté" ,date_inscrit, ingredients_favoris, recette_favorite,liste_course,liste_ingredient_favori,liste_ingredient_non_desires
        )


if __name__ == "__main__":
    dao = UtilisateurDao()
    S(dao).rechercher_par_id_recette(1)
