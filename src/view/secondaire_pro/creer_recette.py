from view.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from datetime import datetime
from dao.recette_dao import RecetteDAO
from dao.recette_favorite_dao import RecetteFavoriteDAO
from service.service_recette import ServiceRecette


class CreerRecette(VueAbstraite):
    """Vue pour ajouter une recette pour un professionnel."""

    def choisir_menu(self):
        """Affiche les prompts pour ajouter une recette et soumet les informations."""
        print("\n" + "-" * 50 + "\nAjouter une Recette\n" + "-" * 50 + "\n")

        # Collecte des informations de la recette
        nom_recette = inquirer.text(message="Entrez le nom de la recette :").execute()
        categorie = inquirer.text(message="Entrez la catégorie de la recette :").execute()
        origine = inquirer.text(message="Entrez le pays d'origine de la recette :").execute()
        instructions = inquirer.text(message="Entrez les instructions de la recette :").execute()
        liste_ingredients = []

        while True:
            # Demande à l'utilisateur s'il veut ajouter un ingrédient ou terminer
            choix = inquirer.select(
                message="Que voulez-vous faire avec les ingrédients ?",
                choices=["Ajouter un ingrédient", "Terminer la liste des ingrédients"],
            ).execute()

            if choix == "Ajouter un ingrédient":
                # Si l'utilisateur choisit d'ajouter un ingrédient, on lui demande de le saisir
                ingredient = inquirer.text(message="Entrez le nom de l'ingrédient :").execute()
                liste_ingredients.append(ingredient)  # Ajouter l'ingrédient à la liste

            elif choix == "Terminer la liste des ingrédients":
                # Si l'utilisateur termine la liste, on quitte la boucle
                break

        nombre_avis = 0
        mots_cles = None
        url_image = None
        note_moyenne = None
        date_derniere_modif = datetime.now().strftime(
            "%Y-%m-%d"
        )  # Date actuelle au format AAAA-MM-JJ

        # Appel à la méthode ajouter_avis dans ServiceAvis
        dao_recette = RecetteDAO()
        dao_recette_fav = RecetteFavoriteDAO()
        service_recette = ServiceRecette(dao_recette, dao_recette_fav)
        service_recette.creer_recette(
            nom_recette=nom_recette,
            categorie=categorie,
            origine=origine,
            instructions=instructions,
            liste_ingredients=liste_ingredients,
            nombre_avis=nombre_avis,
            mots_cles=mots_cles,
            url_image=url_image,
            note_moyenne=note_moyenne,
            date_derniere_modif=date_derniere_modif,
        )

        print("\nMerci ! Votre recette a été ajoutée avec succès.")

        # Retourner à la vue de recherche
        from view.menus_principaux.menu_professionnel import MenuProfessionnel

        return MenuProfessionnel()
