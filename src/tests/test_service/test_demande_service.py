from unittest.mock import MagicMock
from service_demande import DemandeService
from dao.demande_dao import DemandeDAO
from models.demande import Demande


def test_creer_demande_ok():
    """Test de la création d'une demande réussie"""
    # GIVEN
    id_utilisateur, type_demande = 42, "Modification"
    attribut_modifie, attribut_corrige = "nom", "nouveau_nom"
    commentaire_demande = "Correction du nom"
    id_demande = 1

    mock_demande_dao = MagicMock(spec=DemandeDAO)
    mock_demande_dao.add_demande.return_value = id_demande
    demande_service = DemandeService(mock_demande_dao)

    # WHEN
    demande = demande_service.creer_demande(
        id_utilisateur, type_demande, attribut_modifie, attribut_corrige, commentaire_demande
    )

    # THEN
    assert demande.id_demande == id_demande
    assert demande.id_utilisateur == id_utilisateur
    assert demande.type_demande == type_demande
    assert demande.attribut_modifie == attribut_modifie
    assert demande.attribut_corrige == attribut_corrige
    assert demande.commentaire_demande == commentaire_demande
    mock_demande_dao.add_demande.assert_called_once_with(
        id_utilisateur, type_demande, attribut_modifie, attribut_corrige, commentaire_demande
    )


def test_recuperer_demande():
    """Test de la récupération d'une demande par ID"""
    # GIVEN
    id_demande = 1
    demande_data = (id_demande, 42, "Modification", "nom", "nouveau_nom", "Correction du nom")

    mock_demande_dao = MagicMock(spec=DemandeDAO)
    mock_demande_dao.get_demande_by_id.return_value = demande_data
    demande_service = DemandeService(mock_demande_dao)

    # WHEN
    demande = demande_service.recuperer_demande(id_demande)

    # THEN
    assert demande.id_demande == demande_data[0]
    assert demande.id_utilisateur == demande_data[1]
    assert demande.type_demande == demande_data[2]
    mock_demande_dao.get_demande_by_id.assert_called_once_with(id_demande)


def test_modifier_demande():
    """Test de la modification d'une demande"""
    # GIVEN
    id_demande = 1
    kwargs = {"attribut_modifie": "nom", "attribut_corrige": "nom_corrige"}

    mock_demande_dao = MagicMock(spec=DemandeDAO)
    demande_service = DemandeService(mock_demande_dao)

    # WHEN
    demande_service.modifier_demande(id_demande, **kwargs)

    # THEN
    mock_demande_dao.update_demande.assert_called_once_with(id_demande, **kwargs)


def test_supprimer_demande():
    """Test de la suppression d'une demande"""
    # GIVEN
    id_demande = 1

    mock_demande_dao = MagicMock(spec=DemandeDAO)
    demande_service = DemandeService(mock_demande_dao)

    # WHEN
    demande_service.supprimer_demande(id_demande)

    # THEN
    mock_demande_dao.delete_demande.assert_called_once_with(id_demande)


def test_afficher_demande(capsys):
    """Test de l'affichage des détails d'une demande"""
    # GIVEN
    id_demande = 1
    demande_data = Demande(
        id_demande, 42, "Modification", "nom", "nouveau_nom", "Correction du nom"
    )

    mock_demande_dao = MagicMock(spec=DemandeDAO)
    demande_service = DemandeService(mock_demande_dao)

    # Simuler la récupération de la demande
    demande_service.recuperer_demande = MagicMock(return_value=demande_data)

    # WHEN
    demande_service.afficher_demande(id_demande)

    # THEN
    captured = capsys.readouterr()
    assert "Modification" in captured.out
    demande_service.recuperer_demande.assert_called_once_with(id_demande)


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
