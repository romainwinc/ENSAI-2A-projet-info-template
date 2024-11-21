import unittest
from unittest.mock import MagicMock, ANY
from service.service_ingredient import ServiceIngredient
from dao.ingredient_dao import IngredientDAO
from dao.ingredients_favoris_dao import IngredientsFavorisDAO
from dao.ingredients_non_desires_dao import IngredientsNonDesiresDAO
from dao.liste_de_courses_dao import ListeDeCoursesDAO
from models.ingredient import Ingredient
from io import StringIO
import sys


class TestServiceIngredient(unittest.TestCase):
    def setUp(self):
        # Création de mocks pour les DAOs
        self.ingredient_dao_mock = MagicMock(IngredientDAO)
        self.favoris_dao_mock = MagicMock(IngredientsFavorisDAO)
        self.non_desires_dao_mock = MagicMock(IngredientsNonDesiresDAO)
        self.liste_courses_dao_mock = MagicMock(ListeDeCoursesDAO)

        # Création du service avec les DAOs mockés
        self.service_ingredient = ServiceIngredient(
            self.ingredient_dao_mock,
            self.favoris_dao_mock,
            self.non_desires_dao_mock,
            self.liste_courses_dao_mock,
        )

    def test_ajouter_ingredient(self):
        # Définir le comportement attendu du DAO
        self.ingredient_dao_mock.add_ingredient.return_value = True

        # Appeler la méthode
        self.service_ingredient.ajouter_ingredient("Tomate", "Légume rouge")

        # Vérifier que la méthode add_ingredient a été appelée avec les bons arguments
        self.ingredient_dao_mock.add_ingredient.assert_called_once_with(
            ANY  # Ignore la comparaison stricte de l'objet Ingredient
        )

    def test_afficher_ingredient(self):
        # Simuler un ingrédient renvoyé par le DAO
        self.ingredient_dao_mock.get_ingredient_by_id.return_value = {
            "id_ingredient": 1,
            "nom_ingredient": "Tomate",
            "description_ingredient": "Légume rouge",
        }

        # Appeler la méthode
        with self.assertLogs(level="INFO") as log:
            self.service_ingredient.afficher_ingredient(1)

        # Vérifier que le log contient bien l'information attendue
        self.assertIn("Ingrédient ID: 1", log.output[0])
        self.assertIn(
            "Nom: Tomate", log.output[1]
        )  # Mise à jour pour correspondre à une ligne distincte
        self.assertIn("Description: Légume rouge", log.output[2])

    def test_modifier_ingredient(self):
        # Appeler la méthode
        self.service_ingredient.modifier_ingredient(
            1, nom_ingredient="Tomate", description_ingredient="Légume rouge"
        )

        # Vérifier que la méthode update_by_ingredient_id a été appelée avec les bons arguments
        self.ingredient_dao_mock.update_by_ingredient_id.assert_called_once_with(
            1, nom_ingredient="Tomate", description_ingredient="Légume rouge"
        )

    def test_ajouter_ingredients_favoris(self):
        # Simuler que l'ingrédient n'est pas déjà dans les favoris
        self.favoris_dao_mock.is_ingredient_in_favoris.return_value = False
        self.favoris_dao_mock.add_ingredient_favori.return_value = True

        # Appeler la méthode
        result = self.service_ingredient.ajouter_ingredients_favoris(1, "Tomate")

        # Vérifier que l'ingrédient a été ajouté aux favoris
        self.assertTrue(result)
        self.favoris_dao_mock.add_ingredient_favori.assert_called_once_with("Tomate", 1)

    def test_recuperer_ingredients_favoris_utilisateur(self):
        # Simuler un retour de favoris
        self.favoris_dao_mock.get_favoris_by_user_id.return_value = ["Tomate", "Oignon"]

        # Appeler la méthode
        result = self.service_ingredient.recuperer_ingredients_favoris_utilisateur(1)

        # Vérifier que les bons favoris sont récupérés
        self.assertEqual(result, ["Tomate", "Oignon"])

    def test_supprimer_ingredients_favoris(self):
        # Appeler la méthode
        self.service_ingredient.supprimer_ingredients_favoris(1, "Tomate")

        # Vérifier que la méthode delete_ingredient_favori a été appelée avec les bons arguments
        self.favoris_dao_mock.delete_ingredient_favori.assert_called_once_with("Tomate", 1)

    def test_ajouter_ingredients_non_desires(self):
        # Simuler que l'ingrédient n'est pas déjà dans les non-désirés
        self.non_desires_dao_mock.is_ingredient_in_non_desires.return_value = False
        self.non_desires_dao_mock.add_ingredient_non_desire.return_value = True

        # Appeler la méthode
        result = self.service_ingredient.ajouter_ingredients_non_desires(1, "Tomate")

        # Vérifier que l'ingrédient a été ajouté aux non-désirés
        self.assertTrue(result)
        self.non_desires_dao_mock.add_ingredient_non_desire.assert_called_once_with("Tomate", 1)

    def test_recuperer_ingredients_non_desires_utilisateur(self):
        # Simuler un retour des ingrédients non-désirés
        self.non_desires_dao_mock.get_non_desires_by_user_id.return_value = ["Tomate", "Ail"]

        # Appeler la méthode
        result = self.service_ingredient.recuperer_ingredients_non_desires_utilisateur(1)

        # Vérifier que les bons ingrédients non-désirés sont récupérés
        self.assertEqual(result, ["Tomate", "Ail"])

    def test_supprimer_ingredients_non_desires(self):
        # Appeler la méthode
        self.service_ingredient.supprimer_ingredients_non_desires(1, "Tomate")

        # Vérifier que la méthode delete_ingredient_non_desire a été appelée avec les bons arguments
        self.non_desires_dao_mock.delete_ingredient_non_desire.assert_called_once_with("Tomate", 1)

    def test_ajouter_ingredients_liste_courses(self):
        # Simuler que l'ingrédient n'est pas déjà dans la liste de courses
        self.liste_courses_dao_mock.is_ingredient_in_liste.return_value = False
        self.liste_courses_dao_mock.add_liste_de_courses.return_value = True

        # Appeler la méthode
        result = self.service_ingredient.ajouter_ingredients_liste_courses(1, "Tomate")

        # Vérifier que l'ingrédient a été ajouté à la liste de courses
        self.assertTrue(result)
        self.liste_courses_dao_mock.add_liste_de_courses.assert_called_once_with("Tomate", 1)

    def test_afficher_ingredients_liste_courses(self):
        # Simuler un retour de liste de courses
        self.liste_courses_dao_mock.get_liste_de_courses_by_user_id.return_value = ["Tomate", "Ail"]

        # Appeler la méthode
        result = self.service_ingredient.afficher_ingredients_liste_courses(1)

        # Vérifier que les bons ingrédients de la liste de courses sont récupérés
        self.assertEqual(result, ["Tomate", "Ail"])

    def test_supprimer_ingredients_liste_courses(self):
        # Appeler la méthode
        self.service_ingredient.supprimer_ingredients_liste_courses(1, "Tomate")

        # Vérifier que la méthode delete_ingredient_from_liste_de_courses a été appelée avec les bons arguments
        self.liste_courses_dao_mock.delete_ingredient_from_liste_de_courses.assert_called_once_with(
            "Tomate", 1
        )


if __name__ == "__main__":
    unittest.main()
