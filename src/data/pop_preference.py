from dao.ingredient_dao import IngredientDAO
from dao.ingredients_favoris_dao import IngredientsFavorisDAO
from dao.ingredients_non_desires_dao import IngredientsNonDesiresDAO
from dao.liste_de_courses_dao import ListeDeCoursesDAO
from dao.recette_dao import RecetteDAO
from dao.recette_favorite_dao import RecetteFavoriteDAO
from models.recette import Recette
from models.ingredient import Ingredient
from service.service_ingredient import ServiceIngredient
from service.service_recette import ServiceRecette


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

    # Maintenant lkes préférences des recettes

    # Instanciation des DAOs
    recette_dao = RecetteDAO()
    recette_favorite_dao = RecetteFavoriteDAO()

    # Instanciation du service
    service_recette = ServiceRecette(recette_dao, recette_favorite_dao)

    # Ajout de recettes favorites pour chaque utilisateur
    for i in range(1, 7):
        print("utilisateur")
        print(i)
        # Ajout de trois recettes favorites pour chaque utilisateur
        service_recette.ajouter_recette_favorite("Apple Frangipan Tart", i)
        service_recette.ajouter_recette_favorite("Chicken Basquaise", i)
        service_recette.ajouter_recette_favorite("Chicken Parmentier", i)

    print("---- Initialisation des Préferences terminée ----")

except ValueError as e:
    print(e)
