from models.ingredient import Ingredient
from models.avis import Avis
from datetime import datetime


class Recette:
    """
    Représente une recette avec ses détails, ses ingrédients, ses avis et sa note.

    Attributs :
        id_recette (int): L'identifiant unique de la recette.
        nom_recette (str): Le nom de la recette.
        categorie (str): La catégorie de la recette (entrée, plat, dessert, végétarien, etc.).
        origine (str): Le pays d'origine de la recette.
        instructions (str): Les instructions détaillées sur les étapes de la recette.
        mots_cles (str ou None): Les mots-clés associés à la recette (optionnel).
        url_image (str ou None): L'URL de l'image représentant la recette (optionnel).
        liste_ingredients (list[Ingredient]): Liste des ingrédients nécessaires à la recette.
        liste_avis (list[Avis] ou None): Liste des avis laissés par les utilisateurs pour cette recette (optionnel).
        nombre_avis (int): Le nombre d'avis de la recette.
        note_moyenne (float ou None): La moyenne des notes données à la recette (optionnel).
        date_derniere_modif (datetime): La date de la dernière modification de la recette.
    """

    def __init__(
        self,
        id_recette: int,
        nom_recette: str,
        categorie: str,
        origine: str,
        instructions: str,
        liste_ingredients: list[Ingredient],
        nombre_avis: int,
        date_derniere_modif: datetime = datetime.now(),
        mots_cles: str = None,
        url_image: str = None,
        note_moyenne: float = None,
        liste_avis: list[Avis] = None,
    ) -> None:
        """
        Initialise une nouvelle recette.

        Paramètres :
            id_recette (int): L'identifiant unique de la recette.
            nom_recette (str): Le nom de la recette.
            categorie (str): La catégorie de la recette (entrée, plat, dessert, végétarien, etc.).
            origine (str): Le pays d'origine de la recette.
            instructions (str): Les instructions détaillées sur les étapes de la recette.
            liste_ingredients (list[Ingredient]): Liste des ingrédients nécessaires à la recette.
            nombre_avis (int): Le nombre d'avis de la recette.
            date_derniere_modif (datetime, optionnel): La date de la dernière modification de la recette.
                          Par défaut, c'est la date et l'heure actuelles.
            mots_cles (str, optionnel): Les mots-clés associés à la recette. Par défaut, c'est None.
            url_image (str, optionnel): L'URL de l'image représentant la recette. Par défaut, c'est None.
            note_moyenne (float, optionnel): La moyenne des notes données à la recette. Par défaut, c'est None.
            liste_avis (list[Avis], optionnel): Liste des avis laissés pour la recette. Par défaut, c'est None.
        """
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
        """
        Retourne une représentation sous forme de chaîne de la recette.

        Retourne :
            str: Une chaîne de caractères contenant les détails de la recette, incluant
                 son nom, sa catégorie, son origine, ses instructions, ses ingrédients,
                 sa note moyenne et la date de la dernière modification.
        """
        return (
            f"Recette: {self.nom_recette}\n"
            f"Catégorie: {self.categorie}\n"
            f"Origine: {self.origine}\n"
            f"Instructions: {self.instructions}\n"
            f'Mots-clés: {self.mots_cles if self.mots_cles else "Aucun"}\n'
            f"Ingrédients:{self.liste_ingredients}\n"
            f"Note:{self.note_moyenne}/5\n"
            f"Date de la dernière modification:{self.date_derniere_modif.strftime('%d-%m-%Y')}"
        )
