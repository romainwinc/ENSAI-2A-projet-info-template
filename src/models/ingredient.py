class Ingredient:
    """
    Classe représentant un ingrédient.

    Attributes:
        id_ingredient (int): L'identifiant unique de l'ingrédient.
        nom_ingredient (str): Le nom de l'ingrédient.
        description_ingredient (str): La description de l'ingrédient.
    """

    def __init__(
        self,
        nom_ingredient: str,
        description_ingredient: str,
        id_ingredient: int = None,
    ):
        """
        Initialise un nouvel ingrédient.

        Parameters:
            id_ingredient (int): L'identifiant unique de l'ingrédient.
            nom_ingredient (str): Le nom de l'ingrédient.
            description_ingredient (str): La description de l'ingrédient.
        """
        self.id_ingredient = id_ingredient
        self.nom_ingredient = nom_ingredient
        self.description_ingredient = description_ingredient

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de l'ingrédient.

        Returns:
            str: Une chaîne contenant les détails de l'ingrédient.
        """
        return (
            f"ID Ingrédient: {self.id_ingredient}\n"
            f"Nom de l'ingrédient: {self.nom_ingredient}\n"
            f"Description: {self.description_ingredient}"
        )
