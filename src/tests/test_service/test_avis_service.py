# import unittest
# from unittest.mock import MagicMock
# from datetime import datetime
# from service.service_avis import ServiceAvis
# from models.avis import Avis


# class TestServiceAvis(unittest.TestCase):
#     def setUp(self):
#         self.mock_dao = MagicMock()
#         self.service = ServiceAvis(self.mock_dao)

#     def test_afficher_avis_par_recette(self):
#         # Given
#         id_recette = 1
#         self.mock_dao.get_avis_by_recette_id.return_value = [
#             {
#                 "id_avis": 1,
#                 "id_recette": id_recette,
#                 "id_utilisateur": 2,
#                 "titre_avis": "Super recette",
#                 "nom_auteur": "Xavier",
#                 "date_publication": datetime(2024, 1, 1),
#                 "commentaire": "Très bon!",
#                 "note": 5,
#             }
#         ]

#         # When
#         self.service.afficher_avis_par_recette(id_recette)

#         # Then
#         self.mock_dao.get_avis_by_recette_id.assert_called_once_with(id_recette)

#     def test_afficher_avis_par_utilisateur(self):
#         # Given
#         id_utilisateur = 1
#         self.mock_dao.get_avis_by_user_id.return_value = [
#             {
#                 "id_avis": 1,
#                 "id_recette": 10,
#                 "id_utilisateur": id_utilisateur,
#                 "titre_avis": "Bon repas",
#                 "nom_auteur": "Xavier",
#                 "date_publication": datetime(2024, 1, 1),
#                 "commentaire": "Délicieux!",
#                 "note": 4,
#             }
#         ]

#         # When
#         self.service.afficher_avis_par_utilisateur(id_utilisateur)

#         # Then
#         self.mock_dao.get_avis_by_user_id.assert_called_once_with(id_utilisateur)

#     def test_ajouter_avis(self):
#         # Given
#         self.mock_dao.add_avis.return_value = 1
#         id_recette = 1
#         id_utilisateur = 2
#         titre_avis = "Délicieux"
#         nom_auteur = "Xavier"
#         date_publication = datetime(2024, 1, 1)
#         commentaire = "Vraiment bon"
#         note = 5

#         # When
#         avis_id = self.service.ajouter_avis(
#             id_recette, id_utilisateur, titre_avis, nom_auteur, date_publication, commentaire, note
#         )

#         # Then
#         self.mock_dao.add_avis.assert_called_once_with(
#             id_recette, id_utilisateur, titre_avis, nom_auteur, date_publication, commentaire, note
#         )
#         self.assertEqual(avis_id, 1)

#     def test_supprimer_avis(self):
#         # Given
#         avis_id = 1

#         # When
#         self.service.supprimer_avis(avis_id)

#         # Then
#         self.mock_dao.delete_avis.assert_called_once_with(avis_id)

#     def test_modifier_avis(self):
#         # Given
#         avis_id = 1
#         kwargs = {"note": 4, "commentaire": "Pas mal"}

#         # When
#         self.service.modifier_avis(avis_id, **kwargs)

#         # Then
#         self.mock_dao.update_avis.assert_called_once_with(avis_id, **kwargs)

#     def test_afficher_notes_par_utilisateur(self):
#         # Given
#         id_utilisateur = 1
#         self.mock_dao.get_avis_by_user_id.return_value = [
#             {
#                 "id_avis": 1,
#                 "id_recette": 10,
#                 "id_utilisateur": id_utilisateur,
#                 "titre_avis": "Excellent",
#                 "nom_auteur": "Xavier",
#                 "date_publication": datetime(2024, 1, 1),
#                 "commentaire": "Délicieux",
#                 "note": 5,
#             }
#         ]

#         # When
#         self.service.afficher_notes_par_utilisateur(id_utilisateur)

#         # Then
#         self.mock_dao.get_avis_by_user_id.assert_called_once_with(id_utilisateur)
