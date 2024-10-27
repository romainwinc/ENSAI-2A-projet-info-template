from dao.ingredient_dao import IngredientDAO
from dao.ingredients_favoris_dao import IngredientsFavorisDAO
from dao.ingredients_non_desires_dao import IngredientsNonDesiresDAO
from dao.liste_de_courses_dao import ListeDeCoursesDAO
from models.ingredient import Ingredient
from service.service_ingredient import ServiceIngredient


try:
    ingredient_dao = IngredientDAO()
    favoris_dao = IngredientsFavorisDAO()
    non_desires_dao = IngredientsNonDesiresDAO()
    liste_courses_dao = ListeDeCoursesDAO()

    service = ServiceIngredient(ingredient_dao, favoris_dao, non_desires_dao, liste_courses_dao)

    for i in range(1, 7):
        print("utilisateur")
        print(i)
        service.ajouter_ingredients_favoris(i, "Chicken")
        service.ajouter_ingredients_favoris(i, "Rice")
        service.ajouter_ingredients_non_desires(i, "Peanuts")
        service.ajouter_ingredients_non_desires(i, "Peas")
        service.ajouter_ingredients_liste_courses(i, "Beef")
        service.ajouter_ingredients_liste_courses(i, "Lettuce")

    print("---- Initialisation des Préferences terminée ----")

except ValueError as e:
    print(e)
