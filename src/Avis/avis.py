from datetime import datetime

class Avis:
    def __init__(self, titre: str, commentaire: str, nom_auteur: str, 
                 prenom_auteur: str, date_publication: datetime, 
                 note: int = None):
        self.titre = titre
        self.commentaire = commentaire
        self.nom_auteur = nom_auteur
        self.prenom_auteur = prenom_auteur
        self.note = note if note is None or 1 <= note <= 5 else None
        self.date_publication = date_publication or datetime.now()

    def __str__(self):
        return (f"Auteur: {self.prenom_auteur} {self.nom_auteur}\n"
                f"Titre: {self.titre}\n"
                f"Commentaire: {self.commentaire}\n"
                f"Note: {self.note or 'Non noté'}\n"
                f"Date de publication: {self.date_publication.strftime('%d/%m/%Y')}")