# Conception du Système de Gestion de Coworking

## 1. Description des Entités (Tables)
Le système repose sur 4 entités pour garantir une base de données normalisée (3NF) :
- **entreprises** : Registre B2B des sociétés clientes utilisant l'espace.
- **membres** : Utilisateurs individuels rattachés à une entreprise (Relation 1:N).
- **salles** : Catalogue physique des espaces disponibles (Open Space, Bureaux privés, Salles de réunion) avec leurs tarifs respectifs.
- **reservations** : Table transactionnelle centrale enregistrant l'utilisation d'une salle par un membre à une date donnée.

---

## 2. Diagramme Entité-Relation (ERD)

```mermaid
erDiagram
    ENTREPRISES ||--o{ MEMBRES : "emploie"
    MEMBRES ||--o{ RESERVATIONS : "effectue"
    SALLES ||--o{ RESERVATIONS : "accueille"

    ENTREPRISES {
        INTEGER id PK
        TEXT nom
        TEXT secteur
        TEXT ville
    }
    MEMBRES {
        INTEGER id PK
        TEXT nom_complet
        TEXT email
        INTEGER entreprise_id FK
        TEXT statut_badge
    }
    SALLES {
        INTEGER id PK
        TEXT nom_salle
        TEXT type_bureau
        INTEGER capacite
        REAL tarif_heure
    }
    RESERVATIONS {
        INTEGER id PK
        INTEGER membre_id FK
        INTEGER salle_id FK
        DATE date_resa
        INTEGER duree_heures
    }

---

## 3. Choix de la conception 

- Normalisation financière : Les prix (tarif_heure) sont stockés de manière statique dans la table salles pour éviter toute redondance et erreur de saisie lors des réservations.

- Intégrité Référentielle : Utilisation stricte des clés étrangères (FOREIGN KEY). Dans l'application Web (Flask), cela se traduit par des listes déroulantes dynamiques : on ne peut inscrire un membre que dans une entreprise existante, et on ne peut réserver une salle que pour un membre existant.

- Flexibilité et Évolutivité : La table salles est conçue comme un catalogue. Il suffit d'ajouter une ligne (ex: "Espace Podcast") pour que le nouveau produit soit instantanément disponible à la réservation dans l'interface Web, sans toucher au code SQL.

---

## 4. Limitations connues

Le modèle actuel est optimisé pour la facturation journalière globale, mais il ne gère pas encore les conflits de créneaux horaires stricts. En théorie, le système actuel autorise l'enregistrement de deux réservations pour la même salle à la même date (Overbooking). Une V2 du projet nécessiterait l'ajout de colonnes heure_debut et heure_fin avec un déclencheur (TRIGGER) SQL pour bloquer les chevauchements.