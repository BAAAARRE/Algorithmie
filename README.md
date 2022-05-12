# Algorithmie

## Présentation

## Explication

Dictionnaire avec les données finales :



```
{
'<nom_du_fichier_1>': {
    '<id_voilier_1>': {
            'latitude': 12.5991, 
            'longitude': 53.5584, 
            'date': datetime.datetime(2021, 12, 1, 12, 0, 23), 
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

Récupérer le projet :
```
git clone https://github.com/BAAAARRE/Algorithmie.git
```
Créer un environnement virtuel :
```
python -m venv venv
```
Activer l'environnement : 
```
./venv/Scripts/activate.bat
```
Lancer le script : 
```
python main.py
```