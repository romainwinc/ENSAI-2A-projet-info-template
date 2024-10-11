from non_connecte import Non_connecte
from ingredient import Ingredient
from recette import Recette


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
        id_utilisateur: str,
        nom_utilisateur: str,
        mot_de_passe: str,
        role: int = 1,
        date_inscription: datetime, 
        ingredients_favoris: list[Ingredient],
        recette_favorite: List[Recette],
        liste_course: List[Ingredient],
        liste_ingredient_favori: List[Ingredient],
        liste_ingredient_non_desires: List[Ingredient],
        
    ) -> None:
        self.nom = nom
        self.prenom = prenom
        self.username = username
        self.password = password
        self.ingredient_favori = ingredient_favori
        self.recette_favorite = recette_favorite
        self.liste_course = liste_course
        self.liste_ingredient_favori = liste_ingredient_favori
        self.liste_ingredient_non_desires = liste_ingredient_non_desires
        self.grade = grade

    def __repr__(self) -> str:
        """
        Renvoie une représentation lisible de l'utilisateur connecté.
        """
        return (
            f"Connecte(nom={self.nom}, prenom={self.prenom}, username={self.username}, "
            f"ingredient_favori={self.ingredient_favori}, recette_favorite={self.recette_favorite}, "
            f"liste_course={self.liste_course}, liste_ingredient_favori={self.liste_ingredient_favori}, "
            f"liste_ingredient_non_desires={self.liste_ingredient_non_desires}, grade={self.grade})"
        )
