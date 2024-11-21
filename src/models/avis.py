from datetime import datetime


class Avis:
    """
    Représente un avis laissé par un utilisateur pour une recette.

    Attributs :
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
        Initialise un nouvel avis pour une recette.

        Paramètres :
            id_avis (int): L'identifiant unique de l'avis.
            titre_avis (str): Le titre de l'avis.
            id_utilisateur (int): L'identifiant de l'utilisateur ayant laissé l'avis.
            nom_auteur (str): Le nom de l'auteur de l'avis.
            id_recette (int): L'identifiant de la recette à laquelle l'avis est associé.
            date_publication (datetime, optionnel): La date de publication de l'avis.
                          Par défaut, c'est la date et l'heure actuelles.
            commentaire (str, optionnel): Le commentaire de l'avis. Par défaut, c'est une chaîne vide.
            note (int ou None, optionnel): La note donnée à l'avis. Par défaut, c'est None (non noté).
        """
        self.id_avis = id_avis
        self.titre_avis = titre_avis
        self.id_utilisateur = id_utilisateur
        self.nom_auteur = nom_auteur
        self.id_recette = id_recette
        self.date_publication = date_publication
        self.commentaire = commentaire
        self.note = note

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de l'avis.

        Retourne :
            str: Une chaîne de caractères contenant les détails de l'avis, incluant l'ID,
                 le titre, l'auteur, le commentaire, la note, la date de publication et
                 l'ID de la recette associée.
        """
        return (
            f"ID Avis: {self.id_avis}\n"
            f"Titre: {self.titre_avis}\n"
            f"Auteur: {self.nom_auteur}\n"
            f"Commentaire: {self.commentaire}\n"
            f"Note: {self.note or 'Non noté'}\n"
            f"Date de publication: {self.date_publication.strftime('%d/%m/%Y')}\n"
            f"ID Utilisateur: {self.id_utilisateur}\n"
            f"ID Recette: {self.id_recette}"
        )
