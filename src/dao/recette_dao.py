from dao.db_connection import DBConnection
from utils.singleton import Singleton
from psycopg2 import sql
from dotenv import load_dotenv
import os
from models.recette import Recette


class RecetteDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection
        load_dotenv()
        self.schema = os.getenv("POSTGRES_SCHEMA")

    def get_all_recettes(self):
        """Récupère toutes les recettes de la table 'recette'."""
        query = (
            """
            SELECT id_recette, nom_recette, categorie, origine, instructions,
                   mots_cles, url_image, liste_ingredients, nombre_avis,
                   note_moyenne, date_derniere_modif
            FROM {}.recette
        """
        ).format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()

        recettes = []
        for row in rows:
            recette = {
                "id_recette": row["id_recette"],
                "nom_recette": row["nom_recette"],
                "categorie": row["categorie"],
                "origine": row["origine"],
                "instructions": row["instructions"],
                "mots_cles": row["mots_cles"],
                "url_image": row["url_image"],
                "liste_ingredients": row["liste_ingredients"],
                "nombre_avis": row["nombre_avis"],
                "note_moyenne": row["note_moyenne"],
                "date_derniere_modif": row["date_derniere_modif"],
            }
            recettes.append(recette)

        return recettes

    def get_recette_by_id(self, recette_id):
        """Récupère une recette spécifique par son ID."""
        query = (
            """
            SELECT id_recette, nom_recette, categorie, origine, instructions,
                   mots_cles, url_image, liste_ingredients, nombre_avis,
                   note_moyenne, date_derniere_modif
            FROM {}.recette
            WHERE id_recette = %s
        """
        ).format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (recette_id,))
                row = cursor.fetchone()

        if row:
            recette = {
                "id_recette": row["id_recette"],
                "nom_recette": row["nom_recette"],
                "categorie": row["categorie"],
                "origine": row["origine"],
                "instructions": row["instructions"],
                "mots_cles": row["mots_cles"],
                "url_image": row["url_image"],
                "liste_ingredients": row["liste_ingredients"],
                "nombre_avis": row["nombre_avis"],
                "note_moyenne": row["note_moyenne"],
                "date_derniere_modif": row["date_derniere_modif"],
            }
            return recette
        return None

    def get_recette_by_nom_recette(self, nom_recette):
        """Récupère une recette spécifique par son nom."""
        query = (
            """
            SELECT id_recette, nom_recette, categorie, origine, instructions,
                   mots_cles, url_image, liste_ingredients, nombre_avis,
                   note_moyenne, date_derniere_modif
            FROM {}.recette
            WHERE nom_recette = %s
            """
        ).format(self.schema)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (nom_recette,))
                row = cursor.fetchone()

        if row:
            recette = {
                "id_recette": row["id_recette"],
                "nom_recette": row["nom_recette"],
                "categorie": row["categorie"],
                "origine": row["origine"],
                "instructions": row["instructions"],
                "mots_cles": row["mots_cles"],
                "url_image": row["url_image"],
                "liste_ingredients": row["liste_ingredients"],
                "nombre_avis": row["nombre_avis"],
                "note_moyenne": row["note_moyenne"],
                "date_derniere_modif": row["date_derniere_modif"],
            }
            return recette
        return None

    def ajouter_recette(self, recette: Recette):

        try:
            res = None
            with self.connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projet_informatique.recette (nom_recette, "
                    " categorie, origine, instructions, mots_cles, "
                    " url_image, liste_ingredients, nombre_avis, "
                    "note_moyenne, date_derniere_modif) "
                    "VALUES (%(nom_recette)s, %(categorie)s, %(origine)s, %(instructions)s,"
                    " %(mots_cles)s, %(url_image)s, %(liste_ingredients)s, %(nombre_avis)s,"
                    " %(note_moyenne)s, %(date_derniere_modif)s)"
                    "RETURNING id_recette;",
                    {
                        "nom_recette": recette.nom_recette,
                        "categorie": recette.categorie,
                        "origine": recette.origine,
                        "instructions": recette.instructions,
                        "mots_cles": recette.mots_cles,
                        "url_image": recette.url_image,
                        "liste_ingredients": recette.liste_ingredients,
                        "nombre_avis": recette.nombre_avis,
                        "note_moyenne": recette.note_moyenne,
                        "date_derniere_modif": recette.date_derniere_modif,
                    },
                )
                res = cursor.fetchone()
            # created = False
            if res:
                recette.id_recette = res["id_recette"]
                # created = True

        except Exception as e:
            self.connection.rollback()
            print(f"Erreur lors de l'insertion de la recette: {e}")
            return None

    def add_recette(
        self,
        nom_recette,
        categorie,
        origine,
        instructions,
        liste_ingredients,
        nombre_avis,
        mots_cles,
        url_image,
        note_moyenne,
        date_derniere_modif,
    ):
        """Ajoute une nouvelle recette."""
        query = """
            INSERT INTO projet_informatique.recette (nom_recette,categorie,origine,instructions,
            liste_ingredients,nombre_avis,mots_cles,url_image,note_moyenne,date_derniere_modif)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id_recette
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    query,
                    (
                        nom_recette,
                        categorie,
                        origine,
                        instructions,
                        liste_ingredients,
                        nombre_avis,
                        mots_cles,
                        url_image,
                        note_moyenne,
                        date_derniere_modif,
                    ),
                )
                return cursor.fetchone()

    def update_by_recette_id(self, recette_id, **kwargs):
        """Met à jour une recette existante."""
        # Construire dynamiquement la partie SET avec des Identifiers sécurisés
        set_clause = sql.SQL(", ").join(
            sql.SQL("{} = %s").format(sql.Identifier(key)) for key in kwargs
        )

        query = sql.SQL(
            """
                UPDATE {}.recette
                SET {}
                WHERE id_recette = %s
            """
        ).format(sql.Identifier(self.schema), set_clause)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), recette_id))
                connection.commit()

    def update_by_nom_recette(self, nom_recette, **kwargs):
        """Met à jour une recette existante."""
        # Construire dynamiquement la partie SET avec des Identifiers sécurisés
        set_clause = sql.SQL(", ").join(
            sql.SQL("{} = %s").format(sql.Identifier(key)) for key in kwargs
        )

        query = sql.SQL(
            """
                UPDATE {}.recette
                SET {}
                WHERE nom_recette = %s
            """
        ).format(sql.Identifier(self.schema), set_clause)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), nom_recette))
                connection.commit()

    def delete_recette(self, recette_id):
        """Supprime une recette par son ID."""
        query = (
            """DELETE FROM {}.recette
                WHERE id_recette = %s
                """
        ).format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (recette_id,))

    def somme_note_by_recette(self, recette_id):
        """Réalise la somme des notes d'une recette données"""
        query = """ SELECT note FROM projet_informatique.avis
                WHERE id_recette = %s """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (recette_id,))
                rows = cursor.fetchall()
        notes = [row["note"] for row in rows]
        n = len(notes)
        self.update_by_recette_id(recette_id, nombre_avis=n)
        somme = 0
        if n == 0:
            return None
        else:
            for note in notes:
                somme += note
            somme = somme / len(notes)
            return somme


if __name__ == "__main__":
    pass
    # print(RecetteDAO().somme_note_by_recette(1))
    # print(RecetteDAO().get_recette_by_id(1))
    # print(RecetteDAO().get_all_recettes())

    # print("update par id")
    # print(RecetteDAO().update_by_recette_id(1, nom_recette="Tarte"))  # marche

    # print("update par nom")
    # print(RecetteDAO().update_by_nom_recette("Burek", categorie="exemple de dessert"))  # marche

    # RecetteDAO().ajouter_recette(
    #     "Exemple Recette",  # nom_recette
    #     "Dessert",  # categorie
    #     "British",  # origine
    #     "Touiller / Remuer / Mélanger / Agiter",  # instructions
    #     None,  # mots_cles (ici None, donc NULL en base)
    #     None,  # url_image (None si non fourni)
    #     ["Butter", "Jam"],  # liste_ingredients (un tableau en Python)
    #     None,  # nombre_avis (None signifie pas encore d'avis)
    #     None,  # note_moyenne (pas encore de notes)
    #     datetime.now(),  # date_derniere_modif (date d'aujourd'hui)
    # )
