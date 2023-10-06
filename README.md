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

![image](https://github.com/GeniaKybalchych/TPA015PurePython/assets/117115542/739865a2-4688-4d06-8314-64d55a540833)

## Service DAO
Ce service gère la base de données (MySQL) des utilisateurs et offre deux routes pour ajouter et récupérer des utilisateurs.

![image](https://github.com/GeniaKybalchych/TPA015PurePython/assets/117115542/05b06f99-b3e1-444a-8039-6d027ce5ec24)


## Service Analytique
Fournit des statistiques basées sur les données stockées dans la base de données.

![image](https://github.com/GeniaKybalchych/TPA015PurePython/assets/117115542/94ca9ca1-79e4-4eca-8313-10426fe1ca57)


## Client Web
Affiche les informations des utilisateurs et des statistiques à partir du service analytique.
![image](https://github.com/GeniaKybalchych/TPA015PurePython/assets/117115542/378c6eb3-f25f-4e9c-9004-83ded758f0ce)


# Déploiement du service principal
Pré-requis: Assurez-vous d'avoir installé Docker, .NET Core SDK et Python.

## Étapes: 

(1) Construction de l'image: docker build -t micro :latest .

(2) Exécution du service dans un container Docker: docker run -p 5500:5000 micro

![image](https://github.com/GeniaKybalchych/TPA015PurePython/assets/117115542/213b0119-ee3e-4ebe-8ef5-7624c15c1ae1)

(3) Validation avec Postman: 

![image](https://github.com/GeniaKybalchych/TPA015PurePython/assets/117115542/83e5693f-db55-4c95-8e1d-27105f1fe08a)

![image](https://github.com/GeniaKybalchych/TPA015PurePython/assets/117115542/24e8906b-ffff-49b0-9b0c-41f31340e178)



