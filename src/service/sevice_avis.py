from datetime import datetime
from dao.avis_dao import AvisDAO
from models.avis import Avis
from InquirerPy import inquirer


class AvisService:
    def __init__(self, avis_dao):
        self.avis_dao = avis_dao

    def creer_avis(
        self, id_recette, id_utilisateur, titre_avis, nom_auteur, commentaire, note=None
    ):
        """Crée un nouvel avis et le stocke dans la base de données."""
        date_publication = datetime.now()  # Utilisation de la date actuelle
        id_avis = self.avis_dao.add_avis(
            id_recette, id_utilisateur, titre_avis, nom_auteur, date_publication, commentaire, note
        )
        return Avis(
            id_avis, titre_avis, id_utilisateur, nom_auteur, date_publication, commentaire, note
        )

    def recuperer_avis_par_recette(self, id_recette):
        """Récupère tous les avis liés à une recette spécifique."""
        avis_data = self.avis_dao.get_avis_by_recette_id(id_recette)
        return [Avis(*avis) for avis in avis_data]  # Crée une liste d'objets Avis

    def recuperer_avis_par_utilisateur(self, id_utilisateur):
        """Récupère tous les avis postés par un utilisateur spécifique."""
        avis_data = self.avis_dao.get_avis_by_user_id(id_utilisateur)
        return [Avis(*avis) for avis in avis_data]

    def modifier_avis(self, avis_id, **kwargs):
        """Modifie les attributs d'un avis existant."""
        self.avis_dao.update_avis(avis_id, **kwargs)

    def supprimer_avis(self, avis_id):
        """Supprime un avis de la base de données."""
        self.avis_dao.delete_avis(avis_id)

    def afficher_avis(self, id_recette):
        """Affiche les avis liés à une recette."""
        avis_list = self.recuperer_avis_par_recette(id_recette)
        for avis in avis_list:
            print(avis)

    def afficher_avis_utilisateur(self, id_utilisateur):
        """Affiche les avis liés à une recette."""
        avis_list = self.recuperer_avis_par_utilisateur(id_utilisateur)
        for avis in avis_list:
            print(avis)

    def afficher_notes_utilisateur(self, utilisateur_id):
        """Récupère et affiche uniquement les notes des avis de l'utilisateur."""
        avis_list = self.recuperer_avis_par_utilisateur(utilisateur_id)

        if not avis_list:
            print("Vous n'avez aucune note disponible.")
            return

        # Affiche les notes pour chaque avis
        for avis in avis_list:
            if avis.note is not None:  # Vérifie que l'avis a une note
                print(f"ID: {avis.id_avis}, Titre: {avis.titre_avis}, Note: {avis.note}")
            else:
                print(f"ID: {avis.id_avis}, Titre: {avis.titre_avis}, Note: Non noté")

    def supprimer_avis_utilisateur(self, utilisateur_id):
        """Permet à l'utilisateur de choisir un avis à supprimer et le supprime."""
        avis_list = self.recuperer_avis_par_utilisateur(utilisateur_id)

        if not avis_list:
            print("Vous n'avez aucun avis à supprimer.")
            return

        # Afficher les avis disponibles avec leur ID pour que l'utilisateur sache quel ID choisir
        print("\nVoici vos avis :\n")
        for avis in avis_list:
            print(
                f"ID: {avis.id_avis}, Titre: {avis.titre_avis}, Commentaire: {avis.commentaire}, Note: {avis.note}"
            )

        # Demander à l'utilisateur d'entrer l'ID de l'avis à supprimer
        avis_id_choisi = inquirer.text(
            message="Entrez l'ID de l'avis que vous souhaitez supprimer :",
        ).execute()

        # Valider que l'ID est bien dans la liste des avis de l'utilisateur
        avis_ids = [str(avis.id_avis) for avis in avis_list]
        if avis_id_choisi in avis_ids:
            # Supprimer l'avis si l'ID est valide
            self.supprimer_avis(int(avis_id_choisi))
            print(f"L'avis avec l'ID {avis_id_choisi} a été supprimé.")
        else:
            print("L'ID fourni ne correspond à aucun de vos avis.")

    def supprimer_note_utilisateur(self, utilisateur_id):
        """Permet à l'utilisateur de choisir un avis dont il souhaite supprimer la note."""
        avis_list = self.recuperer_avis_par_utilisateur(utilisateur_id)

        if not avis_list:
            print("Vous n'avez aucune note à supprimer.")
            return

        # Afficher les avis avec leurs notes disponibles
        print("\nVoici vos avis avec des notes :\n")
        avis_list_with_notes = [avis for avis in avis_list if avis.note is not None]

        if not avis_list_with_notes:
            print("Aucune note à supprimer.")
            return

        for avis in avis_list_with_notes:
            print(f"ID: {avis.id_avis}, Titre: {avis.titre_avis}, Note: {avis.note}")

        # Demander à l'utilisateur d'entrer l'ID de l'avis dont il souhaite supprimer la note
        avis_id_choisi = inquirer.text(
            message="Entrez l'ID de l'avis dont vous souhaitez supprimer la note :",
        ).execute()

        # Valider que l'ID est bien dans la liste des avis avec notes
        avis_ids = [str(avis.id_avis) for avis in avis_list_with_notes]
        if avis_id_choisi in avis_ids:
            # Supprimer uniquement la note (pas l'avis)
            self.modifier_avis(int(avis_id_choisi), note=None)
            print(f"La note de l'avis avec l'ID {avis_id_choisi} a été supprimée.")
        else:
            print("L'ID fourni ne correspond à aucun avis avec une note.")


if __name__ == "__main__":
    dao = AvisDAO()
    AvisService(dao).creer_avis(1)
