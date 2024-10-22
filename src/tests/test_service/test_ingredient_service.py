import unittest
from unittest.mock import MagicMock
from service.service_ingredient import IngredientService
from dao.ingredient_dao import IngredientDAO


class TestIngredientService(unittest.TestCase):

    def setUp(self):
        # Créer une instance de IngredientService avec des mocks de DAO
        self.ingredients_non_desires_dao = MagicMock()
        self.ingredients_favoris_dao = MagicMock()
        self.service = IngredientService(
            self.ingredients_non_desires_dao, self.ingredients_favoris_dao
        )

    def test_recuperer_ingredients_non_desires_utilisateur(self):
        # Cas où l'utilisateur n'a pas d'ingrédients non-désirés
        self.ingredients_non_desires_dao.get_non_desires_by_user_id.return_value = []
        with self.assertLogs("service.service_ingredient", level="INFO") as log:
            self.service.recuperer_ingredients_non_desires_utilisateur(1)
            self.assertIn("Vous n'avez aucun ingrédient non-désiré.", log.output[0])

        # Cas où l'utilisateur a des ingrédients non-désirés
        ingr_mock_1 = MagicMock(nom="Tomate")
        ingr_mock_2 = MagicMock(nom="Oignon")
        self.ingredients_non_desires_dao.get_non_desires_by_user_id.return_value = [
            ingr_mock_1,
            ingr_mock_2,
        ]
        with self.assertLogs("service.service_ingredient", level="INFO") as log:
            self.service.recuperer_ingredients_non_desires_utilisateur(1)
            self.assertIn("Voici vos ingrédients non-désirés :", log.output[0])

    def test_recuperer_ingredients_favoris_utilisateur(self):
        # Cas où l'utilisateur n'a pas d'ingrédients favoris
        self.ingredients_favoris_dao.get_favoris_by_user_id.return_value = []
        with self.assertLogs("service.service_ingredient", level="INFO") as log:
            self.service.recuperer_ingredients_favoris_utilisateur(1)
            self.assertIn("Vous n'avez aucun ingrédient favoris.", log.output[0])

        # Cas où l'utilisateur a des ingrédients favoris
        ingr_fav_mock_1 = MagicMock(nom="Basilic")
        ingr_fav_mock_2 = MagicMock(nom="Persil")
        self.ingredients_favoris_dao.get_favoris_by_user_id.return_value = [
            ingr_fav_mock_1,
            ingr_fav_mock_2,
        ]
        with self.assertLogs("service.service_ingredient", level="INFO") as log:
            self.service.recuperer_ingredients_favoris_utilisateur(1)
            self.assertIn("Voici vos ingrédients favoris :", log.output[0])

    def test_supprimer_ingredients_non_desires(self):
        # Tester la suppression d'un ingrédient non-désiré
        self.ingredients_non_desires_dao.delete_non_desire.return_value = True
        with self.assertLogs("service.service_ingredient", level="INFO") as log:
            self.service.supprimer_ingredients_non_desires(1, 123)
            self.assertIn("L'ingrédient non-désiré avec l'ID 123 a été supprimé.", log.output[0])

        # Tester la suppression échouée
        self.ingredients_non_desires_dao.delete_non_desire.return_value = False
        with self.assertLogs("service.service_ingredient", level="INFO") as log:
            self.service.supprimer_ingredients_non_desires(1, 123)
            self.assertIn(
                "Erreur lors de la suppression de l'ingrédient non-désiré.", log.output[0]
            )

    def test_supprimer_ingredients_favoris(self):
        # Tester la suppression d'un ingrédient favori
        self.ingredients_favoris_dao.delete_favori.return_value = True
        with self.assertLogs("service.service_ingredient", level="INFO") as log:
            self.service.supprimer_ingredients_favoris(1, 456)
            self.assertIn("L'ingrédient favori avec l'ID 456 a été supprimé.", log.output[0])

        # Tester la suppression échouée
        self.ingredients_favoris_dao.delete_favori.return_value = False
        with self.assertLogs("service.service_ingredient", level="INFO") as log:
            self.service.supprimer_ingredients_favoris(1, 456)
            self.assertIn("Erreur lors de la suppression de l'ingrédient favori.", log.output[0])

    def test_ajouter_ingredients_non_desires(self):
        # Tester l'ajout d'un ingrédient non-désiré
        self.ingredients_non_desires_dao.add_ingredient_non_desire.return_value = True
        with self.assertLogs("service.service_ingredient", level="INFO") as log:
            self.service.ajouter_ingredients_non_desires(1, 789)
            self.assertIn("L'ingrédient non-désiré avec l'ID 789 a été ajouté.", log.output[0])

        # Tester l'ajout échoué
        self.ingredients_non_desires_dao.add_ingredient_non_desire.return_value = False
        with self.assertLogs("service.service_ingredient", level="INFO") as log:
            self.service.ajouter_ingredients_non_desires(1, 789)
            self.assertIn("Erreur lors de l'ajout de l'ingrédient non-désiré.", log.output[0])

    def test_ajouter_ingredients_favoris(self):
        # Tester l'ajout d'un ingrédient favori
        self.ingredients_favoris_dao.add_ingredient_favori.return_value = True
        with self.assertLogs("service.service_ingredient", level="INFO") as log:
            self.service.ajouter_ingredients_favoris(1, 321)
            self.assertIn("L'ingrédient favori avec l'ID 321 a été ajouté.", log.output[0])

        # Tester l'ajout échoué
        self.ingredients_favoris_dao.add_ingredient_favori.return_value = False
        with self.assertLogs("service.service_ingredient", level="INFO") as log:
            self.service.ajouter_ingredients_favoris(1, 321)
            self.assertIn("Erreur lors de l'ajout de l'ingrédient favori.", log.output[0])


if __name__ == "__main__":
    unittest.main()
