# Django Niger

Bienvenue sur le projet Django Niger ! Ce projet vise à créer une communauté dynamique et passionnée autour du framework Django au Niger. Notre objectif est de connecter les développeurs, novices et experts, pour partager des connaissances, collaborer sur des projets, et promouvoir le développement web avec Django.

## Fonctionnalités

- Forums de Discussion
- Workshops et Formations
- Projets Collaboratifs
- Événements à Venir
- Témoignages des Membres

## Installation

### Prérequis

- Python 3.11
- Django 5.x
- PostgreSQL (optionnel)
- pipenv ou virtualenv pour la gestion des environnements virtuels

### Étapes d'Installation

1. Clonez le dépôt :

    ```sh
    git clone https://github.com/Django-Niger/django_niger
    cd django-niger
    ```

2. Créez un environnement virtuel et activez-le :

    ```sh
    python -m venv .env
    source .env/bin/activate  # Sur Windows, utilisez `.env\Scripts\activate`
    ```

3. Installez les dépendances :

    ```sh
    pip install -r requirements.txt
    ```

4. Configurez les variables d'environnement (si vous utilisez PostgreSQL) :

    Créez un fichier `.env` à la racine du projet et ajoutez-y les configurations suivantes :

    ```env
    POSTGRES_DB=nom_de_la_base_de_données
    POSTGRES_USER=nom_utilisateur
    POSTGRES_PASSWORD=mot_de_passe
    POSTGRES_HOST=hôte
    POSTGRES_PORT=port
    ```

5. Appliquez les migrations de la base de données :

    ```sh
    python manage.py migrate
    ```

6. Démarrez le serveur de développement :

    ```sh
    python manage.py runserver
    ```

## Contribuer

Nous accueillons avec plaisir les contributions de la communauté. Veuillez consulter notre [guide de contribution](CONTRIBUTING.md) pour plus de détails.

## License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Auteurs

- [Votre Nom](https://github.com/nom-utilisateur) - Développeur Principal

---

Pour plus d'informations, visitez notre [site web](http://www.djangoniger.org).
