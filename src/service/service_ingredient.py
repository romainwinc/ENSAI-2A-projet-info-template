class IngredientService:
    def __init__(self, ingredient_dao):
        self.ingredient_dao = ingredient_dao

    # Méthodes pours les ingrédients favoris
    def recuperer_ingredients_favoris_utilisateur(self, utilisateur_id: int):
        """Récupère les ingrédients favoris d'un utilisateur."""
        ingredients_favoris = self.ingredients_favoris_dao.get_favoris_by_user_id(utilisateur_id)

        if not ingredients_favoris:
            print("Vous n'avez aucun ingrédient favoris.")
            return

        print("\nVoici vos ingrédients favoris :\n")
        for ingredient in ingredients_favoris:
            print(f"- {ingredient.nom}")

    def supprimer_ingredients_favoris(self, utilisateur_id: int, ingredient_id: int):
        """Supprime un ingrédient favori d'un utilisateur."""
        success = self.ingredients_favoris_dao.delete_favori(utilisateur_id, ingredient_id)
        if success:
            print(f"L'ingrédient favori avec l'ID {ingredient_id} a été supprimé.")
        else:
            print("Erreur lors de la suppression de l'ingrédient favori.")

    def ajouter_ingredients_favoris(self, utilisateur_id: int, ingredient_id: int):
        """Ajouter un ingrédient favori à un utilisateur."""
        success = self.ingredients_favoris_dao.delete_favori(utilisateur_id, ingredient_id)
        if success:
            print(f"L'ingrédient favori avec l'ID {ingredient_id} a été ajouté.")
        else:
            print("Erreur lors de l'ajout de l'ingrédient favori.")

    # Méthodes pours les ingrédients non-désirés
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
            print(f"- {ingredient.nom}")

    def supprimer_ingredients_non_desires(self, utilisateur_id: int, ingredient_id: int):
        """Supprime un ingrédient non-désiré d'un utilisateur."""
        success = self.ingredients_non_desires_dao.delete_non_desire(utilisateur_id, ingredient_id)
        if success:
            print(f"L'ingrédient non-désiré avec l'ID {ingredient_id} a été supprimé.")
        else:
            print("Erreur lors de la suppression de l'ingrédient non-désiré.")

    def ajouter_ingredients_non_desires(self, utilisateur_id: int, ingredient_id: int):
        """Ajoute un ingrédient non-désiré à un utilisateur."""
        success = self.ingredients_non_desires_dao.add_ingredient_non_desire(
            utilisateur_id, ingredient_id
        )
        if success:
            print(f"L'ingrédient non-désiré avec l'ID {ingredient_id} a été ajouté.")
        else:
            print("Erreur lors de l'ajout de l'ingrédient non-désiré.")

    # Méthodes pour la liste de course
    def afficher_ingredients_liste_courses(self, utilisateur_id: int):
        """Récupère les ingrédients de la liste de course d'un utilisateur."""
        ingredients_liste_courses = self.liste_de_courses_dao.get_liste_by_user_id(utilisateur_id)

        if not ingredients_liste_courses:
            print("Vous n'avez aucun ingrédient dans votre liste de courses.")
            return

        print("\nVoici les ingrédients de votre liste de courses :\n")
        for ingredient in ingredients_liste_courses:
            print(f"- {ingredient.nom}")

    def supprimer_ingredients_liste_courses(
        self, utilisateur_id: int, recette_id: int, ingredient_id: int
    ):
        """Supprime un ingrédient de la liste de courses d'un utilisateur."""
        success = self.liste_de_courses_dao.delete_from_liste(
            ingredient_id, recette_id, utilisateur_id
        )
        if success:
            print(f"L'ingrédient avec l'ID {ingredient_id} a été supprimé de la liste de courses.")
        else:
            print("Erreur lors de la suppression de l'ingrédient de la liste de course.")

    def ajouter_ingredients_liste_courses(
        self, utilisateur_id: int, recette_id: int, ingredient_id: int
    ):
        """Ajoute un ingrédient à la liste de course d'un utilisateur."""
        success = self.liste_de_courses_dao.add_liste_de_courses(
            ingredient_id, recette_id, utilisateur_id
        )
        if success:
            print(f"L'ingrédient avec l'ID {ingredient_id} a été ajouté à la liste de courses.")
        else:
            print("Erreur lors de l'ajout de l'ingrédient à la liste de courses.")
