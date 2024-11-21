from view.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from view.session import Session
from dao.recette_favorite_dao import RecetteFavoriteDAO
from dao.recette_dao import RecetteDAO
from service.service_recette import ServiceRecette
from service.service_avis import ServiceAvis
from dao.avis_dao import AvisDAO


class VueDetailRecette(VueAbstraite):
    """Vue pour afficher les détails d'une recette."""

    def choisir_menu(self):
        """Implémentation requise de la méthode abstraite, sans effet ici."""
        pass

    def afficher(self):
        """Affiche les détails de la recette."""
        recette = Session().recette
        print("\n" + "-" * 50 + "\nDétails de la Recette\n" + "-" * 50 + "\n")
        print(f"{recette}")

        # Permet de revenir au menu principal ou à la recherche
        from view.secondaire_pro.recherche_recette import RechercheRecettePro

        choix = inquirer.select(
            message="Que souhaitez-vous faire ensuite ?",
            choices=[
                "Voir les avis de la recette",
                "Ajouter la recette à mes favoris",
                "Ajouter un avis",
                "Retour à la recherche",
            ],
            max_height=10,
        ).execute()

        utilisateur_id = Session().utilisateur.id_utilisateur
        recette_fav_dao = RecetteFavoriteDAO()
        recette_dao = RecetteDAO()
        recette_service = ServiceRecette(recette_dao, recette_fav_dao)

        match choix:
            case "Ajouter la recette à mes favoris":
                if recette_service.ajouter_recette_favorite(recette.nom_recette, utilisateur_id):
                    print("La recette a bien été ajoutée à vos favoris.")
                else:
                    inquirer.select(
                        message="",
                        choices=["OK"],
                    ).execute()
                return self
            case "Ajouter un avis":
                from view.secondaire_pro.vue_ajouter_avis import VueAjouterAvis

                vue_avis = VueAjouterAvis()
                vue_avis.afficher()
                return vue_avis
            case "Voir les avis de la recette":
                recette_id = Session().recette.id_recette
                dao = AvisDAO()
                avis_service = ServiceAvis(dao)
                avis_service.afficher_avis_par_recette(recette_id)
                inquirer.select(
                    message="",
                    choices=["Retour"],
                ).execute()
                return self
            case "Retour à la recherche":
                Session().fermer_recette()
                return RechercheRecettePro()
