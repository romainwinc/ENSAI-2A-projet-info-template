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

This repository contains a `.vscode/settings.json` file that defines settings for this project. 

For example:

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

This repository contains various configuration files to set up the different tools used.

| File                          | Description                                                         |
|-------------------------------|---------------------------------------------------------------------|
| `.env`                         | Defines the environment variables                                   |
| `.vscode/settings.json`        | Visual Studio Code specific configuration                           |
| `.github/workflows/ci.yml`     | Definition of GitHub Actions workflows                              |
| `logging_config.yml`           | Configuration of the logging system                                 |
| `.gitignore`                   | List of files and directories to ignore during Git operations      |
| `.coveragerc`                  | Configuration of the code coverage tool                             |
| `requirements.txt`             | List of required Python dependencies for the project                |
---

## :arrow_forward: Install the necessary packages

In VSCode:

- [ ] Open a *Git Bash* terminal
- [ ] Run the following commands

```bash
pip install -r requirements.txt
pip list
```

---

## :arrow_forward: Variables d'environnement

You will now define environment variables to declare the database and the web service your Python application will connect to.

At the root of the project, the file:

- [ ] Create a file named `.env`
- [ ] Paste and complete the following items

```default
WEBSERVICE_HOST=https://pokeapi.co/api/v2

POSTGRES_HOST=sgbd-eleves.domensai.ecole
POSTGRES_PORT=5432
POSTGRES_DATABASE=idxxxx
POSTGRES_USER=idxxxx
POSTGRES_PASSWORD=idxxxx
POSTGRES_SCHEMA=projet_informatique
```

---

## :arrow_forward: Launch unit tests

All services are tested:

- [ ] In Git Bash : 
`python -m pytest` 

### Tests coverage

It is also possible to generate test coverage with [Coverage](https://coverage.readthedocs.io/en/7.4.0/index.html)

:bulb: The `.coveragerc` file allows you to modify the configuration

- [ ] `coverage run -m pytest`
- [ ] `coverage html`
- [ ] Open the file coverage_report/index.html

---

## :arrow_forward: Launch program

This application provides a very basic graphical interface to navigate between different menus in the terminal.

- [ ] In Git Bash: `python src/__main__.py`
- [ ] On the first run, execute in Git Bash: `python src/__init__db.py`
  - This program will run the scripts in the `data` folder
  - These scripts load all the data from the API
  - As well as add fake users, requests, reviews, and associated preferences

---
<!-- 
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
``` -->

---

### Connect your application to the database

You will connect your application to the database.

You will use a `.env` file for this, as described in the [Environment Variables](##:arrow_forward:-Environment-Variables) section above. In your VSCode:

- [ ] Create a `.env` file at the root of `ENSAI-2A-projet-info-template`
- [ ] Paste the template (see the *Environment Variables* section)
- [ ] Fill in the `HOSTNAME`, `DATABASE`, `USERNAME`, and `PASSWORD` fields with those of your *PostgreSQL* service
- [ ] Save this file

### Install the packages

- [ ] Open a terminal (CTRL + ù)
- [ ] Navigate to the repository: `cd $ROOT_PROJECT_DIRECTORY/ENSAI-2A-projet-info-template`
- [ ] `pip install -r requirements.txt`


### Launch the application

You can now launch the application or run the unit tests

- `python src/__main__.py` (if this is the first time you're launching the database, don't forget to start by re-initializing the DB by running `python src/__init__db.py`)
- `pytest -v`
