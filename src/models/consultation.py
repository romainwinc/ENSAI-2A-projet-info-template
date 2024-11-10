from datetime import date


class Consultation:
    def __init__(self, id_recette: int, id_utilisateur: int, date_consultation: date):
        self.id_recette = id_recette
        self.id_utilisateur = id_utilisateur
        self.date_consultation = date_consultation

    def __str__(self):
        return (
            f"Consultation(id_recette={self.id_recette}, "
            f"id_utilisateur={self.id_utilisateur}, "
            f"date_consultation={self.date_consultation})"
        )

    def afficher_consultation(self):
        print(
            f"Recette ID: {self.id_recette}, "
            f"Utilisateur ID: {self.id_utilisateur}, "
            f"Date de consultation: {self.date_consultation}"
        )
