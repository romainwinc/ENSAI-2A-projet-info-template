from service.service_utilisateur import ServiceUtilisateur
from dao.utilisateur_dao import UtilisateurDao
from models.utilisateur import Utilisateur


try:
    dao = UtilisateurDao()
    user1 = Utilisateur(
        nom_utilisateur="Antoine_Dupont",
        mot_de_passe="1234",
        id_utilisateur=None,
        role=None,
    )

    user2 = Utilisateur(
        nom_utilisateur="Flo",
        mot_de_passe="1234",
        id_utilisateur=None,
        role=None,
    )

    user3 = Utilisateur(
        nom_utilisateur="Paul_Bocuse",
        mot_de_passe="1234",
        id_utilisateur=None,
        role=None,
    )

    user4 = Utilisateur(
        nom_utilisateur="Lea",
        mot_de_passe="1234",
        id_utilisateur=None,
        role=None,
    )

    user5 = Utilisateur(
        nom_utilisateur="Marc",
        mot_de_passe="1234",
        id_utilisateur=None,
        role=None,
    )

    user6 = Utilisateur(
        nom_utilisateur="Céline_Fontaine",
        mot_de_passe="1234",
        id_utilisateur=None,
        role=None,
    )

    utilisateur1 = ServiceUtilisateur(dao).creer_utilisateur(
        user1.nom_utilisateur, user1.mot_de_passe
    )
    utilisateur2 = ServiceUtilisateur(dao).creer_utilisateur(
        user2.nom_utilisateur, user2.mot_de_passe
    )
    utilisateur3 = ServiceUtilisateur(dao).creer_utilisateur(
        user3.nom_utilisateur, user3.mot_de_passe
    )
    utilisateur4 = ServiceUtilisateur(dao).creer_utilisateur(
        user4.nom_utilisateur, user4.mot_de_passe
    )
    utilisateur5 = ServiceUtilisateur(dao).creer_utilisateur(
        user5.nom_utilisateur, user5.mot_de_passe
    )
    utilisateur6 = ServiceUtilisateur(dao).creer_utilisateur(
        user6.nom_utilisateur, user6.mot_de_passe
    )

    ServiceUtilisateur(dao).changer_role_utilisateur(
        utilisateur3.id_utilisateur, new_role="Professionnel"
    )
    ServiceUtilisateur(dao).changer_role_utilisateur(
        utilisateur4.id_utilisateur, new_role="Professionnel"
    )

    ServiceUtilisateur(dao).changer_role_utilisateur(
        utilisateur5.id_utilisateur, new_role="Administrateur"
    )
    ServiceUtilisateur(dao).changer_role_utilisateur(
        utilisateur6.id_utilisateur, new_role="Administrateur"
    )

    print("---- Initialisation des Utilisateurs terminée ----")

except ValueError as e:
    print(e)
