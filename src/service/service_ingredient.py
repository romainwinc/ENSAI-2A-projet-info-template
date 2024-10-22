class IngredientService:
    def __init__(self, ingredient_dao):
        self.ingredient_dao = ingredient_dao

    def recuperer_ingredients_non_desires_utilisateur(self, utilisateur_id):
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

    def recuperer_ingredients_favoris_utilisateur(self, utilisateur_id):
        """Récupère les ingrédients favoris d'un utilisateur."""
        ingredients_favoris = self.ingredients_favoris_dao.get_favoris_by_user_id(utilisateur_id)

        if not ingredients_favoris:
            print("Vous n'avez aucun ingrédient favoris.")
            return

        print("\nVoici vos ingrédients favoris :\n")
        for ingredient in ingredients_favoris:
            print(f"- {ingredient.nom}")

    def supprimer_ingredients_non_desires(self, utilisateur_id, ingredient_id):
        """Supprime un ingrédient non-désiré d'un utilisateur."""
        success = self.ingredients_non_desires_dao.delete_non_desire(utilisateur_id, ingredient_id)
        if success:
            print(f"L'ingrédient non-désiré avec l'ID {ingredient_id} a été supprimé.")
        else:
            print("Erreur lors de la suppression de l'ingrédient non-désiré.")

    def supprimer_ingredients_favoris(self, utilisateur_id, ingredient_id):
        """Supprime un ingrédient favori d'un utilisateur."""
        success = self.ingredients_favoris_dao.delete_favori(utilisateur_id, ingredient_id)
        if success:
            print(f"L'ingrédient favori avec l'ID {ingredient_id} a été supprimé.")
        else:
            print("Erreur lors de la suppression de l'ingrédient favori.")

    def ajouter_ingredients_non_desires(self, utilisateur_id, ingredient_id):
        """Ajoute un ingrédient non-désiré à un utilisateur."""
        success = self.ingredients_non_desires_dao.add_ingredient_non_desire(
            utilisateur_id, ingredient_id
        )
        if success:
            print(f"L'ingrédient non-désiré avec l'ID {ingredient_id} a été ajouté.")
        else:
            print("Erreur lors de l'ajout de l'ingrédient non-désiré.")

    def ajouter_ingredients_favoris(self, utilisateur_id, ingredient_id):
        """Ajouter un ingrédient favori à un utilisateur."""
        success = self.ingredients_favoris_dao.delete_favori(utilisateur_id, ingredient_id)
        if success:
            print(f"L'ingrédient favori avec l'ID {ingredient_id} a été ajouté.")
        else:
            print("Erreur lors de l'ajout de l'ingrédient favori.")
