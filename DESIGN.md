# Conception du Système de Gestion de Coworking

## Description des Entités (Tables)
- **entreprises** : Registre des sociétés clientes utilisant l'espace.
- **membres** : Utilisateurs individuels rattachés à une entreprise (Relation 1 à Plusieurs).
- **salles** : Catalogue des espaces physiques disponibles (Open Space, Bureaux, Salles de réunion) avec leurs tarifs respectifs.
- **reservations** : Table centrale enregistrant l'utilisation d'une salle par un membre à une date donnée.

## Diagramme Relationnel (ERD)
- Une **Entreprise** possède plusieurs **Membres**.
- Un **Membre** peut effectuer plusieurs **Réservations**.
- Une **Salle** est liée à plusieurs **Réservations**.

## Choix de Conception
- **Normalisation** : Les prix sont stockés dans la table `salles` pour éviter la redondance. 
- **Intégrité** : Utilisation de `PRAGMA foreign_keys = ON` pour garantir que chaque réservation soit liée à un membre et une salle existante.
- **Flexibilité** : La table `salles` permet de modifier le catalogue (ex: ajout d'une salle de sieste) sans modifier la structure des autres tables.

## Limitations connues
Le modèle actuel ne gère pas encore les conflits de créneaux horaires (possibilité théorique de deux réservations sur la même salle à la même heure).