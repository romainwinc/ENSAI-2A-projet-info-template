import unittest
from unittest.mock import MagicMock
from models.recette import Recette
from service.service_recette import ServiceRecette


class TestServiceRecette(unittest.TestCase):
    def setUp(self):
        """
        Setup des mocks de DAO nécessaires à chaque test.
        """
        self.recette_dao_mock = MagicMock()
        self.recette_favorite_dao_mock = MagicMock()
        self.service_recette = ServiceRecette(self.recette_dao_mock, self.recette_favorite_dao_mock)

    def test_rechercher_par_nom_recette(self):
        """
        Test de la méthode rechercher_par_nom_recette.
        """
        self.recette_dao_mock.get_all_recettes.return_value = [
            {
                "id_recette": 1,
                "nom_recette": "Apple Frangipan Tart",
                "categorie": "Dessert",
                "origine": "French",
                "liste_ingredients": ["Apple", "Tart"],
                "instructions": "Mix ingredients and bake.",
                "nombre_avis": 10,
            },
            {
                "id_recette": 2,
                "nom_recette": "Banana Bread",
                "categorie": "Dessert",
                "origine": "American",
                "liste_ingredients": ["Banana", "Flour"],
                "instructions": "Mix ingredients and bake.",
                "nombre_avis": 20,
            },
        ]
        result = self.service_recette.rechercher_par_nom_recette("Apple")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].nom_recette, "Apple Frangipan Tart")

    def test_rechercher_par_id_recette(self):
        """
        Test de la méthode rechercher_par_id_recette.
        """
        self.recette_dao_mock.get_recette_by_id.return_value = {
            "id_recette": 1,
            "nom_recette": "Apple Frangipan Tart",
            "categorie": "Dessert",
            "origine": "French",
            "liste_ingredients": ["Apple", "Tart"],
            "instructions": "Mix ingredients and bake.",
            "nombre_avis": 10,
        }
        result = self.service_recette.rechercher_par_id_recette(1)
        self.assertIsNotNone(result)
        self.assertEqual(result[0].nom_recette, "Apple Frangipan Tart")

    def test_rechercher_par_ingredient(self):
        """
        Test de la méthode rechercher_par_ingredient.
        """
        self.recette_dao_mock.get_all_recettes.return_value = [
            {
                "id_recette": 1,
                "nom_recette": "Apple Frangipan Tart",
                "categorie": "Dessert",
                "origine": "French",
                "liste_ingredients": ["Apple", "Tart"],
                "instructions": "Mix ingredients and bake.",
                "nombre_avis": 10,
            },
            {
                "id_recette": 2,
                "nom_recette": "Banana Bread",
                "categorie": "Dessert",
                "origine": "American",
                "liste_ingredients": ["Banana", "Flour"],
                "instructions": "Mix ingredients and bake.",
                "nombre_avis": 20,
            },
        ]
        result = self.service_recette.rechercher_par_ingredient("Apple")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].nom_recette, "Apple Frangipan Tart")

    def test_creer_recette(self):
        """
        Test de la méthode creer_recette.
        """
        self.recette_dao_mock.add_recette.return_value = 1
        recette_id = self.service_recette.creer_recette(
            "Exemple Recette",
            "Dessert",
            "British",
            "Touiller / Remuer / Mélanger",
            ["Butter", "Jam"],
        )
        self.assertEqual(recette_id, 1)

    def test_modifier_recette_id(self):
        """
        Test de la méthode modifier_recette_id.
        """
        self.recette_dao_mock.get_recette_by_id.return_value = {
            "id_recette": 1,
            "nom_recette": "Apple Frangipan Tart",
            "categorie": "Dessert",
            "origine": "French",
            "liste_ingredients": ["Apple", "Tart"],
            "instructions": "Mix ingredients and bake.",
            "nombre_avis": 10,
        }
        self.recette_dao_mock.update_by_recette_id.return_value = True
        result = self.service_recette.modifier_recette_id(1, nom_recette="Tarte Crème")
        self.assertTrue(result)

    def test_supprimer_recette(self):
        """
        Test de la méthode supprimer_recette.
        """
        self.recette_dao_mock.get_recette_by_id.return_value = {
            "id_recette": 1,
            "nom_recette": "Apple Frangipan Tart",
            "categorie": "Dessert",
            "origine": "French",
            "liste_ingredients": ["Apple", "Tart"],
            "instructions": "Mix ingredients and bake.",
            "nombre_avis": 10,
        }
        self.recette_dao_mock.delete_recette.return_value = True
        result = self.service_recette.supprimer_recette(1)
        self.assertTrue(result)

    def test_ajouter_recette_favorite(self):
        """
        Test de la méthode ajouter_recette_favorite.
        """
        self.recette_favorite_dao_mock.is_recette_in_favoris.return_value = False
        result = self.service_recette.ajouter_recette_favorite("Apple Frangipan Tart", 2)
        self.assertTrue(result)

    def test_supprimer_recette_favorite(self):
        """
        Test de la méthode supprimer_recette_favorite.
        """
        self.recette_favorite_dao_mock.delete_recette_favorite.return_value = True
        result = self.service_recette.supprimer_recette_favorite("Apple Frangipan Tart", 2)
        self.assertIsNone(result)

    def test_afficher_recettes_favorites(self):
        """
        Test de la méthode afficher_recettes_favorites.
        """
        self.recette_favorite_dao_mock.get_favoris_by_user_id.return_value = [
            "Apple Frangipan Tart"
        ]
        result = self.service_recette.afficher_recettes_favorites(2)
        self.assertEqual(result, ["Apple Frangipan Tart"])
