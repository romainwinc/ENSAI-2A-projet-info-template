from create_db import create_tables
from pop_db import insert_ingredients


def main():
    print("Création des tables...")
    create_tables()

    print("Insertion des ingrédients...")
    insert_ingredients()


if __name__ == "__main__":
    main()
