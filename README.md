# ENSAI-2A-projet-info

# modifier les .env
# excécuter le init_dp.py
2nd year computer science project at ENSAI.

The Recipe Maker application includes :

- Layer programming (CAD, service, view, models)
- Connection to a database
- Terminal interface (view layer) with inquirerPy
- Calling a Webservice

## :arrow_forward: Software requirements

- [Visual Studio Code](https://code.visualstudio.com/)
- [Python 3.10](https://www.python.org/)
- Une base de données [PostgreSQL](https://www.postgresql.org/)

---

## :arrow_forward: Opening the file and VScode

- [ ] Download the zipped folder from moodle
- [ ] After unzipping it, open **Visual Studio Code**
- [ ] File > Open Folder
- [ ] Click once on the unzipped folder *ENSAI-2A-projet-info-template* and click on `Sélectionner un dossier`

### VScode parameters

# Project Settings

This repository contains a `.vscode/settings.json` file that defines settings for this project. For example:

## Black Formatter

- Automatically formats a Python file
- **Setting**: `editor.formatOnSave`  
  On every file save, the code is automatically formatted

## Flake

- A linter that ensures the code is clean
- Displays a message if the code does not meet the standards

## Path

- Specifies the folders where the Python modules are located
- **Setting**: `"PYTHONPATH": "${workspaceFolder}/src"`  
  `src` is the root folder for imports


### Configuration files

Ce dépôt contient de nombreux fichiers de configuration pour paramètrer les différents outils utilisés.

| Fichier                      | Description                                                         |
|------------------------------|---------------------------------------------------------------------|
| `.env`                       | Définir les variables d'environnement                               |
| `.vscode/settings.json`      | Configuration spécifique à Visual Studio Code                       |
| `.github/workflows/ci.yml`   | Définition des workflows GitHub Actions                             |
| `logging_config.yml`         | Configuration du système de journalisation (logging)                |
| `.gitignore`                 | Liste des fichiers et répertoires à ignorer lors des opérations Git |
| `.coveragerc`                | Configuration de l'outil de couverture de code (coverage)           |
| `requirements.txt`           | Liste des dépendances Python requises pour le projet                |

---

## :arrow_forward: Installez les packages nécessaires

Dans VSCode :

- [ ] Ouvrez un terminal *Git Bash*
- [ ] Exécutez les commandes suivantes

```bash
pip install -r requirements.txt
pip list
```

---

## :arrow_forward: Variables d'environnement

Vous allez maintenant définir des variables d'environnement pour déclarer la base de données et le webservice auquels vous allez connecter votre application python.

À la racine du projet le fichier :

- [ ] Créez un fichier nommé `.env` 
- [ ] Collez-y et complétez les éléments ci-dessous

```default
WEBSERVICE_HOST=https://pokeapi.co/api/v2

POSTGRES_HOST=sgbd-eleves.domensai.ecole
POSTGRES_PORT=5432
POSTGRES_DATABASE=idxxxx
POSTGRES_USER=idxxxx
POSTGRES_PASSWORD=idxxxx
POSTGRES_SCHEMA=projet
```

---

## :arrow_forward: Lancer les tests unitaires

- [ ] Dans Git Bash : `pytest -v` 
  - ou `python -m pytest -v` si *pytest* n'a pas été ajouté au *PATH*

### TU DAO

Les tests unitaires de la DAO utilisent les données du fichier `data/pop_db_test.sql`.

Ces données sont chargées dans un schéma à part (projet_test_dao) pour ne pas polluer les autres données.

### Couverture de tests

Il est également possible de générer la couverture de tests avec [Coverage](https://coverage.readthedocs.io/en/7.4.0/index.html)

:bulb: Le fichier `.coveragerc` permet de modifier le paramétrage

- [ ] `coverage run -m pytest`
- [ ] `coverage html`
- [ ] Ouvrir le fichier coverage_report/index.html

---

## :arrow_forward: Lancer le programme

Cette application propose une interface graphique très basique pour naviguer entre différents menus.

- [ ] Dans Git Bash : `python src/__main__.py`
- [ ] Au premier lancement, choisissez **Ré-initialiser la base de données**
  - cela appelle le programme `src/utils/reset_database.py`
  - qui lui même va exécuter les scripts SQL du dossier `data`

---

## :arrow_forward: Lancer le webservice

Cette application permet également de créer un webservice.

- [ ] `python src/app.py`
- Exemples de endpoints (à tester par exemple avec *Insomnia* ou éventuellement un navigateur):
  - `GET http://localhost/docs` (swagger)
  - `GET http://localhost/hello/you`
  - `GET http://localhost/joueur`
  - `GET http://localhost/joueur/3`
  - ```
    POST http://localhost/joueur/
    JSON body :
      {
        "pseudo": "patapouf",
        "mdp": "9999",
        "age": "95",
        "mail": "patapouf@mail.fr",
        "fan_pokemon": true
      }
    ```
  - ```
    PUT http://localhost/joueur/3
    JSON body :
      {
         "pseudo": "maurice_new",
         "mdp": null,
         "age": 20,
         "mail": "maurice@ensai.fr",
         "fan_pokemon": true
      }
    ```
  - `DELETE http://localhost/joueur/5`

---

## :arrow_forward: Les logs

L'initalisation se fait dans le module `src/utils/log_init.py` :

- Celui-ci est appelé au démarrage de l'application ou du webservice
- Il utilise le fichier `logging_config.yml` pour la configuration
  - pour modifier le niveau de logs :arrow_right: balise *level*

Un décorateur a été créé dans `src/utils/log_decorator.py`.

Appliqué à une méthode, il permettra d'afficher dans les logs :

- les paramétres d'entrée
- la sortie

Les logs sont consultables dans le dossier `logs`.

Exemple de logs :

```
07/08/2024 09:07:07 - INFO     - ConnexionVue
07/08/2024 09:07:08 - INFO     -     JoueurService.se_connecter('a', '*****') - DEBUT
07/08/2024 09:07:08 - INFO     -         JoueurDao.se_connecter('a', '*****') - DEBUT
07/08/2024 09:07:08 - INFO     -         JoueurDao.se_connecter('a', '*****') - FIN
07/08/2024 09:07:08 - INFO     -            └─> Sortie : Joueur(a, 20 ans)
07/08/2024 09:07:08 - INFO     -     JoueurService.se_connecter('a', '*****') - FIN
07/08/2024 09:07:08 - INFO     -        └─> Sortie : Joueur(a, 20 ans)
07/08/2024 09:07:08 - INFO     - MenuJoueurVue
```

---

## :arrow_forward: Intégration continue

Le dépôt contient un fichier `.github/workflow/main.yml`.

Lorsque vous faîtes un *push* sur GitHub, cela déclanche un pipeline qui va effectuer les les étapes suivantes :

- Création d'un conteneur à partir d'une image Ubuntu (Linux)
  - Autrement dit, cela crée une machine virtuelle avec simplement un noyau Linux
- Installation de Python
- Installation des packages requis
- Lancement des tests unitaires (uniquement les tests de service car plus compliqué de lancer les tests dao)
- Analyse du code avec *pylint*
  - Si la note est inférieure à 7.5, l'étape sera en échec

Vous pouvez consulter le bon déroulement de ce pipeline sur la page GitHub de votre dépôt, onglet *Actions*.

---

## :construction: Lancer le projet sur le Datalab

Il est également possible de développer sur le Datalab.

:warning: Pensez bien à *push* régulièrement votre code, car les services du Datalab ne sont pas éternels.


### Paramétrage Git

Dans un premier temps, il faut autoriser de *push* du code depuis le Datalab vers GitHub.

Générez un jeton dans GitHub :

- [ ] Connectez-vous à [GitHub](https://github.com/)
- [ ] [Générez un nouveau token (classic)](https://github.com/settings/tokens/new)
  - si le lien direct ne fonctionne pas : allez dans *Settings* > *Developer Settings* > *Personal access tokens (classic)*
  - Note : Datalab
  - Date d'expiration : 90j (minimum)
  - Cochez repo
  - `Generate token`
- [ ] Copiez le token et collez le dans Notepad
  - :warning: Celui-ci ne sera visible qu'une seule fois
  - si vous le perdez, il faut en générer un nouveau

Ensuite, déclarez ce jeton au Datalab :

- [ ] Connectez-vous au [Datalab](https://datalab.sspcloud.fr/)
- [ ] Allez dans *Mon Compte*, puis *Services externes*
- [ ] Collez le token dans *Jeton d'accès personnel GitHub*

### Lancer les services

Pour commencer, vous avez besoin d'une base de données PostgreSQL. Sur la Datalab

- [ ] Allez dans *Catalogue de services* > *Database* > `PostgreSQL`
- [ ] Lancez le service
- [ ] Une fois le service lancé, copiez les infos suivantes
  ```
  Hostname : ?
  Port : 5432
  Database : ?
  Username : ?
  Password : ?
  ```
Nous allons ensuite lancer un service VSCode avec Python :

- [ ] Dans le catalogue des services, allez sur *Vscode-python*
- [ ] Cliquez sur *Configuration Vscode-python*
- [ ] Allez dans l'onglet Git
  - Repository : `https://github.com/ludo2ne/ENSAI-2A-projet-info-template.git`
- [ ] Lancez le service

Un nouvel onglet s'ouvre avec VSCode et le dépôt qui a été cloné.

Positionnez-vous dans le bon dossier :

- [ ] File > Open Folder > `/home/onyxia/work/ENSAI-2A-projet-info-template/`


### Connectez votre application et votre base de données

Vous avez lancé 2 services, maintenant il va falloir les relier.

Vous allez utiliser pour cela un fichier `.env` comme décrit dans la section [Variables d'environnement](##:arrow_forward:-Variables-d'environnement) plus haut. Dans votre VScode :

- [ ] Créez à la racine de `ENSAI-2A-projet-info-template` un fichier `.env`
- [ ] Collez le modèle (voir section *Variables d'environnement*)
- [ ] Renseignez les champs `HOSTNAME`, `DATABASE`, `USERNAME` et `PASSWORD` avec ceux de votre service *PostgreSQL*
- [ ] Enregistrez ce fichier

### Installez les packages

- [ ] Ouvrez un terminal (CTRL + ù)
- [ ] Positionnez-vous dans le dépôt : `cd $ROOT_PROJECT_DIRECTORY/ENSAI-2A-projet-info-template`
- [ ] `pip install -r requirements.txt`


### Lancez l'application

Vous pouvez maintenant lancer l'application, le webservice ou les tests unitaires

- `python src/__main__.py` (puis commencez par ré-initialiser la bdd)
- `python src/app.py` (à tester)
- `pytest -v`