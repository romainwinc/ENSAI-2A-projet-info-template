from models.ingredient import Ingredient
from models.avis import Avis
from datetime import date


class Recette:
    """Une recette est caractérisée par son id, elle possède un nom,
    une catégorie, une origine, des instructions, des ingrédients, des avis
    une note et la date de sa dernière modification.

    Parameters
    ----------
    id_recette: int
        identifiant de la recette
    nom_recette: str
        nom de la recette
    categorie: str
        categorie de la recette (entrée, plat, dessert, végétarien, type de
        viande, ...)
    origine: str
        pays d'origine de la recette
    instruction: str
        Instructions sur les étapes de la recette
    mots_cles: str | None
        mots clés de la recette
    url_image: str | None
        URL vers l'image représenatnt la recette
    liste_ingredient: list[dict]
        Liste des ingrédients de la recette avec pour chaque ingrédient,
        la quantité nécéssaire pour la recette
    liste_avis: list[Avis] | None
        liste des avis laissés pour cette recette par les utilisateurs
    nombre_avis: int
        nombre d'avis de la recette
    note_moyenne: float | None
        moyenne des notes laissé par les utilisateurs
    date_derniere_modif: date
        date de la dernière modification de la recette
    """

    def __init__(
        self,
        id_recette: int,
        nom_recette: str,
        categorie: str,
        origine: str,
        instructions: str,
        liste_ingredients: list[dict],
        nombre_avis: int,
        date_derniere_modif: date,
        mots_cles: str = None,
        url_image: str = None,
        note_moyenne: float = None,
        liste_avis: list[Avis] = None,
    ) -> None:

        self.id_recette = id_recette
        self.nom_recette = nom_recette
        self.categorie = categorie
        self.origine = origine
        self.instructions = instructions
        self.mots_cles = mots_cles
        self.url_image = url_image
        self.liste_ingredients = liste_ingredients
        self.liste_avis = liste_avis
        self.nombre_avis = len(liste_avis) if liste_avis else 0
        self.note_moyenne = note_moyenne
        self.date_derniere_modif = date_derniere_modif

    def __repr__(self) -> str:
        ingredients = []

        ingredients_str = ", ".join(
            [f"{ingredient[0]}: {ingredient[1]}" for ingredient in self.liste_ingredients]
        )

        # avis_str = ", ".join(
        #     [f"{avis.auteur}: {avis.note}/5 - {avis.commentaire}" for avis in self.liste_avis]
        # )

        return (
            f"Recette: {self.nom_recette}\n"
            f"Catégorie: {self.categorie}\n"
            f"Origine: {self.origine}\n"
            f"Instructions: {self.instructions}\n"
            f'Mots-clés: {self.mots_cles if self.mots_cles else "Aucun"}\n'
            f"Ingrédients:{self.liste_ingredients}\n"
            # f"Ingrédients:\n{ingredients_str}\n"
            f"Note:{self.note_moyenne}/5\n"
            # f"Avis: [{avis_str}]\n"
            f"Date de la dernière modification:{self.date_derniere_modif.strftime('%d-%m-%Y')}"
        )
