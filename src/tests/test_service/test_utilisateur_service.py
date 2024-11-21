import unittest
from unittest.mock import MagicMock
from datetime import datetime
from service.service_utilisateur import ServiceUtilisateur
from models.utilisateur import Utilisateur
from utils.securite import hash_password


class TestServiceUtilisateur(unittest.TestCase):
    def setUp(self):
        """
        Configure les mocks nécessaires pour chaque test.
        """
        self.utilisateur_dao_mock = MagicMock()
        self.service_utilisateur = ServiceUtilisateur(self.utilisateur_dao_mock)

    def test_creer_utilisateur_succes(self):
        """
        Test de la méthode creer_utilisateur.
        # When given a valid username and password,
        # then it should create a user with the correct attributes.
        """
        self.utilisateur_dao_mock.add_user.return_value = True

        utilisateur = self.service_utilisateur.creer_utilisateur("JohnDoe", "secure_password")
        self.assertIsNotNone(utilisateur)
        self.assertEqual(utilisateur.nom_utilisateur, "JohnDoe")
        self.assertEqual(utilisateur.role, "Connecté")
        self.assertEqual(
            utilisateur.mot_de_passe,
            hash_password("secure_password", "JohnDoe"),
        )

    def test_creer_utilisateur_mdp_vide(self):
        """
        Vérifie qu'une exception est levée si le mot de passe est vide.
        # When given an empty password,
        # then it should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            self.service_utilisateur.creer_utilisateur("JohnDoe", "")

    def test_changer_role_utilisateur(self):
        """
        Test de la méthode changer_role_utilisateur.
        # When given a valid user ID and a new role,
        # then it should call the DAO method to update the role.
        """
        self.service_utilisateur.changer_role_utilisateur("user123", "Admin")
        self.utilisateur_dao_mock.update_user.assert_called_once_with("user123", "Admin")

    def test_supprimer_utilisateur(self):
        """
        Test de la méthode supprimer_utilisateur.
        # When given a valid user ID,
        # then it should call the DAO method to delete the user.
        """
        self.service_utilisateur.supprimer_utilisateur("user123")
        self.utilisateur_dao_mock.delete_user.assert_called_once_with("user123")

    def test_se_connecter_succes(self):
        """
        Test de la méthode se_connecter.
        # When given valid credentials,
        # then it should return a user object with the correct details.
        """
        hashed_password = hash_password("secure_password", "JohnDoe")
        self.utilisateur_dao_mock.se_connecter.return_value = Utilisateur(
            nom_utilisateur="JohnDoe",
            mot_de_passe=hashed_password,
            role="Connecté",
            date_inscription=datetime.now(),
        )

        utilisateur = self.service_utilisateur.se_connecter("JohnDoe", "secure_password")
        self.assertIsNotNone(utilisateur)
        self.assertEqual(utilisateur.nom_utilisateur, "JohnDoe")
        self.assertEqual(utilisateur.role, "Connecté")

    def test_se_connecter_echec(self):
        """
        Vérifie qu'aucun utilisateur n'est retourné si les identifiants sont incorrects.
        # When given invalid credentials,
        # then it should return None.
        """
        self.utilisateur_dao_mock.se_connecter.return_value = None

        utilisateur = self.service_utilisateur.se_connecter("JohnDoe", "wrong_password")
        self.assertIsNone(utilisateur)

    def test_nom_utilisateur_deja_utilise_vrai(self):
        """
        Test de la méthode nom_utilisateur_deja_utilise.
        # When given a username that already exists,
        # then it should return True.
        """
        self.utilisateur_dao_mock.lister_tous.return_value = [
            Utilisateur(
                nom_utilisateur="JohnDoe",
                mot_de_passe="hashed",
                role="Connecté",
                date_inscription=datetime.now(),
            )
        ]

        result = self.service_utilisateur.nom_utilisateur_deja_utilise("JohnDoe")
        self.assertTrue(result)

    def test_nom_utilisateur_deja_utilise_faux(self):
        """
        Test de la méthode nom_utilisateur_deja_utilise.
        # When given a username that does not exist,
        # then it should return False.
        """
        self.utilisateur_dao_mock.lister_tous.return_value = [
            Utilisateur(
                nom_utilisateur="JaneDoe",
                mot_de_passe="hashed",
                role="Connecté",
                date_inscription=datetime.now(),
            )
        ]

        result = self.service_utilisateur.nom_utilisateur_deja_utilise("JohnDoe")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
