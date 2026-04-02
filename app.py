import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
DB_PATH = "coworking_base.db"

@app.route('/')
def home():
    """Affiche les formulaires avec les listes dynamiques (Membres, Salles, Entreprises)."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        
        # 1. On récupère les membres pour les réservations
        cur.execute("SELECT id, nom_complet FROM membres ORDER BY nom_complet")
        membres = cur.fetchall()
        
        # 2. On récupère les salles pour les réservations
        cur.execute("SELECT id, nom_salle FROM salles ORDER BY nom_salle")
        salles = cur.fetchall()

        # 3. On récupère les entreprises pour le nouveau membre
        cur.execute("SELECT id, nom FROM entreprises ORDER BY nom")
        entreprises = cur.fetchall()

    return render_template('index.html', membres=membres, salles=salles, entreprises=entreprises)

@app.route('/ajouter_entreprise', methods=['POST'])
def ajouter_entreprise():
    nom = request.form.get('nom')
    secteur = request.form.get('secteur')
    ville = request.form.get('ville')
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO entreprises (nom, secteur, ville) VALUES (?, ?, ?)", (nom, secteur, ville))
            conn.commit()
        return render_template('success.html', message=f"L'entreprise {nom} a bien été ajoutée.")
    except sqlite3.Error as e:
        return f"Erreur : {e}", 500

@app.route('/ajouter_membre', methods=['POST'])
def ajouter_membre():
    """Lie un nouvel humain à une entreprise existante."""
    nom_complet = request.form.get('nom_complet')
    email = request.form.get('email')
    entreprise_id = request.form.get('entreprise_id')
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO membres (nom_complet, email, entreprise_id) VALUES (?, ?, ?)", (nom_complet, email, entreprise_id))
            conn.commit()
        return render_template('success.html', message=f"Le membre {nom_complet} a été rattaché avec succès.")
    except sqlite3.Error as e:
        return f"Erreur : {e}", 500

@app.route('/ajouter_reservation', methods=['POST'])
def ajouter_reservation():
    membre_id = request.form.get('membre_id')
    salle_id = request.form.get('salle_id')
    date_resa = request.form.get('date_resa')
    duree = request.form.get('duree')
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO reservations (membre_id, salle_id, date_resa, duree_heures) VALUES (?, ?, ?, ?)", (membre_id, salle_id, date_resa, duree))
            conn.commit()
        return render_template('success.html', message=f"Réservation confirmée pour le {date_resa}.")
    except sqlite3.Error as e:
        return f"Erreur : {e}", 500

if __name__ == "__main__":
    app.run(debug=True)