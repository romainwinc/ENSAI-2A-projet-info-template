# import unittest
# from unittest.mock import Mock, patch
# from models.ingredient import Ingredient
# from service.service_ingredient import ServiceIngredient


# class TestServiceIngredient(unittest.TestCase):
#     def setUp(self):
#         # Given: Initialisation des mocks pour les DAOs
#         self.ingredient_dao = Mock()
#         self.favoris_dao = Mock()
#         self.non_desires_dao = Mock()
#         self.liste_courses_dao = Mock()

#         # Given: Initialisation du service avec les DAOs mockés
#         self.service = ServiceIngredient(
#             self.ingredient_dao,
#             self.favoris_dao,
#             self.non_desires_dao,
#             self.liste_courses_dao,
#         )

#     def test_ajouter_ingredient(self):
#         # Given: Un ingrédient à ajouter
#         self.ingredient_dao.add_ingredient.return_value = True
#         ingredient_nom = "Tomate"
#         ingredient_description = "Légume rouge et juteux"

#         # When: L'ingrédient est ajouté via le service
#         self.service.ajouter_ingredient(ingredient_nom, ingredient_description)

#         # Then: Vérifier que la méthode add_ingredient a été appelée avec le bon ingrédient
#         self.ingredient_dao.add_ingredient.assert_called_once_with(
#             Ingredient(
#                 id_ingredient=None,
#                 nom_ingredient=ingredient_nom,
#                 description_ingredient=ingredient_description,
#             )
#         )

#     @patch("builtins.print")  # Cela permet de capturer les appels à print()
#     def test_afficher_ingredient_found(self, mock_print):
#         # Given: Un ingrédient avec l'ID 1 dans la base de données mockée
#         self.ingredient_dao.get_ingredient_by_id.return_value = {
#             "id_ingredient": 1,
#             "nom_ingredient": "Chicken",
#             "description_ingredient": "The chicken is a type of domesticated fowl, ...",
#         }

#         # When: La méthode afficher_ingredient est appelée pour l'ID 1
#         result = self.service.afficher_ingredient(1)

#         # Then: Vérifier que get_ingredient_by_id a été appelé
#         self.ingredient_dao.get_ingredient_by_id.assert_called_once_with(1)

#         # Vérifier que la méthode print() a bien été appelée avec les bonnes informations
#         mock_print.assert_called_with(
#             "Ingrédient ID: 1\nNom: Chicken\nDescription: The chicken is a type of domesticated fowl, ..."
#         )

#         # Vérifier que la méthode retourne bien les données sous forme de dictionnaire
#         self.assertEqual(result["nom_ingredient"], "Chicken")
#         self.assertTrue(result["description_ingredient"].startswith("The chicken"))

#     def test_afficher_ingredient_not_found(self):
#         # Given: Aucun ingrédient avec l'ID 99 dans la base de données mockée
#         self.ingredient_dao.get_ingredient_by_id.return_value = None

#         # When: La méthode afficher_ingredient est appelée pour l'ID 99
#         result = self.service.afficher_ingredient(99)

#         # Then: Vérifier que get_ingredient_by_id a été appelé et que le résultat est None
#         self.ingredient_dao.get_ingredient_by_id.assert_called_once_with(99)
#         self.assertIsNone(result)

#     def test_modifier_ingredient(self):
#         # Given: Un ingrédient à modifier (ID 1)
#         ingredient_id = 1
#         ingredient_nom = "Carotte"
#         ingredient_description = "Orange et croquant"

#         # When: Modifier l'ingrédient via le service
#         self.service.modifier_ingredient(
#             ingredient_id,
#             nom_ingredient=ingredient_nom,
#             description_ingredient=ingredient_description,
#         )

#         # Then: Vérifier que update_by_ingredient_id a été appelée avec les bons paramètres
#         self.ingredient_dao.update_by_ingredient_id.assert_called_once_with(
#             ingredient_id,
#             nom_ingredient=ingredient_nom,
#             description_ingredient=ingredient_description,
#         )

#     def test_rechercher_par_nom_ingredient(self):
#         # Given: Des ingrédients existants dans la base de données mockée
#         self.ingredient_dao.get_all_ingredients.return_value = [
#             {"id_ingredient": 1, "nom_ingredient": "Tomate", "description_ingredient": "Rouge"},
#             {"id_ingredient": 2, "nom_ingredient": "Pomme", "description_ingredient": "Fruit"},
#         ]

#         # When: La méthode rechercher_par_nom_ingredient est appelée avec "tom"
#         result = self.service.rechercher_par_nom_ingredient("tom")

#         # Then: Vérifier que get_all_ingredients a été appelée et que le résultat est correct
#         self.ingredient_dao.get_all_ingredients.assert_called_once()
#         self.assertEqual(len(result), 1)
#         self.assertEqual(result[0].nom_ingredient, "Tomate")

#     def test_ajouter_ingredients_favoris(self):
#         # Given: Un utilisateur et un ingrédient à ajouter aux favoris
#         utilisateur_id = 1
#         nom_ingredient = "Tomate"

#         # When: L'ingrédient est ajouté aux favoris
#         self.service.ajouter_ingredients_favoris(utilisateur_id, nom_ingredient)

#         # Then: Vérifier que add_ingredient_favori a été appelée avec les bons paramètres
#         self.favoris_dao.add_ingredient_favori.assert_called_once_with(
#             nom_ingredient, utilisateur_id
#         )

#     def test_recuperer_ingredients_favoris_utilisateur(self):
#         # Given: Des ingrédients favoris pour un utilisateur
#         self.favoris_dao.get_favoris_by_user_id.return_value = ["Tomate", "Pomme"]

#         # When: La méthode pour récupérer les favoris est appelée
#         result = self.service.recuperer_ingredients_favoris_utilisateur(1)

#         # Then: Vérifier que get_favoris_by_user_id a été appelée et que le résultat est correct
#         self.favoris_dao.get_favoris_by_user_id.assert_called_once_with(1)
#         self.assertEqual(result, ["Tomate", "Pomme"])

#     def test_supprimer_ingredients_favoris(self):
#         # Given: Un utilisateur et un ingrédient à supprimer des favoris
#         utilisateur_id = 1
#         nom_ingredient = "Tomate"

#         # When: L'ingrédient est supprimé des favoris
#         self.service.supprimer_ingredients_favoris(utilisateur_id, nom_ingredient)

#         # Then: Vérifier que delete_ingredient_favori a été appelée avec les bons paramètres
#         self.favoris_dao.delete_ingredient_favori.assert_called_once_with(
#             nom_ingredient, utilisateur_id
#         )

#     def test_ajouter_ingredients_liste_courses(self):
#         # Given: Un utilisateur et un ingrédient à ajouter à la liste de courses
#         utilisateur_id = 1
#         nom_ingredient = "Tomate"

#         # When: L'ingrédient est ajouté à la liste de courses
#         self.service.ajouter_ingredients_liste_courses(utilisateur_id, nom_ingredient)

#         # Then: Vérifier que add_liste_de_courses a été appelée avec les bons paramètres
#         self.liste_courses_dao.add_liste_de_courses.assert_called_once_with(
#             nom_ingredient, utilisateur_id
#         )

#     def test_afficher_ingredients_liste_courses(self):
#         # Given: Une liste d'ingrédients dans la liste de courses d'un utilisateur
#         self.liste_courses_dao.get_liste_de_courses_by_user_id.return_value = ["Tomate", "Pomme"]

#         # When: La méthode pour afficher la liste de courses est appelée
#         result = self.service.afficher_ingredients_liste_courses(1)

#         # Then: Vérifier que get_liste_de_courses_by_user_id a été appelée et que le résultat est correct
#         self.liste_courses_dao.get_liste_de_courses_by_user_id.assert_called_once_with(1)
#         self.assertEqual(result, ["Tomate", "Pomme"])

#     def test_supprimer_ingredients_liste_courses(self):
#         # Given: Un utilisateur et un ingrédient à supprimer de la liste de courses
#         utilisateur_id = 1
#         nom_ingredient = "Tomate"

#         # When: L'ingrédient est supprimé de la liste de courses
#         self.service.supprimer_ingredients_liste_courses(utilisateur_id, nom_ingredient)

#         # Then: Vérifier que delete_ingredient_from_liste_de_courses a été appelée avec les bons paramètres
#         self.liste_courses_dao.delete_ingredient_from_liste_de_courses.assert_called_once_with(
#             nom_ingredient, utilisateur_id
#         )


# if __name__ == "__main__":
#     unittest.main()
