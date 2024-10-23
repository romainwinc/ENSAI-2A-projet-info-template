from service.service_utilisateur import ServiceUtilisateur
from dao.utilisateur_dao import UtilisateurDao
from models.utilisateur import Utilisateur


try:
    dao = UtilisateurDao()
    utilisateur3 = Utilisateur(
        nom_utilisateur="Antoine_Dupont",
        mot_de_passe="Totolebest",
        id_utilisateur=None,
        role="Connecté",
    )
    utilisateur2 = Utilisateur(
        nom_utilisateur="Jean", mot_de_passe="123", id_utilisateur=None, role="Professionel"
    )
    utilisateur = Utilisateur(
        nom_utilisateur="Jaja", mot_de_passe="1234", id_utilisateur=None, role="Connecté"
    )

    utilisateur = ServiceUtilisateur(dao).creer_utilisateur(
        utilisateur.nom_utilisateur, utilisateur.mot_de_passe
    )
    utilisateur2 = ServiceUtilisateur(dao).creer_utilisateur(
        utilisateur2.nom_utilisateur, utilisateur2.mot_de_passe
    )
    utilisateur3 = ServiceUtilisateur(dao).creer_utilisateur(
        utilisateur3.nom_utilisateur, utilisateur3.mot_de_passe
    )
    ServiceUtilisateur(dao).changer_role_utilisateur(
        utilisateur3.id_utilisateur, new_role="Administrateur"
    )
    ServiceUtilisateur(dao).changer_role_utilisateur(
        utilisateur2.id_utilisateur, new_role="Professionnel"
    )
    # ServiceUtilisateur(dao).supprimer_utilisateur(5)
    # ServiceUtilisateur(dao).se_connecter("Jaja", "1234")
    # ServiceUtilisateur(dao).nom_utilisateur_deja_utilise("Jaja")

except ValueError as e:
    print(e)
