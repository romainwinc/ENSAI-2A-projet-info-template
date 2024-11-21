class Demande:
    """
    Représente une demande d'un utilisateur concernant une modification d'attributs.

    Attributs :
        id_demande (int): Identifiant unique de la demande.
        id_utilisateur (int): Identifiant de l'utilisateur ayant fait la demande.
        type_demande (str): Type de la demande (par exemple, 'correction', 'ajout').
        attribut_modifie (str): Nom de l'attribut à modifier.
        attribut_corrige (str): Valeur corrigée ou modifiée de l'attribut.
        commentaire_demande (str): Commentaire ou explication concernant la demande.

    Méthodes :
        __str__(): Retourne une chaîne de caractères représentant l'objet Demande.
        afficher_demande(): Affiche les détails de la demande.
    """

    def __init__(
        self,
        id_demande: int,
        id_utilisateur: int,
        type_demande: str,
        attribut_modifie: str,
        attribut_corrige: str,
        commentaire_demande: str,
    ):
        """
        Initialise une instance de la classe Demande.

        Paramètres :
            id_demande (int): Identifiant unique de la demande.
            id_utilisateur (int): Identifiant de l'utilisateur ayant fait la demande.
            type_demande (str): Type de la demande.
            attribut_modifie (str): Attribut à modifier.
            attribut_corrige (str): Nouvelle valeur de l'attribut.
            commentaire_demande (str): Commentaire expliquant la demande.
        """
        self.id_demande = id_demande
        self.id_utilisateur = id_utilisateur
        self.type_demande = type_demande
        self.attribut_modifie = attribut_modifie
        self.attribut_corrige = attribut_corrige
        self.commentaire_demande = commentaire_demande

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères de l'objet Demande.

        Returns:
            str: La chaîne de caractères représentant la demande.
        """
        return (
            f"Demande(id_demande={self.id_demande}, "
            f"id_utilisateur={self.id_utilisateur}, "
            f"type_demande='{self.type_demande}', "
            f"attribut_modifie='{self.attribut_modifie}', "
            f"attribut_corrige='{self.attribut_corrige}', "
            f"commentaire_demande='{self.commentaire_demande}')"
        )

    def afficher_demande(self):
        """
        Affiche les détails de la demande dans la console.

        Affiche les attributs de la demande : ID de la demande, ID de l'utilisateur,
        type de la demande, attribut modifié, attribut corrigé et commentaire associé.
        """
        print(f"Demande ID: {self.id_demande}")
        print(f"Utilisateur ID: {self.id_utilisateur}")
        print(f"Type de demande: {self.type_demande}")
        print(f"Attribut modifié: {self.attribut_modifie}")
        print(f"Attribut corrigé: {self.attribut_corrige}")
        print(f"Commentaire de la demande: {self.commentaire_demande}")
