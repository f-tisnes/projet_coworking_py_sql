# Système de Gestion de Coworking - SQL, Python & Flask

## Auteur
**TISNES Francesca** - Mars 2026

---

## Présentation du Projet
Ce projet propose une solution complète pour la gestion d'un espace de coworking. Il démontre la transition d'un stockage de données plat (type Excel) vers une **architecture relationnelle normalisée** sous SQLite, couplée à une **interface web dynamique** (Flask) pour la gestion administrative quotidienne.

### Pourquoi ce projet ?
La gestion par tableur est limitée par la redondance des données et les risques d'incohérence. Cette solution garantit :
- **L'intégrité des données** : Les membres sont strictement rattachés à des entreprises via des clés étrangères.
- **L'automatisation** : Génération de rapports financiers instantanés via des jointures SQL complexes.
- **L'accessibilité et l'Ergonomie** : Une interface Web moderne (design SaaS) permet aux utilisateurs non techniques d'interagir avec la base de données en toute simplicité.

---

## Architecture des Données
Le système repose sur **4 tables** optimisées pour éviter toute redondance :

| Table | Rôle | Clé Étrangère |
| :--- | :--- | :--- |
| **entreprises** | Référentiel des sociétés clientes (B2B) | - |
| **membres** | Registre des utilisateurs individuels | `entreprise_id` |
| **salles** | Catalogue des espaces (Open Space, Bureaux) et tarifs | - |
| **reservations** | Historique des occupations et transactions | `membre_id`, `salle_id` |

---

## Installation et Démarrage

### 1. Préparation de l'environnement
1. Ouvrir le dossier `Projet_TISNES` dans **Visual Studio Code**.
2. Activer l'environnement virtuel :
   - Sur Mac/Linux : `source .venv/bin/activate`
   - Sur Windows : `.venv\Scripts\activate`
3. Installer les bibliothèques nécessaires :
   pip install -r requirements.txt

2. Initialisation et Simulation
Exécutez l'intégralité du Notebook gestion_coworking.ipynb.

    Résultat : Le script crée la structure SQL, génère 100 réservations fictives via Faker pour le test, et produit le fichier rapport_activite.csv.

---

### Utilisation de l'Interface Web (Direction)
Pour permettre au directeur d'ajouter manuellement des entreprises sans toucher au code, une interface Flask est disponible.

1. Lancer le serveur :
Dans le terminal VS Code, tapez :
python app.py

2. Accéder à l'interface :
Ouvrez votre navigateur à l'adresse suivante : http://127.0.0.1:5000

3. Fonctionnalité de l'application Web :
   - Interface Moderne : Design type SaaS, responsive, utilisant la typographie 'Inter' et des animations fluides.
   - Sécurité SQL : Utilisation de requêtes paramétrées pour bloquer les injections SQL.
   - Fiabilité : Gestion des erreurs (try/except) et utilisation de gestionnaires de contexte (with) pour protéger la base de données même en cas de crash.
   - Feedback Utilisateur : Redirection vers une page de succès (success.html) avec validation visuelle.

---

### Contenu du Dépôt (Livrables)

- **app.py** : Moteur de l'application Web Flask.
- **templates/** : Dossier contenant les interfaces HTML/CSS (index.html et success.html).
- **DESIGN.md** : Documentation technique et diagramme entité-relation (ERD).
- **schema.sql** : Script SQL de création des tables et contraintes.
- **queries.sql** : Requêtes SQL de manipulation quotidienne (Insert, Update, Delete).
- **analysis.sql** : Requêtes SQL d'analyse financière (JOIN, SUM, GROUP BY).
- **requirements.txt** : Liste des dépendances Python.

--- 

Projet réalisé par Francesca TISNES - M1 APE - DS2E 
