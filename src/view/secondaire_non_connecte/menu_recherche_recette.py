from InquirerPy import inquirer
from dao.db_connection import DBConnection


class RechercheRecetteVue:
    """Vue pour rechercher une recette.

    Permet à l'utilisateur de rechercher une recette par nom ou ingrédient.
    """

    def choisir_menu(self):
        """Affiche le menu pour rechercher une recette.

        Return
        ------
        vue
            Retourne la vue suivante en fonction de la recherche de l'utilisateur.
        """
        print("\n" + "-" * 50 + "\nRecherche de Recette\n" + "-" * 50 + "\n")

        # Choix du type de recherche (par nom ou par ingrédient)
        type_recherche = inquirer.select(
            message="Choisissez le type de recherche :",
            choices=[
                "Rechercher par nom de recette",
                "Rechercher par ingrédient",
                "Retour au menu principal",
            ],
        ).execute()

        match type_recherche:
            case "Rechercher par nom de recette":
                self.rechercher_par_nom()
            case "Rechercher par ingrédient":
                self.rechercher_par_ingredient()
            case "Retour au menu principal":
                from view.menu_principal_vue import MenuPrincipalVue

                return MenuPrincipalVue()

    def rechercher_par_nom(self):
        """Permet la recherche d'une recette par nom."""
        nom_recette = inquirer.text(
            message="Entrez le nom de la recette : ",
            validate=lambda x: x != "",
            invalid_message="Le nom de la recette ne peut pas être vide.",
        ).execute()

        # Simule la recherche dans une base de données ou un appel à une API
        recette_trouvee = self.simuler_recherche_recette(nom_recette)
        if recette_trouvee:
            print(f"Recette trouvée : {recette_trouvee}")
            return self.choisir_menu()  # Retour au menu de recherche
        else:
            print(f"Aucune recette trouvée pour le nom '{nom_recette}'.")
            return self.choisir_menu()

    def rechercher_par_ingredient(self):
        """Permet la recherche d'une recette par ingrédient."""
        ingredient = inquirer.text(
            message="Entrez l'ingrédient : ",
            validate=lambda x: x != "",
            invalid_message="L'ingrédient ne peut pas être vide.",
        ).execute()

        # Simule la recherche dans une base de données ou un appel à une API
        recettes_trouvees = self.simuler_recherche_par_ingredient(ingredient)
        if recettes_trouvees:
            print(f"Recettes trouvées avec l'ingrédient '{ingredient}': {recettes_trouvees}")
            return self.choisir_menu()  # Retour au menu de recherche
        else:
            print(f"Aucune recette trouvée avec l'ingrédient '{ingredient}'.")
            return self.choisir_menu()

    def simuler_recherche_recette(self, nom_recette):
        """Simule la recherche d'une recette par nom.

        Parameters
        ----------
        nom_recette : str
            Le nom de la recette à rechercher.

        Returns
        -------
        str
            Retourne le nom de la recette trouvée ou None si aucune recette n'est trouvée.
        """
        # Simuler un appel API à TheMealDB ou une recherche dans la base de données
        query = "SELECT * FROM projet_informatique.recette_ingredient WHERE id_recette = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_recette,))
                return cursor.fetchall()
        if nom_recette in query:
            return nom_recette
        return None

    def simuler_recherche_par_ingredient(self, ingredient):
        """Simule la recherche de recettes par ingrédient.

        Parameters
        ----------
        ingredient : str
            L'ingrédient pour lequel rechercher des recettes.

        Returns
        -------
        list
            Retourne liste recettes contenant l'ingrédient ou None si aucune recette n'est trouvée
        """
        # Simuler une base de données de recettes avec ingrédients
        recettes_par_ingredient = {
            "pommes": ["Tarte aux pommes", "Compote de pommes"],
            "tomates": ["Pâtes à la bolognaise", "Salade de tomates"],
            "poulet": ["Salade César", "Poulet rôti"],
        }

        return recettes_par_ingredient.get(ingredient, None)
