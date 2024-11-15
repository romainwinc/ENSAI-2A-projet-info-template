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

    def afficher_demande(self, demande_id):
        """Affiche les détails d'une demande en montrant les valeurs des attributs."""
        demande = self.recuperer_demande(demande_id)
        if demande:
            print(f"ID Demande: {demande.id_demande}")
            print(f"Type de Demande: {demande.type_demande}")
            print(f"Attribut Modifié: {demande.attribut_modifie}")
            print(f"Attribut Corrigé: {demande.attribut_corrige}")
            print(f"Commentaire: {demande.commentaire_demande}")
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


if __name__ == "__main__":
    dao = DemandeDAO()

    # print(
    #     ServiceDemande(dao).creer_demande(
    #         id_utilisateur=1,
    #         type_demande="modification utilisateur",
    #         attribut_modifie="nom",
    #         attribut_corrige="Xavier",
    #         commentaire_demande="changer nom de l'utilisateur 1 par Xavier",
    #     )
    # )  # Marche

    # print(ServiceDemande(dao).recuperer_demande(1))

    # print(ServiceDemande(dao).supprimer_demande(1))

    # print(ServiceDemande(dao).afficher_demande(1))

    # print(ServiceDemande(dao).recherche_demande_par_id_utilisateur(1))

    print(ServiceDemande(dao).afficher_demandes_par_id_utilisateur(1))
