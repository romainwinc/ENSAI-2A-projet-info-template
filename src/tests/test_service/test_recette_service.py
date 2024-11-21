# import unittest
# from unittest.mock import MagicMock
# from datetime import datetime
# from models.recette import Recette
# from service.service_recette import ServiceRecette


# class TestServiceRecette(unittest.TestCase):
#     def setUp(self):
#         """
#         Setup les mocks de DAO nécessaires à chaque test.
#         """
#         self.recette_dao_mock = MagicMock()
#         self.recette_favorite_dao_mock = MagicMock()
#         self.service_recette = ServiceRecette(self.recette_dao_mock, self.recette_favorite_dao_mock)

#     def test_rechercher_par_nom_recette(self):
#         """
#         Test de la méthode rechercher_par_nom_recette.
#         when given a valid recette name,
#         then it should return a list of recipes containing the given name.
#         """
#         self.recette_dao_mock.get_all_recettes.return_value = [
#             {"nom_recette": "Apple Frangipan Tart", "liste_ingredients": ["Apple", "Tart"]},
#             {"nom_recette": "Banana Bread", "liste_ingredients": ["Banana", "Flour"]},
#         ]
#         result = self.service_recette.rechercher_par_nom_recette("Apple")
#         self.assertEqual(len(result), 1)
#         self.assertEqual(result[0].nom_recette, "Apple Frangipan Tart")

#     def test_rechercher_par_id_recette(self):
#         """
#         Test de la méthode rechercher_par_id_recette.
#         when given a valid recipe ID,
#         then it should return the recipe with the corresponding ID.
#         """
#         self.recette_dao_mock.get_recette_by_id.return_value = {
#             "nom_recette": "Apple Frangipan Tart",
#             "liste_ingredients": ["Apple", "Tart"],
#         }
#         result = self.service_recette.rechercher_par_id_recette(1)
#         self.assertIsNotNone(result)
#         self.assertEqual(result[0].nom_recette, "Apple Frangipan Tart")

#     def test_rechercher_par_ingredient(self):
#         """
#         Test de la méthode rechercher_par_ingredient.
#         when given an ingredient name,
#         then it should return a list of recipes that contain the given ingredient.
#         """
#         self.recette_dao_mock.get_all_recettes.return_value = [
#             {"nom_recette": "Apple Frangipan Tart", "liste_ingredients": ["Apple", "Tart"]},
#             {"nom_recette": "Banana Bread", "liste_ingredients": ["Banana", "Flour"]},
#         ]
#         result = self.service_recette.rechercher_par_ingredient("Apple")
#         self.assertEqual(len(result), 1)
#         self.assertEqual(result[0].nom_recette, "Apple Frangipan Tart")

#     def test_creer_recette(self):
#         """
#         Test de la méthode creer_recette.
#         when given valid recipe details,
#         then it should create a new recipe and return its ID.
#         """
#         self.recette_dao_mock.add_recette.return_value = 1
#         recette_id = self.service_recette.creer_recette(
#             "Exemple Recette",
#             "Dessert",
#             "British",
#             "Touiller / Remuer / Mélanger",
#             ["Butter", "Jam"],
#         )
#         self.assertEqual(recette_id, 1)

#     def test_modifier_recette_id(self):
#         """
#         Test de la méthode modifier_recette_id.
#         when given a valid recipe ID and new parameters,
#         then it should update the recipe and return True.
#         """
#         self.recette_dao_mock.get_recette_by_id.return_value = {
#             "nom_recette": "Apple Frangipan Tart",
#             "liste_ingredients": ["Apple", "Tart"],
#         }
#         self.recette_dao_mock.update_by_recette_id.return_value = True
#         result = self.service_recette.modifier_recette_id(1, nom_recette="Tarte Crème")
#         self.assertTrue(result)

#     def test_supprimer_recette(self):
#         """
#         Test de la méthode supprimer_recette.
#         when given a valid recipe ID,
#         then it should delete the recipe and return True.
#         """
#         self.recette_dao_mock.get_recette_by_id.return_value = {
#             "nom_recette": "Apple Frangipan Tart",
#             "liste_ingredients": ["Apple", "Tart"],
#         }
#         self.recette_dao_mock.delete_recette.return_value = True
#         result = self.service_recette.supprimer_recette(1)
#         self.assertTrue(result)

#     def test_ajouter_recette_favorite(self):
#         """
#         Test de la méthode ajouter_recette_favorite.
#         when given a valid recette name and user ID,
#         then it should add the recipe to the user's favorites.
#         """
#         self.recette_favorite_dao_mock.is_recette_in_favoris.return_value = False
#         result = self.service_recette.ajouter_recette_favorite("Apple Frangipan Tart", 2)
#         self.assertTrue(result)

#     def test_supprimer_recette_favorite(self):
#         """
#         Test de la méthode supprimer_recette_favorite.
#         when given a valid recette name and user ID,
#         then it should remove the recipe from the user's favorites.
#         """
#         self.recette_favorite_dao_mock.delete_recette_favorite.return_value = True
#         result = self.service_recette.supprimer_recette_favorite("Apple Frangipan Tart", 2)
#         self.assertIsNone(result)  # On ne renvoie rien après suppression

#     def test_afficher_recettes_favorites(self):
#         """
#         Test de la méthode afficher_recettes_favorites.
#         when given a valid user ID,
#         then it should return a list of the user's favorite recipes.
#         """
#         self.recette_favorite_dao_mock.get_favoris_by_user_id.return_value = [
#             "Apple Frangipan Tart"
#         ]
#         result = self.service_recette.afficher_recettes_favorites(2)
#         self.assertEqual(result, ["Apple Frangipan Tart"])


# if __name__ == "__main__":
#     unittest.main()
# if __name__ == "__main__":
#     unittest.main()
