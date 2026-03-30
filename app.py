from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Route principale : affiche le formulaire
@app.route('/')
def home():
    return render_template('index.html')

# Route qui reçoit les données du formulaire
@app.route('/ajouter', methods=['POST'])
def ajouter():
    nom = request.form['nom']
    secteur = request.form['secteur']
    ville = request.form['ville']

    # Connexion à ta base existante
    conn = sqlite3.connect("coworking_base.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO entreprises (nom, secteur, ville) VALUES (?, ?, ?)", (nom, secteur, ville))
    conn.commit()
    conn.close()

    return f"<h1>Succès !</h1><p>L'entreprise {nom} a bien été ajoutée. <a href='/'>Retour</a></p>"

if __name__ == "__main__":
    app.run(debug=True)