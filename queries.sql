-- ACTION 1 : Ajouter un nouveau client (Entreprise et son premier employé)
INSERT INTO entreprises (nom, secteur, ville) VALUES ('DataFuture', 'IA', 'Lyon');
INSERT INTO membres (nom_complet, email, entreprise_id) VALUES ('Alice Martin', 'a.martin@datafuture.com', 11);

-- ACTION 2 : Mettre à jour le statut d'un membre (Perte de badge)
UPDATE membres SET statut_badge = 'Bloqué' WHERE id = 5;

-- ACTION 3 : Modifier le tarif d'une salle pour la saison haute
UPDATE salles SET tarif_heure = 55.0 WHERE nom_salle = 'Grande Conférence';

-- ACTION 4 : Supprimer une réservation annulée
DELETE FROM reservations WHERE id = 1;