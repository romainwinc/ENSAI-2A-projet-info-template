from InquirerPy import inquirer
from view.vue_abstraite import VueAbstraite
from dao.recette_dao import RecetteDAO
from service.service_recette import ServiceRecette
from models.recette import Recette


class RechercheRecetteNonConnecte(VueAbstraite):
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
                "Rechercher par id",
                "Retour au menu principal",
            ],
        ).execute()

        match type_recherche:
            case "Rechercher par nom de recette":
                self.rechercher_recette("nom")
            case "Rechercher par ingrédient":
                self.rechercher_recette("ingredient")
            case "Rechercher par id":
                self.rechercher_recette("id")
            case "Retour au menu principal":
                from view.accueil.accueil_vue import AccueilVue

                return AccueilVue()

    def rechercher_recette(self, type_recherche: str):
        """Recherche une recette en fonction du type de recherche sélectionné.

        Parameters
        ----------
        type_recherche : str
            Type de recherche ("nom", "ingredient" ou "id").
        """
        if type_recherche == "nom":
            nom_recette = inquirer.text(message="Entrez le nom de la recette :").execute()
            recettes = ServiceRecette(RecetteDAO()).rechercher_par_nom_recette(nom_recette)
            self.afficher_resultats(recettes)

        elif type_recherche == "ingredient":
            nom_ingredient = inquirer.text(message="Entrez le nom de l'ingrédient :").execute()
            recettes = ServiceRecette(RecetteDAO()).rechercher_par_ingredient(nom_ingredient)
            self.afficher_resultats(recettes)

        elif type_recherche == "id":
            recette_id = inquirer.number(message="Entrez l'ID de la recette :").execute()
            recette = ServiceRecette(RecetteDAO()).rechercher_par_id_recette(recette_id)
            self.afficher_resultats(recette)

    def afficher_resultats(self, recettes: Recette):
        """Affiche les résultats de recherche.

        Parameters
        ----------
        recettes : list
            Liste de recettes à afficher.
        """
        if recettes:
            for recette in recettes:
                print(f"Recette trouvée : {recette}")
        else:
            print("Aucune recette trouvée.")
