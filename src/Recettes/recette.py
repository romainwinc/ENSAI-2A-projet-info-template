class Recette:
    """Un carburant est caractérisé par son nom et sa composition chimique.

    Parameters
    ----------
    nom : str
        nom du carburant
    composition_chimique : dict[SubstanceChimique, float]
        composition chimique du carburant
    """
    def __init__(self, idMeal: str, strMeal: str, strCategory: str, 
                 strArea: str, strInstructions: str, strTags: str | None,
                 strIngredient1: str | None, 
                 strIngredient2: str | None, 
                 strIngredient3: str | None, 
                 strIngredient4: str | None, 
                 strIngredient5: str | None, 
                 strIngredient6: str | None, 
                 strIngredient7: str | None, 
                 strIngredient8: str | None, 
                 strIngredient9: str | None, 
                 strIngredient10: str | None, 
                 strIngredient11: str | None, 
                 strIngredient12: str | None, 
                 strIngredient13: str | None, 
                 strIngredient14: str | None, 
                 strIngredient15: str | None, 
                 strIngredient16: str | None, 
                 strIngredient17: str | None, 
                 strIngredient18: str | None, 
                 strIngredient19: str | None, 
                 strIngredient20: str | None, 
                 strMeasure1: str | None, 
                 strMeasure2: str | None, 
                 strMeasure3: str | None, 
                 strMeasure4: str | None, 
                 strMeasure5: str | None, 
                 strMeasure6: str | None, 
                 strMeasure7: str | None, 
                 strMeasure8: str | None, 
                 strMeasure9: str | None, 
                 strMeasure10: str | None, 
                 strMeasure11: str | None, 
                 strMeasure12: str | None, 
                 strMeasure13: str | None, 
                 strMeasure14: str | None, 
                 strMeasure15: str | None, 
                 strMeasure16: str | None, 
                 strMeasure17: str | None, 
                 strMeasure18: str | None, 
                 strMeasure19: str | None,
                 strMeasure20: str | None) -> None:
        
        self.idMeal = idMeal
        self.strMeal = strMeal
        self.strCategory = strCategory
        self.strArea = strArea
        self.strInstructions = strInstructions
        self.strTags = strTags
        self.strIngredient1 = strIngredient1
        self.strIngredient2 = strIngredient2
        self.strIngredient3 = strIngredient3
        self.strIngredient4 = strIngredient4
        self.strIngredient5 = strIngredient5
        self.strIngredient6 = strIngredient6
        self.strIngredient7 = strIngredient7
        self.strIngredient8 = strIngredient8
        self.strIngredient9 = strIngredient9
        self.strIngredient10 = strIngredient10
        self.strIngredient11 = strIngredient11
        self.strIngredient12 = strIngredient12
        self.strIngredient13 = strIngredient13
        self.strIngredient14 = strIngredient14
        self.strIngredient15 = strIngredient15
        self.strIngredient16 = strIngredient16
        self.strIngredient17 = strIngredient17
        self.strIngredient18 = strIngredient18
        self.strIngredient19 = strIngredient19
        self.strIngredient20 = strIngredient20
        self.strMeasure1 = strMeasure1
        self.strMeasure2 = strMeasure2
        self.strMeasure3 = strMeasure3
        self.strMeasure4 = strMeasure4
        self.strMeasure5 = strMeasure5
        self.strMeasure6 = strMeasure6
        self.strMeasure7 = strMeasure7
        self.strMeasure8 = strMeasure8
        self.strMeasure9 = strMeasure9
        self.strMeasure10 = strMeasure10
        self.strMeasure11 = strMeasure11
        self.strMeasure12 = strMeasure12
        self.strMeasure13 = strMeasure13
        self.strMeasure14 = strMeasure14
        self.strMeasure15 = strMeasure15
        self.strMeasure16 = strMeasure16
        self.strMeasure17 = strMeasure17
        self.strMeasure18 = strMeasure18
        self.strMeasure19 = strMeasure19
        self.strMeasure20 = strMeasure20

    def __repr__(self) -> str:
        ingredients = []
        measures = []

        for i in range(1, 21):
            ingredient = getattr(self, f'strIngredient{i}')
            measure = getattr(self, f'strMeasure{i}')
            if ingredient and measure:
                ingredients.append(f'{measure} {ingredient}')
            elif ingredient:
                ingredients.append(ingredient)
        
        ingredients_str = '\n'.join(ingredients)

        return (f'Recette: {self.strMeal}\n'
                f'Catégorie: {self.strCategory}\n'
                f'Région: {self.strArea}\n'
                f'Instructions: {self.strInstructions}\n'
                f'Ingrédients:\n{ingredients_str}\n'
                f'Tags: {self.strTags if self.strTags else "Aucun"}')


