import unittest
from unittest.mock import MagicMock, patch
from service.service_ingredient import ServiceIngredient


class TestServiceIngredient(unittest.TestCase):
    def setUp(self):
        # Création des mocks pour les DAO
        self.ingredients_favoris_dao_mock = MagicMock()
        self.ingredients_non_desires_dao_mock = MagicMock()
        self.liste_de_courses_dao_mock = MagicMock()

        # Création de l'instance de ServiceIngredient avec les mocks
        self.service_ingredient = ServiceIngredient(
            ingredient_dao=None,  # Si cette dépendance n'est pas utilisée, laissez-la comme None
            ingredients_favoris_dao=self.ingredients_favoris_dao_mock,
            ingredients_non_desires_dao=self.ingredients_non_desires_dao_mock,
            liste_de_courses_dao=self.liste_de_courses_dao_mock,
        )

    @patch("sys.stdout", new_callable=MagicMock)
    def test_recuperer_ingredients_favoris_utilisateur(self, mock_stdout):
        self.ingredients_favoris_dao_mock.get_favoris_by_user_id.return_value = [
            MagicMock(nom="Tomate"),
            MagicMock(nom="Carotte"),
        ]

        self.service_ingredient.recuperer_ingredients_favoris_utilisateur(utilisateur_id=1)

        self.ingredients_favoris_dao_mock.get_favoris_by_user_id.assert_called_once_with(1)

        # Vérification de l'impression
        mock_stdout.assert_called_with(
            "\nVoici vos ingrédients favoris :\n", "- Tomate\n", "- Carotte\n"
        )

    @patch("sys.stdout", new_callable=MagicMock)
    def test_supprimer_ingredients_favoris(self, mock_stdout):
        self.ingredients_favoris_dao_mock.delete_favori.return_value = True

        self.service_ingredient.supprimer_ingredients_favoris(utilisateur_id=1, ingredient_id=2)

        self.ingredients_favoris_dao_mock.delete_favori.assert_called_once_with(1, 2)

        # Vérification de l'impression
        mock_stdout.assert_called_with(f"L'ingrédient favori avec l'ID 2 a été supprimé.")

    @patch("sys.stdout", new_callable=MagicMock)
    def test_ajouter_ingredients_favoris(self, mock_stdout):
        self.ingredients_favoris_dao_mock.add_favori.return_value = (
            True  # Assurez-vous que la méthode est correcte
        )

        self.service_ingredient.ajouter_ingredients_favoris(utilisateur_id=1, ingredient_id=2)

        self.ingredients_favoris_dao_mock.add_favori.assert_called_once_with(1, 2)

        # Vérification de l'impression
        mock_stdout.assert_called_with(f"L'ingrédient favori avec l'ID 2 a été ajouté.")

    @patch("sys.stdout", new_callable=MagicMock)
    def test_recuperer_ingredients_non_desires_utilisateur(self, mock_stdout):
        self.ingredients_non_desires_dao_mock.get_non_desires_by_user_id.return_value = [
            MagicMock(nom="Oignon"),
            MagicMock(nom="Poivron"),
        ]

        self.service_ingredient.recuperer_ingredients_non_desires_utilisateur(utilisateur_id=1)

        self.ingredients_non_desires_dao_mock.get_non_desires_by_user_id.assert_called_once_with(1)

        # Vérification de l'impression
        mock_stdout.assert_called_with(
            "\nVoici vos ingrédients non-désirés :\n", "- Oignon\n", "- Poivron\n"
        )

    @patch("sys.stdout", new_callable=MagicMock)
    def test_supprimer_ingredients_non_desires(self, mock_stdout):
        self.ingredients_non_desires_dao_mock.delete_non_desire.return_value = True

        self.service_ingredient.supprimer_ingredients_non_desires(utilisateur_id=1, ingredient_id=2)

        self.ingredients_non_desires_dao_mock.delete_non_desire.assert_called_once_with(1, 2)

        # Vérification de l'impression
        mock_stdout.assert_called_with(f"L'ingrédient non-désiré avec l'ID 2 a été supprimé.")

    @patch("sys.stdout", new_callable=MagicMock)
    def test_ajouter_ingredients_non_desires(self, mock_stdout):
        self.ingredients_non_desires_dao_mock.add_ingredient_non_desire.return_value = True

        self.service_ingredient.ajouter_ingredients_non_desires(utilisateur_id=1, ingredient_id=2)

        self.ingredients_non_desires_dao_mock.add_ingredient_non_desire.assert_called_once_with(
            1, 2
        )

        # Vérification de l'impression
        mock_stdout.assert_called_with(f"L'ingrédient non-désiré avec l'ID 2 a été ajouté.")

    @patch("sys.stdout", new_callable=MagicMock)
    def test_afficher_ingredients_liste_courses(self, mock_stdout):
        self.liste_de_courses_dao_mock.get_liste_by_user_id.return_value = [
            MagicMock(nom="Pâtes"),
            MagicMock(nom="Sauce tomate"),
        ]

        self.service_ingredient.afficher_ingredients_liste_courses(utilisateur_id=1)

        self.liste_de_courses_dao_mock.get_liste_by_user_id.assert_called_once_with(1)

        # Vérification de l'impression
        mock_stdout.assert_called_with(
            "\nVoici les ingrédients de votre liste de courses :\n", "- Pâtes\n", "- Sauce tomate\n"
        )

    @patch("sys.stdout", new_callable=MagicMock)
    def test_supprimer_ingredients_liste_courses(self, mock_stdout):
        self.liste_de_courses_dao_mock.delete_from_liste.return_value = True

        self.service_ingredient.supprimer_ingredients_liste_courses(
            utilisateur_id=1, recette_id=1, ingredient_id=2
        )

        self.liste_de_courses_dao_mock.delete_from_liste.assert_called_once_with(2, 1, 1)

        # Vérification de l'impression
        mock_stdout.assert_called_with(
            f"L'ingrédient avec l'ID 2 a été supprimé de la liste de courses."
        )

    @patch("sys.stdout", new_callable=MagicMock)
    def test_ajouter_ingredients_liste_courses(self, mock_stdout):
        self.liste_de_courses_dao_mock.add_liste_de_courses.return_value = True

        self.service_ingredient.ajouter_ingredients_liste_courses(
            utilisateur_id=1, recette_id=1, ingredient_id=2
        )

        self.liste_de_courses_dao_mock.add_liste_de_courses.assert_called_once_with(2, 1, 1)

        # Vérification de l'impression
        mock_stdout.assert_called_with(
            f"L'ingrédient avec l'ID 2 a été ajouté à la liste de courses."
        )


if __name__ == "__main__":
    unittest.main()
