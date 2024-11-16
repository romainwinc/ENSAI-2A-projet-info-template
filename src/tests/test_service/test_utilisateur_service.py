# import unittest
# from unittest.mock import MagicMock
# from service.service_utilisateur import ServiceUtilisateur
# from models.utilisateur import Utilisateur
# from utils.securite import hash_password


# class TestServiceUtilisateur(unittest.TestCase):
#     def setUp(self):
#         # Création d'un mock pour UtilisateurDao
#         self.utilisateur_dao_mock = MagicMock()
#         self.service_utilisateur = ServiceUtilisateur()
#         self.service_utilisateur.utilisateur_dao = self.utilisateur_dao_mock

#     def test_creer_utilisateur(self):
#         # Configuration des données de test
#         self.utilisateur_dao_mock.add_user.return_value = True  # Simule le succès de l'ajout
#         nouvel_utilisateur = self.service_utilisateur.creer_utilisateur("Nouveau_User", "mon_mot_de_passe")

#         # Vérifications
#         self.assertEqual(nouvel_utilisateur.nom_utilisateur, "Nouveau_User")
#         self.assertEqual(nouvel_utilisateur.role, "Connecté")
#         self.utilisateur_dao_mock.add_user.assert_called_once()

#     def test_creer_utilisateur_mdp_vide(self):
#         """Test pour vérifier que ValueError est levé si le mot de passe est vide."""
#         with self.assertRaises(ValueError) as context:
#             self.service_utilisateur.creer_utilisateur("Nouveau_User", "")
#         self.assertEqual(str(context.exception), "Le mot de passe ne peut pas être vide.")

#     def test_changer_role_utilisateur(self):
#         """Test pour vérifier le changement de rôle d'un utilisateur."""
#         service = self.service_utilisateur
#         service.changer_role_utilisateur("1", "Admin")

#         self.utilisateur_dao_mock.update_user.assert_called_once_with("1", "Admin")

#     def test_supprimer_utilisateur(self):
#         """Test pour vérifier la suppression d'un utilisateur."""
#         service = self.service_utilisateur
#         service.supprimer_utilisateur("1")

#         self.utilisateur_dao_mock.delete_user.assert_called_once_with("1")

#     def test_se_connecter(self):
#         """Test pour vérifier la connexion d'un utilisateur."""
#         hashed_password = hash_password("mot_de_passe", "pseudo")
#         self.utilisateur_dao_mock.se_connecter.return_value = Utilisateur(nom_utilisateur="Jaja", mot_de_passe=hashed_password)

#         utilisateur = self.service_utilisateur.se_connecter("Jaja", "mot_de_passe")

#         self.assertEqual(utilisateur.nom_utilisateur, "Jaja")
#         self.utilisateur_dao_mock.se_connecter.assert_called_once()

#     def test_nom_utilisateur_deja_utilise(self):
#         """Test pour vérifier si le nom d'utilisateur est déjà utilisé."""
#         fake_utilisateurs = [
#             Utilisateur(nom_utilisateur="Jaja", mot_de_passe="1234", role="Connecté"),
#             Utilisateur(nom_utilisateur="Jean", mot_de_passe="123", role="Professionnel"),
#         ]
#         self.utilisateur_dao_mock.lister_tous.return_value = fake_utilisateurs

#         existe_deja = self.service_utilisateur.nom_utilisateur_deja_utilise("Jaja")

#         self.assertTrue(existe_deja)  # "Jaja" existe déjà

#     def test_nom_utilisateur_non_utilise(self):
#         """Test pour vérifier que le nom d'utilisateur n'est pas utilisé."""
#         fake_utilisateurs = [
#             Utilisateur(nom_utilisateur="Jaja", mot_de_passe="1234", role="Connecté"),
#             Utilisateur(nom_utilisateur="Jean", mot_de_passe="123", role="Professionnel"),
#         ]
#         self.utilisateur_dao_mock.lister_tous.return_value = fake_utilisateurs

#         existe_deja = self.service_utilisateur.nom_utilisateur_deja_utilise("Inconnu")

#         self.assertFalse(existe_deja)  # "Inconnu" n'existe pas


# if __name__ == "__main__":
#     unittest.main()
