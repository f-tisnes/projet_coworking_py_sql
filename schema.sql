-- Création des Entreprises
CREATE TABLE entreprises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    secteur TEXT,
    ville TEXT
);

-- Création des Membres liés aux entreprises
CREATE TABLE membres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_complet TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    entreprise_id INTEGER,
    statut_badge TEXT DEFAULT 'Actif',
    FOREIGN KEY (entreprise_id) REFERENCES entreprises(id)
);

-- Création du catalogue des Salles
CREATE TABLE salles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_salle TEXT NOT NULL,
    type_bureau TEXT CHECK(type_bureau IN ('Open Space', 'Bureau Privé', 'Salle de Réunion')),
    capacite INTEGER,
    tarif_heure REAL
);

-- Création des Réservations (Table de transaction)
CREATE TABLE reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    membre_id INTEGER,
    salle_id INTEGER,
    date_resa DATE,
    duree_heures INTEGER,
    FOREIGN KEY (membre_id) REFERENCES membres(id),
    FOREIGN KEY (salle_id) REFERENCES salles(id)
);