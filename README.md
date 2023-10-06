#  Projet: Suggestion d’une Activité Basé sur la Température

- Développement et intégration de trois services REST avec une base de données SQL 
- Conception et mise en place de protocoles d’authentification, ainsi que l'élaboration d'une documentation pertinente 
- Développement de deux clients consommant les APIs, et création d'interfaces
- Déploiement du service principal via Docker

**Environnement** : Python, C#, REST, SQL, Docker, Flasgger

## Client C#
Un client console simple en C# qui récupère la température et la date de naissance de l'utilisateur, et demande une suggestion d'activité basée sur la température.

![image](https://github.com/GeniaKybalchych/TPA015PurePython/assets/117115542/6af8a6bd-f99c-4b79-b71e-bef3adb7e33a)


## Service Principal
Le service principal est basé sur Flask et utilise JWT pour l'authentification. Il fournit une suggestion d'activité basée sur la température et enregistre les informations de l'utilisateur dans une base de données à l'aide du service DAO.

## Service DAO
Ce service gère la base de données des utilisateurs et offre deux routes pour ajouter et récupérer des utilisateurs.

## Service Analytique
Fournit des statistiques basées sur les données stockées dans la base de données.

## Client Web
Affiche les informations des utilisateurs et des statistiques à partir du service analytique.

# Déploiement
Pré-requis: Assurez-vous d'avoir installé Docker, .NET Core SDK et Python.
