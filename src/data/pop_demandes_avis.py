from dao.demande_dao import DemandeDAO
from dao.avis_dao import AvisDAO
from service.service_avis import ServiceAvis
from service.service_demande import ServiceDemande
from datetime import datetime


try:
    # Les demandes de changement de role

    demande_dao = DemandeDAO()

    ServiceDemande(demande_dao).creer_demande(
        id_utilisateur=1,
        type_demande="Passer professionnel",
        attribut_modifie="",
        attribut_corrige="Xavier",
        commentaire_demande=f"changer nom de l'utilisateurpar Xavier",
    )

    ServiceDemande(demande_dao).creer_demande(
        id_utilisateur=2,
        type_demande="Passer Administrateur",
        attribut_modifie="",
        attribut_corrige="Xavier",
        commentaire_demande=f"changer nom de l'utilisateu par Xavier",
    )

    ServiceDemande(demande_dao).creer_demande(
        id_utilisateur=3,
        type_demande="Passer administrateur",
        attribut_modifie="",
        attribut_corrige="Xavier",
        commentaire_demande=f"changer nom de l'utilisateurpar Xavier",
    )

    ServiceDemande(demande_dao).creer_demande(
        id_utilisateur=4,
        type_demande="Passer administrateur",
        attribut_modifie="",
        attribut_corrige="Xavier",
        commentaire_demande=f"changer nom de l'utilisat par Xavier",
    )

    # Les avis

    avis_dao = AvisDAO()

    ServiceAvis(avis_dao).ajouter_avis(
        id_recette=1,
        id_utilisateur=1,
        titre_avis="Je recommande",
        nom_auteur="Antoine_Dupont",
        date_publication=datetime.now(),
        commentaire="Tarte originale.",
        note=5,
    )

    ServiceAvis(avis_dao).ajouter_avis(
        id_recette=1,
        id_utilisateur=2,
        titre_avis="Attention à la cuisson",
        nom_auteur="Flo",
        date_publication=datetime.now(),
        commentaire="Je penses qu'il faudrait diminuer le temps de cuisson, sinon ren à repprocher.",
        note=4,
    )

    ServiceAvis(avis_dao).ajouter_avis(
        id_recette=1,
        id_utilisateur=3,
        titre_avis="Classique",
        nom_auteur="Paul_Bocuse",
        date_publication=datetime.now(),
        commentaire="Une recommande cette recette Classique de la gastronomie Française",
        note=4,
    )

    ServiceAvis(avis_dao).ajouter_avis(
        id_recette=1,
        id_utilisateur=4,
        titre_avis="Recette au top",
        nom_auteur="Lea",
        date_publication=datetime.now(),
        commentaire="Une recette que je recommande les yeux fermés.",
        note=5,
    )

    print("---- Initialisation des Demandes et Avis terminée ----")

except ValueError as e:
    print(e)
