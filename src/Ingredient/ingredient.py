class Ingredient:
    """
    Classe représentant un ingrédient avec ses attributs et sa description.

    Attributs :
    -----------
    idIngredient : str
        Identifiant unique de l'ingrédient.
    strIngredient : str
        Nom de l'ingrédient.
    strDescription : str
        Description détaillée de l'ingrédient, y compris son origine et son utilisation.
    strType : Optional[str]
        Type ou catégorie de l'ingrédient (peut être None si non défini).
    """

    def __init__(
        self, idIngredient: str, strIngredient: str, strDescription: str, strType: str = None
    ):
        """
        Initialise un objet Ingredient.

        Paramètres :
        ------------
        idIngredient : str
            Identifiant unique de l'ingrédient.
        strIngredient : str
            Nom de l'ingrédient.
        strDescription : str
            Description détaillée de l'ingrédient.
        strType : Optional[str]
            Type ou catégorie de l'ingrédient (valeur par défaut : None).
        """
        self.idIngredient = idIngredient
        self.strIngredient = strIngredient
        self.strDescription = strDescription
        self.strType = strType

    def __repr__(self) -> str:
        """
        Retourne une représentation lisible de l'objet Ingredient.

        Retour :
        --------
        str
            Représentation de l'ingrédient sous forme de chaîne de caractères.
        """
        return (
            f"Ingredient(idIngredient={self.idIngredient}, "
            f"strIngredient='{self.strIngredient}', "
            f"strDescription='{self.strDescription}', "
            f"strType='{self.strType}')"
        )
