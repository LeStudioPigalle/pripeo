# Pripeo

[![Version](https://img.shields.io/badge/version-1.1.6-blue.svg)](https://img.shields.io/badge/version-1.1.6-blue.svg)

Pripeo est une plateforme qui permet de commander une carte virtuel ou physique. 

## Librairies Utilisées

- [Django](https://docs.djangoproject.com/en/4.2): Un framework web Python puissant pour assurer le site web.
- [gunicorn](https://docs.gunicorn.org/en/stable/index.html): Librairie pour le déploiement d'applications web Python en production (serveur HTTP WSGI).
- [request](https://pypi.org/project/requests/): Librairie pour les requêtes HTTTP

## Service externe 

- [Wallester](https://wallester.com/): Prestation de service de moyen de paiement

## Installation

1. Clonez le dépôt :

```sh
git clone https://github.com/<votreutilisateur>/saiyo.git
cd votreprrojet
```

2. Créez un environnement virtuel et installez les dépendances : 

```sh
python -m venv venv
source venv/bin/activate  # Sous Windows, utilisez `venv\Scripts\activate`
pip install -r requirements.txt
```

3. Appliquez les migrations :

```sh
python3 manage.py makemigrations
python3 manage.py migrate
```

4. Lancez le serveur de développement :

```sh
python manage.py runserver
```

## Mise en production

1. Configurez le fichier conf :

```sh
command='/<path>/<projet_name>/venv/bin/gunicorn'
pythonpath= '/<path>/<projet_name>'
bin = "<domain>:<port>"
worker = 3
```

2. Lancez la production

```sh
gunicorn -c gunicorn_config.py <nom_de_votre_projet>.wsgi:application
```
