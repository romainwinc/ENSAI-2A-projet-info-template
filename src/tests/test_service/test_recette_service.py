import unittest
from unittest.mock import MagicMock
from service.service_recette import ServiceRecette
from models.recette import Recette


class TestServiceRecette(unittest.TestCase):
    def setUp(self):
        # Création d'un mock pour RecetteDAO
        self.recette_dao_mock = MagicMock()
        self.service_recette = ServiceRecette(self.recette_dao_mock)

    def test_rechercher_par_nom_recette(self):
        # Configuration des données de test
        self.recette_dao_mock.get_all_recettes.return_value = [
            {"nom_recette": "Tarte aux pommes"},
            {"nom_recette": "Tarte aux cerises"},
        ]

        result = self.service_recette.rechercher_par_nom_recette("Tarte aux pommes")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].nom_recette, "Tarte aux pommes")

    def test_rechercher_par_id_recette(self):
        # Configuration des données de test
        self.recette_dao_mock.get_recette_by_id.return_value = {
            "nom_recette": "Tarte aux pommes",
            "id_recette": 1,
        }

        result = self.service_recette.rechercher_par_id_recette(1)
        self.assertIsNotNone(result)
        self.assertEqual(result.nom_recette, "Tarte aux pommes")

    def test_rechercher_par_ingredient(self):
        # Configuration des données de test
        self.recette_dao_mock.get_all_recettes.return_value = [
            {"nom_recette": "Tarte aux pommes", "liste_ingredients": ["Pommes", "Farine"]},
            {"nom_recette": "Gâteau au chocolat", "liste_ingredients": ["Chocolat", "Farine"]},
        ]

        result = self.service_recette.rechercher_par_ingredient("Pommes")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].nom_recette, "Tarte aux pommes")

    def test_creer_recette(self):
        # Configuration des données de test
        self.recette_dao_mock.add_recette.return_value = 1  # Simule l'ID retourné

        recette_id = self.service_recette.creer_recette(
            "Exemple Recette", "Dessert", "British", "Instructions", ["Ingrédient 1"]
        )
        self.assertEqual(recette_id, 1)
        self.recette_dao_mock.add_recette.assert_called_once()

    def test_modifier_recette(self):
        # Configuration des données de test
        self.recette_dao_mock.get_recette_by_id.return_value = {"nom_recette": "Tarte aux pommes"}

        result = self.service_recette.modifier_recette(1, nom_recette="Tarte aux poires")
        self.assertTrue(result)
        self.recette_dao_mock.update_recette.assert_called_once_with(
            1, nom_recette="Tarte aux poires"
        )

    def test_supprimer_recette(self):
        # Configuration des données de test
        self.recette_dao_mock.get_recette_by_id.return_value = {"nom_recette": "Tarte aux pommes"}

        result = self.service_recette.supprimer_recette(1)
        self.assertTrue(result)
        self.recette_dao_mock.delete_recette.assert_called_once_with(1)

    def test_afficher_recette(self):
        # Configuration des données de test
        self.recette_dao_mock.get_recette_by_id.return_value = {
            "id_recette": 1,
            "nom_recette": "Tarte aux pommes",
        }

        result = self.service_recette.afficher_recette(1)
        self.assertIn("Tarte aux pommes", result)

    def test_afficher_recette_non_trouvee(self):
        # Configuration des données de test
        self.recette_dao_mock.get_recette_by_id.return_value = None

        result = self.service_recette.afficher_recette(999)
        self.assertEqual(result, "Aucune recette trouvée avec l'ID 999.")


if __name__ == "__main__":
    unittest.main()
