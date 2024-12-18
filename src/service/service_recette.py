from dao.recette_dao import RecetteDAO
from dao.recette_favorite_dao import RecetteFavoriteDAO
from models.recette import Recette
from datetime import datetime


class ServiceRecette:
    def __init__(self, recette_dao: RecetteDAO, recette_favorite_dao: RecetteFavoriteDAO):
        self.recette_dao = recette_dao
        self.recette_favorite_dao = recette_favorite_dao

    def rechercher_par_nom_recette(self, nom_recette: str) -> list[Recette]:
        """
        Recherche les recettes par leur nom.
        """
        recettes = self.recette_dao.get_all_recettes()
        return [
            Recette(**recette)
            for recette in recettes
            if nom_recette.lower() in recette["nom_recette"].lower()
        ]

    def rechercher_par_id_recette(self, recette_id: int) -> Recette | None:
        """
        Recherche une recette par son ID.
        """
        recette_data = self.recette_dao.get_recette_by_id(recette_id)
        if recette_data:
            return [Recette(**recette_data)]
        return None

    def rechercher_par_ingredient(self, nom_ingredient: str) -> list[Recette]:
        """
        Recherche les recettes contenant un ingrédient spécifique.
        """
        recettes = self.recette_dao.get_all_recettes()
        recettes_avec_ingredient = []

        for recette_data in recettes:
            ingredients = recette_data["liste_ingredients"]

            # Vérifier si l'ingrédient est dans la liste des ingrédients
            if any(nom_ingredient.lower() in ingredient.lower() for ingredient in ingredients):
                recettes_avec_ingredient.append(Recette(**recette_data))

        return recettes_avec_ingredient

    def creer_recette(
        self,
        nom_recette: str,
        categorie: str,
        origine: str,
        instructions: str,
        liste_ingredients: list[str],
        nombre_avis: int = 0,
        mots_cles: str = None,
        url_image: str = None,
        note_moyenne: float = None,
        date_derniere_modif: datetime = datetime.now(),
    ) -> int:
        """
        Crée une nouvelle recette et retourne son ID.
        """
        recette_id = self.recette_dao.add_recette(
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
        )
        return recette_id

    def modifier_recette_id(self, recette_id: int, **kwargs) -> bool:
        """
        Modifie une recette existante. Les champs à mettre à jour sont passés en tant que
        paramètres.
        """
        recette_existante = self.recette_dao.get_recette_by_id(recette_id)
        if not recette_existante:
            print(f"Recette avec ID {recette_id} non trouvée.")
            return False

        self.recette_dao.update_by_recette_id(recette_id, **kwargs)
        return True

    def modifier_recette_nom_recette(self, nom_recette: int, **kwargs) -> bool:
        """
        Modifie une recette existante. Les champs à mettre à jour sont passés en tant que
        paramètres.
        """
        recette_existante = self.recette_dao.get_recette_by_nom_recette(nom_recette)
        if not recette_existante:
            print(f"Recette avec ID {nom_recette} non trouvée.")
            return False

        self.recette_dao.update_by_nom_recette(nom_recette, **kwargs)
        return True

    def supprimer_recette(self, recette_id: int) -> bool:
        """
        Supprime une recette par son ID.
        """
        recette_existante = self.recette_dao.get_recette_by_id(recette_id)
        if not recette_existante:
            print(f"Recette avec ID {recette_id} non trouvée.")
            return False

        self.recette_dao.delete_recette(recette_id)
        print(f"Recette avec ID {recette_id} supprimée.")
        return True

    def afficher_recette(self, recette_id: int) -> str:
        """
        Affiche une recette formatée par son ID.
        """
        note = self.recette_dao.somme_note_by_recette(recette_id)
        recette = self.recette_dao.update_by_recette_id(recette_id, note_moyenne=note)
        recette = self.recette_dao.get_recette_by_id(recette_id)
        if recette:
            recette = Recette(
                id_recette=recette["id_recette"],
                nom_recette=recette["nom_recette"],
                categorie=recette["categorie"],
                origine=recette["origine"],
                instructions=recette["instructions"],
                liste_ingredients=recette["liste_ingredients"],
                nombre_avis=recette["nombre_avis"],
                date_derniere_modif=recette["date_derniere_modif"],
                mots_cles=recette["mots_cles"],
                url_image=recette["url_image"],
                note_moyenne=recette["note_moyenne"],
            )
            return recette.__repr__
        return f"Aucune recette trouvée avec l'ID {recette_id}."

    # Section recette favorites

    def ajouter_recette_favorite(self, nom_recette: str, id_utilisateur: int) -> str:
        """Ajoute une recette aux favoris de l'utilisateur et renvoie un message de confirmation."""
        if self.recette_favorite_dao.is_recette_in_favoris(nom_recette, id_utilisateur):
            print(f"La recette '{nom_recette}' est déjà dans vos favoris.")
            return False

        # Ajouter la recette si elle n'est pas déjà en favoris
        self.recette_favorite_dao.add_recette_favorite(nom_recette, id_utilisateur)
        print(
            f"La recette '{nom_recette}' a été ajoutée aux favoris de l'utilisateur "
            f"{id_utilisateur}."
        )
        return True

    def supprimer_recette_favorite(self, nom_recette: str, id_utilisateur: int) -> str:
        """
        Supprime une recette des favoris de l'utilisateur et renvoie un message de confirmation.
        """
        self.recette_favorite_dao.delete_recette_favorite(nom_recette, id_utilisateur)
        # print(
        #     f"La recette '{nom_recette}' a été supprimée des favoris de l'utilisateur
        #     f"{id_utilisateur}."
        # )

    def afficher_recettes_favorites(self, id_utilisateur: int) -> list[str]:
        """
        Affiche toutes les recettes favorites d'un utilisateur.
        """
        favoris = self.recette_favorite_dao.get_favoris_by_user_id(id_utilisateur)

        if not favoris:
            print("Vous n'avez pas de recettes favorites.")
        else:
            print("Voici vos recettes favorites")
            print(favoris)
            return favoris

    def proposition_recette(self, id_user):
        """
        Donne un ou des noms de recette qu'un utilisateur n'a pas en
        recettes favorites et qui contient au moins un igredient favori
        et aucun ingredient non désiré.
        """
        liste = []
        liste = self.recette_favorite_dao.proposition_recette_sans_ingredient_non_désire(
            id_utilisateur=id_user
        )
        return liste


if __name__ == "__main__":
    dao = RecetteDAO()
    recette_favorite_dao = RecetteFavoriteDAO()  # Instanciation de la DAO des recettes favorites
    service_recette = ServiceRecette(dao, recette_favorite_dao)
    pass
    # service_recette.proposition_recette(1)
    # print("id")
    # print(service_recette.rechercher_par_id_recette(1))  # marche
    # print("Nom")
    # print(service_recette.rechercher_par_nom_recette("Apple Frangipan Tart"))  # marche
    # print("ingredient")
    # print(service_recette.rechercher_par_ingredient("digestive biscuits"))  # marche
    # print("supprimer")
    # print(service_recette.supprimer_recette(2))  # marche
    # print("modifier un argument")
    # print(service_recette.modifier_recette_id(1, nom_recette="Tarte crème"))  # marche
    # print("modifier un argument")
    # print(service_recette.modifier_recette_nom_recette("Ayam Percik", categorie="Viande"))
    # # marche

    # print("stock dans la base de donnée")
    # print(service_recette.creer_recette(
    #     "Exemple Recette",
    #     "Dessert",
    #     "British",
    #     "Touiller / Remuer / Mélanger / Agiter",
    #     ["Butter", "Jam"],
    # ))

    # # Afficher une recette
    # print(service_recette.afficher_recette(1))  # Marche mais est peut être redondant
    # service_recette.afficher_recettes_favorites(1)
    # ServiceRecette(dao).afficher_recette(1)  # Marche mais est peut être redondant

    # Nouvelles fonctionnalitées ici qui marchent
    # Exemple d'utilisation des nouvelles méthodes
    # service_recette.ajouter_recette_favorite(
    #     "Apple Frangipan Tart", 2
    # )  # Ajoute 'Apple Frangipan Tart' aux favoris de l'utilisateur 1
    # # print(service_recette.afficher_recettes_favorites(1))
    # # Affiche les recettes favorites de l'utilisateur 1
    # service_recette.enlever_recette_favorite("Apple Frangipan Tart", 1)
    # # Enlève 'Apple Frangipan Tart' des favoris de l'utilisateur 1
