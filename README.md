# Projet : Système de Gestion de Coworking - SQL et Python

## Auteur
**TISNES Francesca** - Mars 2026

---

## Présentation du Projet
Ce projet consiste en la mise en place d'un système de gestion de données pour un espace de travail partagé (coworking). L'objectif principal est de démontrer la transition d'un stockage de données plat, type tableur, vers une architecture de base de données relationnelle normalisée utilisant SQLite et Python.

### Objectifs métier
L'utilisation de fichiers Excel pour la gestion de réservations multiples présente des risques élevés d'incohérence et de redondance. Ce projet résout ces problématiques en isolant les entités (Entreprises, Membres, Réservations) pour garantir l'intégrité des informations.

---

## Architecture des Données (Normalisation)
Le système repose sur un schéma relationnel structuré en trois tables distinctes, évitant ainsi la répétition inutile de données.

| Table | Fonction | Clé Primaire | Clé Étrangère |
| :--- | :--- | :--- | :--- |
| **entreprises** | Référentiel des entités clientes | `id` | - |
| **membres** | Registre des utilisateurs (salariés) | `id` | `entreprise_id` |
| **reservations** | Historique des flux et transactions | `id` | `membre_id` |

---

## Caractéristiques Techniques
Le projet met en œuvre les technologies et méthodologies suivantes :
* **Génération de données :** Utilisation de la bibliothèque `Faker` pour la création d'un jeu de données de test (100 réservations, 40 membres, 10 entreprises).
* **Moteur de base de données :** Implémentation via SQLite pour une gestion locale et légère.
* **Traitement de données :** Utilisation de requêtes SQL complexes incluant des jointures (`JOIN`) et des fonctions d'agrégation (`SUM`, `COUNT`).
* **Analyse et Reporting :** Intégration de la bibliothèque `Pandas` pour le traitement des résultats et la génération de rapports financiers.
* **Interopérabilité :** Exportation automatique des analyses au format CSV pour exploitation dans des logiciels tiers.

---

## Installation et Exécution
1.  Ouvrir le dossier `projet_TISNES` dans l'environnement Visual Studio Code.
2.  Activer l'environnement virtuel Python (`.venv`).
3.  Exécuter l'intégralité du Notebook `gestion_coworking.ipynb` pour générer la base de données.
4.  Le fichier de sortie `rapport_activite_TISNES.csv` sera automatiquement créé à la racine du dossier.

---

## Maintenance et Évolutivité
Le code source inclut des procédures de maintenance démontrant la flexibilité du système :
* **Modification structurelle :** Ajout de colonnes via la commande `ALTER TABLE` sans interruption de service.
* **Mise à jour sélective :** Correction et mise à jour de données ciblées via la commande `UPDATE`.