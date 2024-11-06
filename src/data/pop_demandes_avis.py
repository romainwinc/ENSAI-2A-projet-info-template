from dao.demande_dao import DemandeDAO
from dao.avis_dao import AvisDAO
from models.avis import Avis
from models.demande import Demande
from service.service_avis import ServiceAvis
from service.service_demande import ServiceDemande


try:
    demande_dao = DemandeDAO()
    avis_dao = AvisDAO()

    for i in range(1, 7):
        ServiceDemande(demande_dao).creer_demande(
            id_utilisateur=i,
            type_demande="modification utilisateur",
            attribut_modifie="nom",
            attribut_corrige="Xavier",
            commentaire_demande=f"changer nom de l'utilisateur {i} par Xavier",
        )

    print("---- Initialisation des Demandes et Avis terminée ----")

except ValueError as e:
    print(e)
