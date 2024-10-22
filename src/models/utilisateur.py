from recette import Recette
from datetime import datetime
from ingredient import Ingredient


class Utilisateur:
    """
    Représente un utilisateur connecté avec des informations personnelles,
    des préférences alimentaires et une liste de courses.

    Parameters
    ----------
    nom : str
        Le nom de l'utilisateur.
    prenom : str
        Le prénom de l'utilisateur.
    username : str
        Le nom d'utilisateur pour la connexion.
    password : str
        Le mot de passe de l'utilisateur.
    ingredient_favori : list[Ingredient]
        Une liste d'ingrédients favoris de l'utilisateur.
    recette_favorite : list[Recette]
        Une liste de recettes favorites de l'utilisateur.
    liste_course : list[Ingredient]
        Une liste des ingrédients pour les courses de l'utilisateur.
    liste_ingredient_favori : list[Ingredient]
        Une liste d'ingrédients favoris.
    liste_ingredient_non_desires : list[Ingredient]
        Une liste d'ingrédients non désirés par l'utilisateur.
    grade : int
        Le grade ou niveau de l'utilisateur (par défaut, 1).
    """

    def __init__(
        self,
        nom_utilisateur: str,
        mot_de_passe: str,
        id_utilisateur: str = None,
        role: str = "Non connecté",
        date_inscription: datetime = None,
        ingredients_favoris: list(Ingredient) = [None],
        recette_favorite: list(Recette) = [None],
        liste_course: list(Ingredient) = [None],
        liste_ingredient_favori: list(Ingredient) = [None],
        liste_ingredient_non_desires: list(Ingredient) = [None],
    ) -> None:
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe = mot_de_passe
        self.id_utilisateur = id_utilisateur
        self.role = role
        self.date_inscription = date_inscription
        self.ingredients_favoris = ingredients_favoris
        self.recette_favorite = recette_favorite
        self.liste_course = liste_course
        self.liste_ingredient_favori = liste_ingredient_favori
        self.liste_ingredient_non_desires = liste_ingredient_non_desires

    def __repr__(self) -> str:
        """
        Renvoie une représentation lisible de l'utilisateur connecté.
        """
        return (
            f"Connecte(identifiant={self.id_utilisateur}, nom d'utilisateur={self.nom_utilisateur},"
            f"mot de passe ={self.mot_de_passe},ingredient_favori={self.ingredient_favori},"
            f"recette_favorite={self.recette_favorite},liste_course={self.liste_course}, "
            f"liste_ingredient_favori={self.liste_ingredient_favori}, "
            f"liste_ingredient_non_desires={self.liste_ingredient_non_desires}, role={self.grade})"
        )
