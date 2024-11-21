from dao.ingredient_dao import IngredientDAO
from dao.ingredients_favoris_dao import IngredientsFavorisDAO
from dao.ingredients_non_desires_dao import IngredientsNonDesiresDAO
from dao.liste_de_courses_dao import ListeDeCoursesDAO
from models.ingredient import Ingredient
import logging


class ServiceIngredient:
    def __init__(self, ingredient_dao, favoris_dao, non_desires_dao, liste_courses_dao):
        self.ingredient_dao = ingredient_dao
        self.ingredients_favoris_dao = favoris_dao
        self.ingredients_non_desires_dao = non_desires_dao
        self.liste_de_courses_dao = liste_courses_dao

    # Méthodes pour afficher un ingrédient
    def afficher_ingredient(self, ingredient_id):
        """Affiche un ingrédient spécifique par son ID."""
        ingredient = self.ingredient_dao.get_ingredient_by_id(ingredient_id)
        if ingredient:
            logging.info(f"\nIngrédient ID: {ingredient['id_ingredient']}")
            logging.info(f"Nom: {ingredient['nom_ingredient']}")
            logging.info(f"Description: {ingredient['description_ingredient']}\n")
        else:
            logging.warning(f"Aucun ingrédient trouvé avec l'ID: {ingredient_id}")

    def ajouter_ingredient(self, nom_ingredient, description_ingredient):
        """Ajoute un nouvel ingrédient."""
        ingredient = Ingredient(
            id_ingredient=None,
            nom_ingredient=nom_ingredient,
            description_ingredient=description_ingredient,
        )
        if self.ingredient_dao.add_ingredient(ingredient):
            logging.info(f"L'ingrédient '{nom_ingredient}' a été ajouté avec succès.")
        else:
            logging.warning("Erreur lors de l'ajout de l'ingrédient.")

    def modifier_ingredient(self, ingredient_id, **kwargs):
        """Modifie un ingrédient existant."""
        self.ingredient_dao.update_by_ingredient_id(ingredient_id, **kwargs)
        print(f"L'ingrédient avec ID {ingredient_id} a été modifié avec succès.")

    def rechercher_par_nom_ingredient(self, nom_ingredient: str) -> list[Ingredient]:
        """
        Recherche les ingredients par leur nom.
        """
        ingredients = self.ingredient_dao.get_all_ingredients()
        return [
            Ingredient(**ingredient)
            for ingredient in ingredients
            if nom_ingredient.lower() in ingredient["nom_ingredient"].lower()
        ]

    # Méthodes pour les ingrédients favoris
    def recuperer_ingredients_favoris_utilisateur(self, utilisateur_id: int):
        """Récupère les ingrédients favoris d'un utilisateur."""
        ingredients_favoris = self.ingredients_favoris_dao.get_favoris_by_user_id(utilisateur_id)

        if not ingredients_favoris:
            print("Vous n'avez aucun ingrédient favoris.")
            return

        print("\nVoici vos ingrédients favoris :\n")
        for ingredient in ingredients_favoris:
            print(f"- {ingredient}")
        return ingredients_favoris

    def supprimer_ingredients_favoris(self, utilisateur_id: int, nom_ingredient: str):
        """Supprime un ingrédient favori d'un utilisateur."""
        self.ingredients_favoris_dao.delete_ingredient_favori(nom_ingredient, utilisateur_id)
        print(f"L'ingrédient '{nom_ingredient}' a été supprimé des favoris.")

    def ajouter_ingredients_favoris(self, utilisateur_id: int, nom_ingredient: str):
        """Ajoute un ingrédient favori à un utilisateur."""
        if self.ingredients_favoris_dao.is_ingredient_in_favoris(nom_ingredient, utilisateur_id):
            print(f"L'ingrédient '{nom_ingredient}' est déjà dans vos favoris.")
            return False
        self.ingredients_favoris_dao.add_ingredient_favori(nom_ingredient, utilisateur_id)
        print(f"L'ingrédient favori '{nom_ingredient}' a été ajouté.")
        return True

    # Méthodes pour les ingrédients non-désirés
    def recuperer_ingredients_non_desires_utilisateur(self, utilisateur_id: int):
        """Récupère les ingrédients non-désirés d'un utilisateur."""
        ingredients_non_desires = self.ingredients_non_desires_dao.get_non_desires_by_user_id(
            utilisateur_id
        )

        if not ingredients_non_desires:
            print("Vous n'avez aucun ingrédient non-désiré.")
            return

        print("\nVoici vos ingrédients non-désirés :\n")
        for ingredient in ingredients_non_desires:
            print(f"- {ingredient}")
        return ingredients_non_desires

    def supprimer_ingredients_non_desires(self, utilisateur_id: int, nom_ingredient: str):
        """Supprime un ingrédient non-désiré d'un utilisateur."""
        self.ingredients_non_desires_dao.delete_ingredient_non_desire(
            nom_ingredient, utilisateur_id
        )
        print(f"L'ingrédient '{nom_ingredient}' a été supprimé des non-désirés.")

    def ajouter_ingredients_non_desires(self, utilisateur_id: int, nom_ingredient: str):
        """Ajoute un ingrédient non-désiré à un utilisateur."""
        if self.ingredients_non_desires_dao.is_ingredient_in_non_desires(
            nom_ingredient, utilisateur_id
        ):
            print(f"L'ingrédient '{nom_ingredient}' est déjà dans vos non désirés.")
            return False
        self.ingredients_non_desires_dao.add_ingredient_non_desire(nom_ingredient, utilisateur_id)
        print(f"L'ingrédient non-désiré '{nom_ingredient}' a été ajouté.")
        return True

    # Méthodes pour la liste de course
    def afficher_ingredients_liste_courses(self, utilisateur_id: int):
        """Affiche les ingrédients de la liste de courses d'un utilisateur."""
        liste_courses = self.liste_de_courses_dao.get_liste_de_courses_by_user_id(utilisateur_id)
        if not liste_courses:
            print("Vous n'avez aucun ingrédient dans votre liste de courses.")
            return

        print("\nVoici les ingrédients de votre liste de courses :\n")
        for ingredient in liste_courses:
            print(f"- {ingredient}")
        return liste_courses

    def supprimer_ingredients_liste_courses(self, utilisateur_id: int, nom_ingredient: str):
        """Supprime un ingrédient de la liste de courses d'un utilisateur."""
        self.liste_de_courses_dao.delete_ingredient_from_liste_de_courses(
            nom_ingredient, utilisateur_id
        )
        print(f"L'ingrédient '{nom_ingredient}' a été supprimé de la liste de courses.")

    def ajouter_ingredients_liste_courses(self, utilisateur_id: int, nom_ingredient: str):
        """Ajoute un ingrédient à la liste de course d'un utilisateur."""
        if self.liste_de_courses_dao.is_ingredient_in_liste(nom_ingredient, utilisateur_id):
            print(f"L'ingrédient '{nom_ingredient}' est déjà dans votre liste de courses.")
            return False
        self.liste_de_courses_dao.add_liste_de_courses(nom_ingredient, utilisateur_id)
        print(f"L'ingrédient '{nom_ingredient}' a été ajouté à la liste de courses.")
        return True


if __name__ == "__main__":
    ingredient_dao = IngredientDAO()
    favoris_dao = IngredientsFavorisDAO()
    non_desires_dao = IngredientsNonDesiresDAO()
    liste_courses_dao = ListeDeCoursesDAO()

    service = ServiceIngredient(ingredient_dao, favoris_dao, non_desires_dao, liste_courses_dao)

    # Exemple d'utilisation :
    # service.ajouter_ingredient("Tomate", "Légume rouge utilisé dans de nombreux plats.")
    service.afficher_ingredient(1)  # Affiche l'ingrédient avec ID 1
    # service.modifier_ingredient(
    #  1, nom_ingredient="Chicken", description_ingredient="Légume rouge et juteux."
    # )

    # Favoris
    # service.ajouter_ingredients_favoris(1, "Tomate")  # Remplacez 1 par un ID utilisateur valide
    # service.recuperer_ingredients_favoris_utilisateur(1)
    # service.supprimer_ingredients_favoris(1, "Tomate")

    # # Non-désirés
    # service.ajouter_ingredients_non_desires(
    #     1, "Chicken"
    # )  # Remplacez 1 par un ID utilisateur valide
    # service.recuperer_ingredients_non_desires_utilisateur(1)
    # service.supprimer_ingredients_non_desires(1, "Chicken")

    # Liste de courses
    # service.ajouter_ingredients_liste_courses(1, "Beef")
    # # Remplacez 1 par un ID utilisateur valide
    # service.afficher_ingredients_liste_courses(1)
    # service.supprimer_ingredients_liste_courses(1, "Beef")
    # service.modifier_ingredient(
    #     1,
    #     nom_ingredient="Chicken",
    #     description_ingredient="Légume rouge et juteux.",
    # )
