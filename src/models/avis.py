from datetime import datetime


class Avis:
    """
    Classe représentant un avis d'utilisateur.

    Attributes:
        id_avis (int): L'identifiant unique de l'avis.
        titre_avis (str): Le titre de l'avis.
        id_utilisateur (int): L'identifiant de l'utilisateur qui a publié l'avis.
        nom_auteur (str): Le nom de l'auteur de l'avis.
        date_publication (datetime): La date de publication de l'avis.
        commentaire (str): Le commentaire de l'avis.
        note (int or None): La note donnée à l'avis (peut être None si non noté).
        id_recette (int): L'identifiant de la recette à laquelle l'avis est associé.
    """

    def __init__(
        self,
        id_avis: int,
        titre_avis: str,
        id_utilisateur: int,
        nom_auteur: str,
        id_recette: int,
        date_publication: datetime = datetime.now(),
        commentaire: str = "",
        note: int = None,
    ):
        """
        Initialise un nouvel avis.

        Parameters:
            id_avis (int): L'identifiant unique de l'avis.
            titre_avis (str): Le titre de l'avis.
            id_utilisateur (int): L'identifiant de l'utilisateur.
            nom_auteur (str): Le nom de l'auteur de l'avis.
            id_recette (int): L'identifiant de la recette à laquelle l'avis est associé.
            date_publication (datetime, optional): La date de publication. Par défaut,
                         c'est la date et l'heure actuelles.
            commentaire (str, optional): Le commentaire de l'avis. Par défaut,
                        c'est une chaîne vide.
            note (int or None, optional): La note donnée à l'avis. Par défaut, c'est None.
        """
        self.id_avis = id_avis
        self.titre_avis = titre_avis
        self.id_utilisateur = id_utilisateur
        self.nom_auteur = nom_auteur
        self.id_recette = id_recette  # Ajout de l'ID de la recette
        self.date_publication = date_publication
        self.commentaire = commentaire
        self.note = note

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de l'avis.

        Returns:
            str: Une chaîne contenant les détails de l'avis.
        """
        return (
            f"ID Avis: {self.id_avis}\n"  # Affichage de l'ID de l'avis
            f"Titre: {self.titre_avis}\n"  # Affichage du titre de l'avis
            f"Auteur: {self.nom_auteur}\n"  # Affichage du nom de l'auteur
            f"Commentaire: {self.commentaire}\n"  # Affichage du commentaire
            f"Note: {self.note or 'Non noté'}\n"  # Affichage de la note
            f"Date de publication: {self.date_publication.strftime('%d/%m/%Y')}\n"
            # Affichage de la date
            f"ID Utilisateur: {self.id_utilisateur}\n"  # Affichage de l'ID de l'utilisateur
            f"ID Recette: {self.id_recette}"  # Affichage de l'ID de la recette
        )
