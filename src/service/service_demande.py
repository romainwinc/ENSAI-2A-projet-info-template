from dao.demande_dao import DemandeDAO
from models.demande import Demande


class ServiceDemande:
    def __init__(self, demande_dao):
        self.demande_dao = demande_dao

    def creer_demande(
        self, id_utilisateur, type_demande, attribut_modifie, attribut_corrige, commentaire_demande
    ):
        """Crée une nouvelle demande et la stocke dans la base de données."""
        id_demande = self.demande_dao.add_demande(
            id_utilisateur, type_demande, attribut_modifie, attribut_corrige, commentaire_demande
        )
        return Demande(
            id_demande,
            id_utilisateur,
            type_demande,
            attribut_modifie,
            attribut_corrige,
            commentaire_demande,
        )

    def recuperer_demande(self, demande_id):
        """Récupère une demande par son ID."""
        demande_data = self.demande_dao.get_demande_by_id(demande_id)
        if demande_data:
            return Demande(*demande_data)
        return None

    def recuperer_demandes_with_role(self):
        """
        Récupère et affiche toutes les demandes de la table 'demande'
        où l'attribut_modifie est égal à "role".

        Returns:
            None
        """
        demandes = self.demande_dao.get_demandes_with_role()

        if not demandes:  # Vérifie si la liste est vide
            print("Aucune demande avec l'attribut modifié égal à 'role'.")
            return

        print("Demandes où 'attribut_modifie' est égal à 'role' :")
        print("=" * 50)
        for demande in demandes:
            print(f"ID Demande       : {demande['id_demande']}")
            print(f"ID Utilisateur   : {demande['id_utilisateur']}")
            print(f"Type de Demande  : {demande['type_demande']}")
            print(f"Attribut Modifié : {demande['attribut_modifie']}")
            print(f"Attribut Corrigé : {demande['attribut_corrige']}")
            print(f"Commentaire      : {demande['commentaire_demande']}")
            print("-" * 50)
        return demandes

    def recuperer_demandes_with_recette(self):
        """
        Récupère et affiche toutes les demandes de la table 'demande'
        où le type de demande est "Suppression recette".

        Returns:
            None
        """
        demandes = self.demande_dao.get_demandes_with_recette()

        if not demandes:  # Vérifie si la liste est vide
            print("Aucune demande de suppression de recettes.")
            return

        print("Demandes de suppressions de recettes :")
        print("=" * 50)
        for demande in demandes:
            print(f"ID Demande       : {demande['id_demande']}")
            print(f"ID Utilisateur   : {demande['id_utilisateur']}")
            print(f"Type de Demande  : {demande['type_demande']}")
            print(f"Attribut Modifié : {demande['attribut_modifie']}")
            print(f"Attribut Corrigé : {demande['attribut_corrige']}")
            print(f"Commentaire      : {demande['commentaire_demande']}")
            print("-" * 50)
        return demandes

    def afficher_demande(self, demande_id):
        """Affiche les détails d'une demande en montrant les valeurs des attributs."""
        demande = self.demande_dao.get_demande_by_id(demande_id)
        if demande:
            print(f"ID Demande: {demande['id_demande']}")
            print(f"Type de Demande: {demande['id_utilisateur']}")
            print(f"Attribut Modifié: {demande['type_demande']}")
            print(f"Attribut Corrigé: {demande['attribut_corrige']}")
            print(f"Commentaire: {demande['commentaire_demande']}")
        else:
            print("Demande non trouvée.")

    def afficher_demandes_par_id_utilisateur(self, id_utilisateur):
        """
        Affiche toutes les demandes d'un utilisateur donné en montrant les valeurs des attributs.
        """
        demandes = self.demande_dao.get_demande_by_id_utilisateur(id_utilisateur)

        if demandes:
            print(f"Demandes pour l'utilisateur {id_utilisateur} :")
            for demande in demandes:
                # On suppose que chaque 'demande' est un dictionnaire avec les valeurs
                # accessibles par clé
                print(f"ID Demande: {demande['id_demande']}")
                print(f"Type de Demande: {demande['type_demande']}")
                print(f"Attribut Modifié: {demande['attribut_modifie']}")
                print(f"Attribut Corrigé: {demande['attribut_corrige']}")
                print(f"Commentaire: {demande['commentaire_demande']}")
                print("-" * 40)  # Ligne de séparation pour chaque demande
        else:
            print(f"Aucune demande trouvée pour l'utilisateur {id_utilisateur}.")
            return False

    def supprimer_demande(self, demande_id):
        """
        Supprime une demande par son ID.

        Args:
            demande_id (int): L'ID de la demande à supprimer.

        Returns:
            bool: True si la demande a été supprimée, False si aucune demande avec cet ID n'existe.
        """
        # Vérifie si la demande existe avant de tenter de la supprimer
        demande_existe = self.demande_dao.get_demande_by_id(demande_id)

        if not demande_existe:
            return False  # La demande n'existe pas, retour False

        # Supprime la demande
        self.demande_dao.delete_demande(demande_id)
        return True


if __name__ == "__main__":
    dao = DemandeDAO()
    pass

    # print(ServiceDemande(dao).recuperer_demande(1))

    # print(ServiceDemande(dao).supprimer_demande(1))

    # print(ServiceDemande(dao).afficher_demande(1))

    # print(ServiceDemande(dao).afficher_demandes_par_id_utilisateur(1))

    # print(ServiceDemande(dao).afficher_demandes_par_id_utilisateur(1))

    # print(ServiceDemande(dao).recuperer_demandes_with_role())

    # print(ServiceDemande(dao).supprimer_demande(1))
