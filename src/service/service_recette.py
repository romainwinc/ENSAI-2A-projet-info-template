from dao.recette_dao import RecetteDAO
from models.recette import Recette


class ServiceRecette:
    def __init__(self, recette_dao: RecetteDAO):
        self.recette_dao = recette_dao

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
            return Recette(**recette_data)
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
            if any(
                nom_ingredient.lower() in ingredient["nom"].lower() for ingredient in ingredients
            ):
                recettes_avec_ingredient.append(Recette(**recette_data))
        return recettes_avec_ingredient

    def creer_recette(
        self,
        nom_recette: str,
        categorie: str,
        origine: str,
        instructions: str,
        mots_cles: str | None,
        url_image: str | None,
        liste_ingredients: list[dict],
        nombre_avis: int = 0,
        note_moyenne: float = None,
        date_derniere_modif: str = None,
    ) -> int:
        """
        Crée une nouvelle recette et retourne son ID.
        """
        recette_id = self.recette_dao.add_recette(
            nom_recette,
            categorie,
            origine,
            instructions,
            mots_cles,
            url_image,
            liste_ingredients,
            nombre_avis,
            note_moyenne,
            date_derniere_modif,
        )
        return recette_id

    def modifier_recette(self, recette_id: int, **kwargs) -> bool:
        """
        Modifie une recette existante. Les champs à mettre à jour sont passés en tant que paramètres.
        """
        recette_existante = self.recette_dao.get_recette_by_id(recette_id)
        if not recette_existante:
            print(f"Recette avec ID {recette_id} non trouvée.")
            return False

        self.recette_dao.update_recette(recette_id, **kwargs)
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
        recette = self.rechercher_par_id(recette_id)
        if recette:
            return recette.__repr__()
        return f"Aucune recette trouvée avec l'ID {recette_id}."


if __name__ == "__main__":
    dao = RecetteDAO()
    ServiceRecette(dao).rechercher_par_id_recette(1)
