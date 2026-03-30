-- ANALYSE 1 : Calcul du Chiffre d'Affaires total par Entreprise (Triple Jointure)
SELECT e.nom AS Client, SUM(s.tarif_heure * r.duree_heures) AS CA_Cumulé
FROM entreprises e
JOIN membres m ON e.id = m.entreprise_id
JOIN reservations r ON m.id = r.membre_id
JOIN salles s ON s.id = r.salle_id
GROUP BY e.nom
ORDER BY CA_Cumulé DESC;

-- ANALYSE 2 : Taux d'utilisation des salles (Nombre de réservations par salle)
SELECT s.nom_salle, COUNT(r.id) AS Nb_Occupations
FROM salles s
LEFT JOIN reservations r ON s.id = r.salle_id
GROUP BY s.nom_salle;

-- ANALYSE 3 : Liste des membres sans entreprise rattachée (Contrôle d'anomalie)
SELECT nom_complet, email FROM membres WHERE entreprise_id IS NULL;