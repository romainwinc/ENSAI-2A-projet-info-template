from InquirerPy import inquirer

from view.vue_abstraite import VueAbstraite
from view.session import Session


class MenuUtilisateurConnecte(VueAbstraite):
    """Vue du menu d'un utilisateur connecté (qui n'a pas de rôle spécial
    comme administrateur ou profeissionnel)

    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'utilisateur
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Principal\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter mes recettes favorites",
                "Chercher une recette",
                "Consulter mes notes et avis",
                "Consulter mes ingrédients favoris",
                "Consulter mes ingrédients non-désirés",
                "Proposer une recette",
                "Regarder ma liste de course",
                "Demander un compte professionnel",
                "Supprimer mon compte",
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Consulter mes recettes favorites":
                from View.recette_favorite import RecetteFavorite

                return RecetteFavorite()

            case "Chercher une recette":
                from View.recherche_recette import RechercheRecette

                return RechercheRecette()
            case "Consulter mes notes et avis":
                from View.consulter_mes_avis import ConsulterMesAvis

                return ConsulterMesAvis()
            case "Consulter mes ingrédients favoris":
                from View.ingredients_favoris import IngredientsFavoris

                return IngredientsFavoris()
            case "Consulter mes ingrédients non-désirés":
                from View.ingredients_non_desires import IngredientsNonDesires

                return IngredientsNonDesires()
            case "Demander un compte professionnel":
                from View.demande_compte_pro import DemandeComptePro

                return DemandeComptePro()
            case "Proposer une recette":
                from View.proposer_recette import ProposerRecette

                return ProposerRecette()
            case "Regarder ma liste de course":
                from View.ma_liste_de_course import MaListeDeCourse

                return MaListeDeCourse()
            case "Supprimer mon compte":
                from View.supprimer_compte import SupprimerCompte

                return SupprimerCompte()
            case "Se déconnecter":
                Session().deconnexion()
                from View.menu_non_connecte import MenuNonConnecte

                return MenuNonConnecte()
