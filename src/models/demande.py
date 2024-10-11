class Demande:
    def __init__(
        self,
        id_demande: int,
        id_utilisateur: int,
        type_demande: str,
        attribut_modifie: str,
        attribut_corrige: str,
        commentaire_demande: str,
    ):
        self.id_demande = id_demande
        self.id_utilisateur = id_utilisateur
        self.type_demande = type_demande
        self.attribut_modifie = attribut_modifie
        self.attribut_corrige = attribut_corrige
        self.commentaire_demande = commentaire_demande

    def __str__(self):
        return (
            f"Demande(id_demande={self.id_demande}, id_utilisateur={self.id_utilisateur}, "
            f"type_demande='{self.type_demande}', attribut_modifie='{self.attribut_modifie}', "
            f"attribut_corrige='{self.attribut_corrige}', commentaire_demande='{self.commentaire_demande}')"
        )

    def afficher_demande(self):
        print(f"Demande ID: {self.id_demande}")
        print(f"Utilisateur ID: {self.id_utilisateur}")
        print(f"Type de demande: {self.type_demande}")
        print(f"Attribut modifié: {self.attribut_modifie}")
        print(f"Attribut corrigé: {self.attribut_corrige}")
        print(f"Commentaire de la demande: {self.commentaire_demande}")
