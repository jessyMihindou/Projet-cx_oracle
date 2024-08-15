# Database Manager Application

![App Header](https://mma.prnewswire.com/media/467598/Oracle_Logo.jpg?p=facebook) 

## Description

Cette application Django permet de manipuler une base de données Oracle de manière interactive. Elle offre des fonctionnalités pour gérer les utilisateurs, exécuter des requêtes SQL, et gérer les tables directement depuis l'interface web.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

- Python 3.6 ou supérieur
- Django 3.x
- Oracle Database
- `cx_Oracle` pour la connexion à Oracle Database

## Installation

1. **Clonez le dépôt :**

    ```bash
    git clone https://github.com/yourusername/database-manager.git
    cd database-manager
    ```

2. **Créez un environnement virtuel et activez-le :**

    ```bash
    python -m venv venv
    source venv/bin/activate   # Sur Windows utilisez `venv\Scripts\activate`
    ```

3. **Installez les dépendances :**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurez la connexion à la base de données Oracle :**

    Modifiez le fichier `database_manager/settings.py` et configurez la connexion Oracle :

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME': 'your_oracle_database',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'your_oracle_host',
            'PORT': 'your_oracle_port',
        }
    }
    ```

5. **Exécutez les migrations :**

    ```bash
    python manage.py migrate
    ```

6. **Lancez le serveur de développement :**

    ```bash
    python manage.py runserver
    ```

7. **Accédez à l'application :**

    Ouvrez votre navigateur et allez à [http://localhost:8000](http://localhost:8000) pour accéder à l'application.

## Fonctionnalités

- **Gestion des Utilisateurs :** Ajouter, supprimer et modifier les utilisateurs de la base de données Oracle.
- **Exécution des Requêtes SQL :** Exécutez des requêtes SQL directement depuis l'interface.
- **Gestion des Tables :** Créez, modifiez et supprimez des tables dans la base de données Oracle.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez contribuer, veuillez suivre ces étapes :

1. Fork le projet.
2. Créez une nouvelle branche (`git checkout -b feature/YourFeature`).
3. Committez vos modifications (`git commit -am 'Add new feature'`).
4. Poussez la branche (`git push origin feature/YourFeature`).
5. Ouvrez une Pull Request.

## Licence

Ce projet est sous la licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Auteurs

- **MIHINDOU MAMBOUNDOU Gervais Jessy** - *Créateur* - [Profil GitHub](https://github.com/jessyMihindou/)

---

Pour toute question ou problème, veuillez ouvrir une issue sur [GitHub](https://github.com/jessyMihindou/Projet-cx_oracle/new/master?filename=README.md)
