from non_connecte import Non_connecte


class Connecte(Non_connecte):
    """Un carburant est caractérisé par son nom et sa composition chimique.

    Parameters
    ----------
    nom : str
        nom du carburant
    composition_chimique : dict[SubstanceChimique, float]
        composition chimique du carburant
    """

    def __init__(self, nom: str, password: str) -> None:
        self.nom = nom
        self.password = password
        self.grade = 1
