from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session
from dao.ingredient_dao import IngredientDAO
from dao.ingredients_favoris_dao import IngredientsFavorisDAO
from dao.ingredients_non_desires_dao import IngredientsNonDesiresDAO
from dao.liste_de_courses_dao import ListeDeCoursesDAO
from service.service_ingredient import ServiceIngredient


class IngredientsFavEtND(VueAbstraite):
    """Vue du menu des ingrédient favoris et des ingrédients non-désirés pour
    un professionnel

    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par le professionnel
    """

    def choisir_menu(self):
        """Choix du menu suivant du professionnel

        Return
        ------
        vue
            Retourne la vue choisie par le professionnel dans le terminal
        """

        print("\n" + "-" * 50 + "\nMes ingredients favoris et non-désires\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Ajouter des ingrédients favoris ou non-désirés",
                "Consulter mes ingrédients favoris",
                "Consulter mes ingrédients non-désirés",
                # "Consulter ma liste de course",
                "Retour au menu principal",
            ],
        ).execute()

        match choix:
            case "Ajouter des ingrédients favoris ou non-désirés":
                from view.secondaire_pro.recherche_ingredient import (
                    RechercheIngredientPro,
                )

                return RechercheIngredientPro()

            case "Consulter mes ingrédients favoris":
                self.afficher_favoris()
                return self

            case "Consulter mes ingrédients non-désirés":
                self.afficher_non_desires()
                return self

            # case "Consulter ma liste de course":
            #     self.afficher_liste_courses()
            #     return self

            case "Retour au menu principal":
                from view.menus_principaux.menu_professionnel import MenuProfessionnel

                return MenuProfessionnel()

    def afficher_favoris(self):
        """Affiche les ingrédients favoris."""
        id_utilisateur = Session().utilisateur.id_utilisateur
        ingredient_dao = IngredientDAO()
        favoris_dao = IngredientsFavorisDAO()
        non_desires_dao = IngredientsNonDesiresDAO()
        liste_courses_dao = ListeDeCoursesDAO()
        service_ingredient = ServiceIngredient(
            ingredient_dao, favoris_dao, non_desires_dao, liste_courses_dao
        )

        favoris = service_ingredient.recuperer_ingredients_favoris_utilisateur(id_utilisateur)

        # Vérifiez si l'utilisateur a des ingrédients favorites
        if not favoris:
            inquirer.select(
                message="",
                choices=["OK"],
            ).execute()
            return self

        # Afficher les ingredients favorites
        choix_menu = favoris + ["Retour au menu principal"]
        choix = inquirer.select(
            message="Sélectionnez un ingrédient pour plus de détails ou retournez au menu :",
            choices=choix_menu,
        ).execute()

        if choix in favoris:
            # Afficher les détails de l'ingrédient sélectionné
            ingredient_selectionne = choix
            Session().ouvrir_ingredient(ingredient_selectionne)
            from view.secondaire_pro.vue_detail_ingredient_fav import DetailIngredientFav

            return DetailIngredientFav().afficher()
        else:
            # Retourner au menu précédent
            return self

    def afficher_non_desires(self):
        """Affiche les ingrédients non-désirés."""
        id_utilisateur = Session().utilisateur.id_utilisateur
        ingredient_dao = IngredientDAO()
        favoris_dao = IngredientsFavorisDAO()
        non_desires_dao = IngredientsNonDesiresDAO()
        liste_courses_dao = ListeDeCoursesDAO()
        service_ingredient = ServiceIngredient(
            ingredient_dao, favoris_dao, non_desires_dao, liste_courses_dao
        )

        non_desires = service_ingredient.recuperer_ingredients_non_desires_utilisateur(
            id_utilisateur
        )

        # Vérifiez si l'utilisateur a des ingrédients non-désirés
        if not non_desires:
            inquirer.select(
                message="",
                choices=["OK"],
            ).execute()
            return self

        # Afficher les ingredients non-désirés
        choix_menu = non_desires + ["Retour au menu principal"]
        choix = inquirer.select(
            message="Sélectionnez un ingrédient pour plus de détails ou retournez au menu :",
            choices=choix_menu,
        ).execute()

        if choix in non_desires:
            # Afficher les détails de l'ingrédient sélectionné
            ingredient_selectionne = choix
            Session().ouvrir_ingredient(ingredient_selectionne)
            from view.secondaire_pro.vue_detail_ingredient_nd import DetailIngredientND

            return DetailIngredientND().afficher()
        else:
            # Retourner au menu précédent
            return self

    # def afficher_liste_courses(self):
    #     """Affiche les ingrédients de la liste de course."""
    #     id_utilisateur = Session().utilisateur.id_utilisateur
    #     ingredient_dao = IngredientDAO()
    #     favoris_dao = IngredientsFavorisDAO()
    #     non_desires_dao = IngredientsNonDesiresDAO()
    #     liste_courses_dao = ListeDeCoursesDAO()
    #     service_ingredient = ServiceIngredient(
    #         ingredient_dao, favoris_dao, non_desires_dao, liste_courses_dao
    #     )

    #     liste = service_ingredient.afficher_ingredients_liste_courses(id_utilisateur)

    #     # Vérifiez si l'utilisateur a des ingrédients dans sa liste de course
    #     if not liste:
    #         inquirer.select(
    #             message="",
    #             choices=["OK"],
    #         ).execute()
    #         return self

    #     # Afficher les ingredients de la liste de course
    #     choix_menu = liste + ["Retour au menu principal"]
    #     choix = inquirer.select(
    #         message="Sélectionnez un ingrédient pour plus de détails ou retournez au menu :",
    #         choices=choix_menu,
    #     ).execute()

    #     if choix in liste:
    #         # Afficher les détails de l'ingrédient sélectionné
    #         ingredient_selectionne = choix
    #         Session().ouvrir_ingredient(ingredient_selectionne)
    #         from view.secondaire_pro.vue_detail_ingredient_liste_courses import (
    #             DetailIngredientListeCourses,
    #         )

    #         return DetailIngredientListeCourses().afficher()
    #     else:
    #         # Retourner au menu précédent
    #         return self
