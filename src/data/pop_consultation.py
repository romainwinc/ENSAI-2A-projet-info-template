from dao.consultation_dao import ConsultationDAO
from models.consultation import Consultation
from service.consultation import ServiceConsultation


try:
    # ingredient_dao = IngredientDAO()
    # favoris_dao = IngredientsFavorisDAO()
    # non_desires_dao = IngredientsNonDesiresDAO()
    # liste_courses_dao = ListeDeCoursesDAO()

    # service = ServiceIngredient(ingredient_dao, favoris_dao, non_desires_dao, liste_courses_dao)

    print("---- Initialisation des Consultations terminée ----")

except ValueError as e:
    print(e)
