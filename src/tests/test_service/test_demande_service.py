# import unittest
# from unittest.mock import MagicMock
# from service.service_demande import ServiceDemande
# from models.demande import Demande


# class TestServiceDemande(unittest.TestCase):
#     def setUp(self):
#         self.mock_dao = MagicMock()
#         self.service = ServiceDemande(self.mock_dao)

#     def test_creer_demande(self):
#         # Given
#         self.mock_dao.add_demande.return_value = 1
#         id_utilisateur = 1
#         type_demande = "modification utilisateur"
#         attribut_modifie = "nom"
#         attribut_corrige = "Xavier"
#         commentaire_demande = "Changer le nom"

#         # When
#         demande = self.service.creer_demande(
#             id_utilisateur, type_demande, attribut_modifie, attribut_corrige, commentaire_demande
#         )

#         # Then
#         self.mock_dao.add_demande.assert_called_once_with(
#             id_utilisateur, type_demande, attribut_modifie, attribut_corrige, commentaire_demande
#         )
#         self.assertIsInstance(demande, Demande)
#         self.assertEqual(demande.id_demande, 1)
#         self.assertEqual(demande.type_demande, type_demande)

#     def test_recuperer_demande(self):
#         # Given
#         demande_id = 1
#         self.mock_dao.get_demande_by_id.return_value = (
#             1,
#             1,
#             "modification utilisateur",
#             "nom",
#             "Xavier",
#             "Commentaire",
#         )

#         # When
#         demande = self.service.recuperer_demande(demande_id)

#         # Then
#         self.mock_dao.get_demande_by_id.assert_called_once_with(demande_id)
#         self.assertIsInstance(demande, Demande)
#         self.assertEqual(demande.type_demande, "modification utilisateur")

#     def test_afficher_demandes_par_id_utilisateur(self):
#         # Given
#         id_utilisateur = 1
#         self.mock_dao.get_demande_by_id_utilisateur.return_value = [
#             {
#                 "id_demande": 1,
#                 "type_demande": "modification utilisateur",
#                 "attribut_modifie": "nom",
#                 "attribut_corrige": "Xavier",
#                 "commentaire_demande": "Changer le nom",
#             }
#         ]

#         # When
#         self.service.afficher_demandes_par_id_utilisateur(id_utilisateur)

#         # Then
#         self.mock_dao.get_demande_by_id_utilisateur.assert_called_once_with(id_utilisateur)

#     def test_recuperer_demande_non_existante(self):
#         # Given
#         demande_id = 99
#         self.mock_dao.get_demande_by_id.return_value = None

#         # When
#         demande = self.service.recuperer_demande(demande_id)

#         # Then
#         self.mock_dao.get_demande_by_id.assert_called_once_with(demande_id)
#         self.assertIsNone(demande)


# if __name__ == "__main__":
#     unittest.main()
