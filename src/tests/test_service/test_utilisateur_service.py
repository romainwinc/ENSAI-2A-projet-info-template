# import unittest
# from unittest.mock import MagicMock, patch
# from datetime import datetime
# from service.service_utilisateur import ServiceUtilisateur
# from models.utilisateur import Utilisateur
# from utils.securite import hash_password


# class TestServiceUtilisateur(unittest.TestCase):
#     def setUp(self):
#         self.mock_dao = MagicMock()
#         self.service = ServiceUtilisateur(self.mock_dao)

#     def test_creer_utilisateur(self):
#         # Given
#         nom = "Xavier"
#         mdp = "securepassword"
#         grade = "Connecté"
#         date_inscrit = datetime(2024, 1, 1)

#         with patch("service.service_utilisateur.hash_password", return_value="hashedpassword"):
#             self.mock_dao.add_user.return_value = True

#             # When
#             utilisateur = self.service.creer_utilisateur(nom, mdp)

#             # Then
#             self.mock_dao.add_user.assert_called_once()
#             self.assertEqual(utilisateur.nom_utilisateur, nom)
#             self.assertEqual(utilisateur.mot_de_passe, "hashedpassword")
#             self.assertEqual(utilisateur.role, grade)
#             self.assertIsInstance(utilisateur.date_inscription, datetime)

#     def test_creer_utilisateur_sans_mdp(self):
#         # Given
#         nom = "Xavier"
#         mdp = ""

#         # When & Then
#         with self.assertRaises(ValueError):
#             self.service.creer_utilisateur(nom, mdp)

#     def test_changer_role_utilisateur(self):
#         # Given
#         id_utilisateur = 1
#         new_role = "Administrateur"

#         # When
#         self.service.changer_role_utilisateur(id_utilisateur, new_role)

#         # Then
#         self.mock_dao.update_user.assert_called_once_with(id_utilisateur, new_role)

#     def test_supprimer_utilisateur(self):
#         # Given
#         id_utilisateur = 1

#         # When
#         self.service.supprimer_utilisateur(id_utilisateur)

#         # Then
#         self.mock_dao.delete_user.assert_called_once_with(id_utilisateur)

#     def test_se_connecter_utilisateur(self):
#         # Given
#         pseudo = "Xavier"
#         mdp = "securepassword"
#         hashed_password = "hashedpassword"
#         utilisateur_attendu = Utilisateur(
#             nom_utilisateur=pseudo,
#             mot_de_passe=hashed_password,
#             role="Connecté",
#             date_inscription=datetime.now(),
#         )

#         with patch("service.service_utilisateur.hash_password", return_value=hashed_password):
#             self.mock_dao.se_connecter.return_value = utilisateur_attendu

#             # When
#             utilisateur = self.service.se_connecter(pseudo, mdp)

#             # Then
#             self.mock_dao.se_connecter.assert_called_once_with(pseudo, hashed_password)
#             self.assertEqual(utilisateur.nom_utilisateur, utilisateur_attendu.nom_utilisateur)

#     def test_nom_utilisateur_deja_utilise(self):
#         # Given
#         utilisateurs_mock = [
#             Utilisateur(
#                 nom_utilisateur="Xavier",
#                 mot_de_passe="hashed",
#                 role="Connecté",
#                 date_inscription=datetime.now(),
#             ),
#             Utilisateur(
#                 nom_utilisateur="Alice",
#                 mot_de_passe="hashed",
#                 role="Connecté",
#                 date_inscription=datetime.now(),
#             ),
#         ]
#         self.mock_dao.lister_tous.return_value = utilisateurs_mock

#         # When
#         resultat = self.service.nom_utilisateur_deja_utilise("Xavier")

#         # Then
#         self.mock_dao.lister_tous.assert_called_once()
#         self.assertTrue(resultat)

#     def test_nom_utilisateur_non_utilise(self):
#         # Given
#         utilisateurs_mock = [
#             Utilisateur(
#                 nom_utilisateur="Alice",
#                 mot_de_passe="hashed",
#                 role="Connecté",
#                 date_inscription=datetime.now(),
#             ),
#         ]
#         self.mock_dao.lister_tous.return_value = utilisateurs_mock

#         # When
#         resultat = self.service.nom_utilisateur_deja_utilise("Bob")

#         # Then
#         self.mock_dao.lister_tous.assert_called_once()
#         self.assertFalse(resultat)


# if __name__ == "__main__":
#     unittest.main()
