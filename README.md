# Description du Système

## Client C#
Un client console simple en C# qui récupère la température et la date de naissance de l'utilisateur, et demande une suggestion d'activité basée sur la température.

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
