# Algorithmie

## Présentation

## Explication
Différentes étapes sont effectuées dans le fichier main.py :
* open_sailboats : On ouvre le fichier voiliers.tsv. On le met dans un dictionnaire avec l'identifiant du voilier en clé
et son nom en valeur. Pour le nom on enlève le '\n'.
* get_all_files : Cette fonction permet de lister tous les noms de fichiers des positions du dossier data.
* open_positions : On ouvre tous les fichiers de positions. On les met dans un dictionnaire avec le nom du fichier en clé
et une liste avec chaque ligne en valeur
* raw_positions_to_dict : On reprend le dictionnaire précédent, renomme les clés avec juste la date du fichier. Pour 
chaque ligne de chaque fichier on créé un dictionnaire avec l'identifiant du voilier en clé et autre dictionnaire en 
valeur. Dans cet autre dictionnaire on ajoute latitude, longitude et date en clé avec leurs valeurs.

Dictionnaire à l'état de cette étape :
```
{
'<nom_du_fichier_1>': {
    '<id_voilier_1>': {
            'latitude': '12.5991N', 
            'longitude': '53.5584W', 
            'date': '12/01/21 12:00:23'
        },
    ...
    },
'<nom_du_fichier_2>': {
    '<id_voilier_1>': {
            'latitude': '12.5991N', 
            'longitude': '53.5584W', 
            'date': '12/01/21 12:00:23'
        },
    ...
    },
    ...
}
```

Dictionnaire avec les données finales :
```
{
'<nom_du_fichier_1>': {
    '<id_voilier_1>': {
            'latitude': 12.5991, 
            'longitude': 53.5584, 
            'date': datetime.datetime(2021, 12, 1, 12, 0, 23), 
            'name': 'Akoya', 
            'distance': 892.020063, 
            'distance_with_previous_point': 32.9523, 
            'time_with_previous_point': 4.0, 
            'speed': 8.24, 
            'ranking': 12
        },
    ...
    },
'<nom_du_fichier_2>': {
    '<id_voilier_1>': {
            'latitude': 12.5991, 
            'longitude': 53.5584, 
            'date': datetime.datetime(2021, 12, 1, 12, 0, 23), 
            'name': 'Akoya', 
            'distance': 892.020063, 
            'distance_with_previous_point': 32.9523, 
            'time_with_previous_point': 4.0, 
            'speed': 8.24, 
            'ranking': 12
        },
    ...
    },
    ...
}
```

## Execution
Prérequis : Avoir installé sur ça machine [Python](https://www.python.org/downloads/) et [Git](https://git-scm.com/)

Ouvrir un interpréteur de commandes et lancer les commandes suivantes : 

Récupérer le projet :
```
git clone https://github.com/BAAAARRE/Algorithmie.git
```
Créer un environnement virtuel :
```
(Unix /Linux) : python3.8 -m venv venv
(windows) : python -m venv venv
```
Activer l'environnement : 
```
(Unix /Linux) : source venv/bin/activate
(windows) : ./venv/Scripts/activate.bat
```
Lancer le script : 
```
python main.py
```