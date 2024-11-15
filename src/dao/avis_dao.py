from dao.db_connection import DBConnection
from utils.singleton import Singleton


class AvisDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection

    def add_avis(
        self,
        id_recette,
        id_utilisateur,
        titre_avis,
        nom_auteur,
        date_publication,
        commentaire,
        note,
    ):
        """Ajoute un nouvel avis."""
        query = """
            INSERT INTO projet_informatique.avis (id_recette, id_utilisateur, titre_avis,
            nom_auteur, date_publication, commentaire, note)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id_avis
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    query,
                    (
                        id_recette,
                        id_utilisateur,
                        titre_avis,
                        nom_auteur,
                        date_publication,
                        commentaire,
                        note,
                    ),
                )
                return cursor.fetchone()

    def get_avis_by_recette_id(self, id_recette):
        """Récupère les avis pour une recette donnée."""
        query = "SELECT * FROM projet_informatique.avis WHERE id_recette = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_recette,))
                rows = cursor.fetchall()

        avis = []
        for row in rows:
            avi = {
                "id_avis": row["id_avis"],
                "id_recette": row["id_recette"],
                "id_utilisateur": row["id_utilisateur"],
                "titre_avis": row["titre_avis"],
                "nom_auteur": row["nom_auteur"],
                "date_publication": row["date_publication"],
                "commentaire": row["commentaire"],
                "note": row["note"],
            }
            avis.append(avi)

        return avis

    def get_avis_by_user_id(self, id_utilisateur):
        """Récupère les avis d'un utilisateur donné."""
        query = "SELECT * FROM projet_informatique.avis WHERE id_utilisateur = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_utilisateur,))
                rows = cursor.fetchall()

        avis = []
        for row in rows:
            avi = {
                "id_avis": row["id_avis"],
                "id_recette": row["id_recette"],
                "id_utilisateur": row["id_utilisateur"],
                "titre_avis": row["titre_avis"],
                "nom_auteur": row["nom_auteur"],
                "date_publication": row["date_publication"],
                "commentaire": row["commentaire"],
                "note": row["note"],
            }
            avis.append(avi)

        return avis

    def update_avis(self, avis_id, **kwargs):
        """Met à jour un avis."""
        query = (
            "UPDATE projet_informatique.avis SET "
            + ", ".join([f"{key} = %s" for key in kwargs])
            + " WHERE id_avis = %s"
        )
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), avis_id))

    def delete_avis(self, avis_id):
        """Supprime un avis par son ID."""
        query = "DELETE FROM projet_informatique.avis WHERE id_avis = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (avis_id,))

    def update_avis_note(self, id_avis, note):
        """Modifie la note d'un avis"""
        query = (
            "UPDATE projet_informatique.avis SET note = %(note)s" + "WHERE id_avis = %(id_avis)s"
        )
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_avis, note))

    def somme_note_by_recette(self, recette_id):
        """Réalise la somme des notes d'une recette données"""
        query = """ SELECT note FROM projet_informatique.avis
                WHERE id_recette = %s """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (recette_id,))
                rows = cursor.fetchall()
        notes = [row["note"] for row in rows]
        somme = 0
        for note in notes:
            somme += note
        somme = somme / len(notes)
        print(somme)


if __name__ == "__main__":
    # print(AvisDAO().get_avis_by_recette_id(1))
    # print(AvisDAO().get_avis_by_user_id(8))
    # print(AvisDAO().count_nb_avis(1))
    AvisDAO().somme_note_by_recette(1)
