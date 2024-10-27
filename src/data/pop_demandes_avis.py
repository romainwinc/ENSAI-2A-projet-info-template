from dao.demande_dao import DemandeDAO
from dao.avis_dao import AvisDAO
from models.avis import Avis
from models.demande import Demande
from service.service_avis import ServiceAvis
from service.service_demande import ServiceDemande


try:
    # ingredient_dao = IngredientDAO()
    # favoris_dao = IngredientsFavorisDAO()
    # non_desires_dao = IngredientsNonDesiresDAO()
    # liste_courses_dao = ListeDeCoursesDAO()

    # service = ServiceIngredient(ingredient_dao, favoris_dao, non_desires_dao, liste_courses_dao)

    print("---- Initialisation des Demandes et Avis terminée ----")

except ValueError as e:
    print(e)
