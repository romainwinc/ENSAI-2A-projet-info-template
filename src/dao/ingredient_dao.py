from dao.db_connection import DBConnection

class UneClasseDAO(metaclass=Singleton):

    def une_methode_dao():

        # Etape 1 : On récupère la connexion en utilisant la classe DBConnection.
        with DBConnection().connection as connection :
        
            # Etape 2 : à partir de la connexion on crée un curseur pour la requête 
            with connection.cursor() as cursor : 
            
                # Etape 3 : on exécute notre requête SQL
                cursor.execute(requete_sql)

                # Etape 4 : on stocke le résultat de la requête
                res = cursor.fetchall()

        if res:
            # Etape 5 : on agence les résultats selon la forme souhaitée (objet, liste...)

        return something