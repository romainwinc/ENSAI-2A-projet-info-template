from dao.ingredient_dao import IngredientDAO
from dao.ingredients_favoris_dao import IngredientsFavorisDAO
from dao.ingredients_non_desires_dao import IngredientsNonDesiresDAO
from dao.liste_de_courses_dao import ListeDeCoursesDAO
from models.ingredient import Ingredient


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
            print(f"\nIngrédient ID: {ingredient['id_ingredient']}")
            print(f"Nom: {ingredient['nom_ingredient']}")
            print(f"Description: {ingredient['description_ingredient']}\n")
        else:
            print(f"Aucun ingrédient trouvé avec l'ID: {ingredient_id}")

    def ajouter_ingredient(self, nom_ingredient, description_ingredient):
        """Ajoute un nouvel ingrédient."""
        ingredient = Ingredient(
            id_ingredient=None,
            nom_ingredient=nom_ingredient,
            description_ingredient=description_ingredient,
        )
        if self.ingredient_dao.add_ingredient(ingredient):
            print(f"L'ingrédient '{nom_ingredient}' a été ajouté avec succès.")
        else:
            print("Erreur lors de l'ajout de l'ingrédient.")

    def modifier_ingredient(self, ingredient_id, **kwargs):
        """Modifie un ingrédient existant."""
        self.ingredient_dao.update_by_ingredient_id(ingredient_id, **kwargs)
        print(f"L'ingrédient avec ID {ingredient_id} a été modifié avec succès.")

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

    def supprimer_ingredients_favoris(self, utilisateur_id: int, nom_ingredient: str):
        """Supprime un ingrédient favori d'un utilisateur."""
        self.ingredients_favoris_dao.delete_ingredient_favori(nom_ingredient, utilisateur_id)
        print(f"L'ingrédient favori '{nom_ingredient}' a été supprimé.")

    def ajouter_ingredients_favoris(self, utilisateur_id: int, nom_ingredient: str):
        """Ajoute un ingrédient favori à un utilisateur."""
        self.ingredients_favoris_dao.add_ingredient_favori(nom_ingredient, utilisateur_id)
        print(f"L'ingrédient favori '{nom_ingredient}' a été ajouté.")

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

    def supprimer_ingredients_non_desires(self, utilisateur_id: int, nom_ingredient: str):
        """Supprime un ingrédient non-désiré d'un utilisateur."""
        self.ingredients_non_desires_dao.delete_ingredient_non_desire(
            nom_ingredient, utilisateur_id
        )
        print(f"L'ingrédient non-désiré '{nom_ingredient}' a été supprimé.")

    def ajouter_ingredients_non_desires(self, utilisateur_id: int, nom_ingredient: str):
        """Ajoute un ingrédient non-désiré à un utilisateur."""
        self.ingredients_non_desires_dao.add_ingredient_non_desire(nom_ingredient, utilisateur_id)
        print(f"L'ingrédient non-désiré '{nom_ingredient}' a été ajouté.")

    # Méthodes pour la liste de course
    def afficher_ingredients_liste_courses(self, utilisateur_id: int):
        """Récupère les ingrédients de la liste de course d'un utilisateur."""
        ingredients_liste_courses = self.liste_de_courses_dao.get_liste_de_courses_by_user_id(
            utilisateur_id
        )

        if not ingredients_liste_courses:
            print("Vous n'avez aucun ingrédient dans votre liste de courses.")
            return

        print("\nVoici les ingrédients de votre liste de courses :\n")
        for ingredient in ingredients_liste_courses:
            print(f"- {ingredient}")

    def supprimer_ingredients_liste_courses(self, utilisateur_id: int, nom_ingredient: str):
        """Supprime un ingrédient de la liste de courses d'un utilisateur."""
        self.liste_de_courses_dao.delete_ingredient_from_liste_de_courses(
            nom_ingredient, utilisateur_id
        )
        print(f"L'ingrédient '{nom_ingredient}' a été supprimé de la liste de courses.")

    def ajouter_ingredients_liste_courses(self, utilisateur_id: int, nom_ingredient: str):
        """Ajoute un ingrédient à la liste de course d'un utilisateur."""
        self.liste_de_courses_dao.add_liste_de_courses(nom_ingredient, utilisateur_id)
        print(f"L'ingrédient '{nom_ingredient}' a été ajouté à la liste de courses.")


if __name__ == "__main__":
    ingredient_dao = IngredientDAO()
    favoris_dao = IngredientsFavorisDAO()
    non_desires_dao = IngredientsNonDesiresDAO()
    liste_courses_dao = ListeDeCoursesDAO()

    service = ServiceIngredient(ingredient_dao, favoris_dao, non_desires_dao, liste_courses_dao)

    # Exemple d'utilisation :
    # service.ajouter_ingredient("Tomate", "Légume rouge utilisé dans de nombreux plats.")
    # service.afficher_ingredient(1)  # Affiche l'ingrédient avec ID 1
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
    # service.ajouter_ingredients_liste_courses(1, "Beef")  # Remplacez 1 par un ID utilisateur valide
    service.afficher_ingredients_liste_courses(1)
    # service.supprimer_ingredients_liste_courses(1, "Beef")
