from dao import utilisateur_dao
from models import utilisateur


class UtilisateurService:
    def __init__(self, utilisateur_dao):
        self.utlisateur_dao = utilisateur_dao
