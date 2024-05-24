# Django Niger

Bienvenue sur le projet Django Niger ! Ce projet vise à créer une communauté dynamique et passionnée autour du framework Django au Niger. Notre objectif est de connecter les développeurs, novices et experts, pour partager des connaissances, collaborer sur des projets, et promouvoir le développement web avec Django et Python.

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

4. Configurez les variables d'environnement :

    Créez un fichier `.env` à la racine du projet et ajoutez-y les configurations suivantes :

    ```env
    POSTGRES_DB=nom_de_la_base_de_données
    POSTGRES_USER=nom_utilisateur
    POSTGRES_PASSWORD=mot_de_passe
    POSTGRES_HOST=hôte
    POSTGRES_PORT=port

    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    EMAIL_HOST=smtp.your-email-provider.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_USE_SSL=False
    EMAIL_HOST_USER=your-email@example.com
    EMAIL_HOST_PASSWORD=your-email-password
    DEFAULT_FROM_EMAIL=your-email@example.com
    ```

5. Appliquez les migrations de la base de données :

    ```sh
    python manage.py migrate
    ```

6. Démarrez le serveur de développement :

    ```sh
    python manage.py runserver
    ```

### Configuration de l'Email

Assurez-vous de configurer les variables d'environnement pour l'email dans votre fichier `.env` comme mentionné ci-dessus. Voici un rappel des paramètres :

```python
EMAIL_BACKEND = config("EMAIL_BACKEND")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT", cast=int)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool)
EMAIL_USE_SSL = config("EMAIL_USE_SSL", cast=bool)
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
```

### Création de la Base de Données PostgreSQL

1. Connectez-vous à PostgreSQL en utilisant un utilisateur avec des privilèges d'administration :

    ```sh
    sudo -u postgres psql
    ```

2. Créez la base de données et l'utilisateur :

    ```sql
    CREATE DATABASE nom_de_la_base_de_données;
    CREATE USER nom_utilisateur WITH PASSWORD 'mot_de_passe';
    ```

3. Accordez tous les privilèges sur la base de données à l'utilisateur :

    ```sql
    GRANT ALL PRIVILEGES ON DATABASE nom_de_la_base_de_données TO nom_utilisateur;
    ```

4. Accordez les privilèges nécessaires sur le schéma `public` :

    ```sql
    \c nom_de_la_base_de_données
    GRANT USAGE ON SCHEMA public TO nom_utilisateur;
    GRANT CREATE ON SCHEMA public TO nom_utilisateur;
    GRANT ALL PRIVILEGES ON SCHEMA public TO nom_utilisateur;
    ```

## Contribuer

Nous accueillons avec plaisir les contributions de la communauté. Veuillez consulter notre [guide de contribution](CONTRIBUTING.md) pour plus de détails.

## License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Auteurs

- [ISSAKA HAMA Barhamou](https://github.com/HamaBarhamou) - Développeur Principal

---

Pour plus d'informations, visitez notre : [site web](https://django.pythonniger.org/) .

