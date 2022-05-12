# Algorithmie

## Présentation

## Explication
Différentes étapes sont effectuées dans le fichier main.py :

### Préparation des données
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

* clean_dict_positions : On nettoie les données afin de les exploiter. On ôte le '\n' des dates et change le 
type chaîne de caractères en type datetime. On enlève le 'N' et le 'W' des latitudes et des longitudes. On rajoute le
nom des voiliers à chaque voilier.

### Calculs des indicateurs
* distance_position_finish : On calcule pour chaque position la distance en kilomètre avec le point d'arrivée
* speed_between_two_points : On calcule la vitesse de chaque voilier par rapport à son enregistrement précedent.
* ranking_sail_boat : On calcule le classement de chaque voilier à chaque eregistrement par rapport à la distance qui 
leur restent au point d'arrivée.

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

### Visualisation
* ranking : Permet d'afficher le classement, les vitesses et les distances restantes pour chaque enrigstrement.

## Execution
Prérequis : Avoir installé sur ça machine [Python](https://www.python.org/downloads/) et [Git](https://git-scm.com/)

Ouvrir un interpréteur de commandes et lancer les commandes suivantes : 

Récupérer le projet :
```
git clone https://github.com/BAAAARRE/Algorithmie.git
```
Accéder au dossier :
```
cd Algorithmie
```
Créer un environnement virtuel :
```
(Unix /Linux) : python3.8 -m venv venv
(windows) : python -m venv venv
```
Activer l'environnement : 
```
(Unix /Linux) : source venv/bin/activate
(windows) : venv\Scripts\activate
```
Lancer le script : 
```
python main.py
```