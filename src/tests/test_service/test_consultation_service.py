from unittest.mock import MagicMock
from service.service_consultation import ConsultationService
from dao.consultation_dao import ConsultationDAO
from models.consultation import Consultation
from datetime import date


def test_creer_consultation_ok():
    """Test de la création d'une consultation réussie"""
    # GIVEN
    id_recette, id_utilisateur = 1, 42
    mock_consultation_dao = MagicMock(spec=ConsultationDAO)
    consultation_service = ConsultationService(mock_consultation_dao)

    # WHEN
    consultation = consultation_service.creer_consultation(id_recette, id_utilisateur)

    # THEN
    assert consultation.id_recette == id_recette
    assert consultation.id_utilisateur == id_utilisateur
    assert consultation.date_consultation == date.today()
    mock_consultation_dao.add_consultation.assert_called_once_with(
        id_recette, id_utilisateur, date.today()
    )


def test_recuperer_consultations_par_utilisateur():
    """Test de la récupération des consultations d'un utilisateur"""
    # GIVEN
    id_utilisateur = 42
    consultations_data = [
        (1, id_utilisateur, date(2023, 1, 1)),
        (2, id_utilisateur, date(2023, 1, 2)),
    ]
    mock_consultation_dao = MagicMock(spec=ConsultationDAO)
    mock_consultation_dao.get_consultations_by_user_id.return_value = consultations_data
    consultation_service = ConsultationService(mock_consultation_dao)

    # WHEN
    consultations = consultation_service.recuperer_consultations_par_utilisateur(id_utilisateur)

    # THEN
    assert len(consultations) == 2
    assert consultations[0].id_recette == 1
    assert consultations[1].id_recette == 2
    mock_consultation_dao.get_consultations_by_user_id.assert_called_once_with(id_utilisateur)


def test_modifier_consultation():
    """Test de la modification d'une consultation"""
    # GIVEN
    id_recette, id_utilisateur = 1, 42
    kwargs = {"date_consultation": date(2023, 10, 10)}
    mock_consultation_dao = MagicMock(spec=ConsultationDAO)
    consultation_service = ConsultationService(mock_consultation_dao)

    # WHEN
    consultation_service.modifier_consultation(id_recette, id_utilisateur, **kwargs)

    # THEN
    mock_consultation_dao.update_consultation.assert_called_once_with(
        id_recette, id_utilisateur, **kwargs
    )


def test_supprimer_consultation():
    """Test de la suppression d'une consultation"""
    # GIVEN
    id_recette, id_utilisateur = 1, 42
    mock_consultation_dao = MagicMock(spec=ConsultationDAO)
    consultation_service = ConsultationService(mock_consultation_dao)

    # WHEN
    consultation_service.supprimer_consultation(id_recette, id_utilisateur)

    # THEN
    mock_consultation_dao.delete_consultation.assert_called_once_with(id_recette, id_utilisateur)


def test_afficher_consultations_utilisateur(capsys):
    """Test de l'affichage des consultations d'un utilisateur"""
    # GIVEN
    id_utilisateur = 42
    consultations_data = [
        Consultation(1, id_utilisateur, date(2023, 1, 1)),
        Consultation(2, id_utilisateur, date(2023, 1, 2)),
    ]
    mock_consultation_dao = MagicMock(spec=ConsultationDAO)
    consultation_service = ConsultationService(mock_consultation_dao)

    # On simule la méthode de récupération des consultations pour cet utilisateur
    consultation_service.recuperer_consultations_par_utilisateur = MagicMock(
        return_value=consultations_data
    )

    # WHEN
    consultation_service.afficher_consultations_utilisateur(id_utilisateur)

    # THEN
    captured = capsys.readouterr()
    assert "Recette: 1" in captured.out
    assert "Recette: 2" in captured.out
    consultation_service.recuperer_consultations_par_utilisateur.assert_called_once_with(
        id_utilisateur
    )


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
