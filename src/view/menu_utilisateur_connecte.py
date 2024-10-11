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
                "Consulter une recette",
                "Consulter mes notes et avis",
                "Consulter mes ingrédients favoris",
                "Consulter mes ingrédients non-désirés",
                "Proposer une recette",
                "Regarder ma liste de course",
                "Mon compte",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().deconnexion()
                from menu_non_connecte import MenuNonConnecte

                return MenuNonConnecte()

            case "Consulter les recettes favorites":

                return
            case "Consulter une recette":
                joueurs_str = JoueurService().afficher_tous()
                return MenuJoueurVue(joueurs_str)

            case "Afficher des pokemons (par appel à un Webservice)":
                from view.pokemon_vue import PokemonVue

                return PokemonVue()
