import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
DB_PATH = "coworking_base.db"

@app.route('/')
def home():
    """Affiche le formulaire principal."""
    return render_template('index.html')

@app.route('/ajouter', methods=['POST'])
def ajouter():
    """Gère l'insertion SQL et redirige vers la page de succès."""
    nom = request.form.get('nom')
    secteur = request.form.get('secteur')
    ville = request.form.get('ville')

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO entreprises (nom, secteur, ville) VALUES (?, ?, ?)", 
                (nom, secteur, ville)
            )
            conn.commit()
            
        # On passe le nom de l'entreprise à notre nouveau template de succès
        return render_template('success.html', nom_entreprise=nom)

    except sqlite3.Error as e:
        return f"<h1>❌ Erreur Système</h1><p>{e}</p><a href='/'>Retour</a>", 500

if __name__ == "__main__":
    app.run(debug=True)