from dao import recette_dao_dao
from models import recette

class RecetteService:
    def __init__(self, recette_dao):
        self.recette_dao = recette_dao

    def 