from dao.utilisateur_dao import UtilisateurDao
from models import utilisateur


if __name__ == "__main__":
    dao = UtilisateurDao()
    ServiceRecette(dao).rechercher_par_id_recette(1)
