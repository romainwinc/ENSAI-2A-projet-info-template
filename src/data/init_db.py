# Permet d'initialiser les tables de la bases de données
# Récupère toutes les recettes et ingrédients provenant de l'API
print("---- Création des tables et remplisages ----")
import data.create_db
import data.pop_db

print("---- Initialisation des utilisateurs ----")
import data.pop_utilisateur

print("---- Initialisation des préférences ----")
import data.pop_preference
