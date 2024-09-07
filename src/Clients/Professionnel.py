from connecte import Connecte


class Professionnel(Connecte):
    """Un carburant est caractérisé par son nom et sa composition chimique.

    Parameters
    ----------
    nom : str
        nom du carburant
    composition_chimique : dict[SubstanceChimique, float]
        composition chimique du carburant
    """

    def __init__(self) -> None:
        self.grade = 2