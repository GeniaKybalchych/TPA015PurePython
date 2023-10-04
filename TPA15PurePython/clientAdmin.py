import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def afficher_info_utilisateurs():
    try:
        # Récupérer la liste des utilisateurs
        reponse_utilisateurs = requests.get('http://127.0.0.1:5002/utilisateurs')
        if reponse_utilisateurs.status_code != 200:
            return f"Erreur utilisateurs: {reponse_utilisateurs.status_code} - {reponse_utilisateurs.reason}"

        data_utilisateurs = reponse_utilisateurs.json()
        utilisateurs = data_utilisateurs.get('demandes', {}).get('userDemandes', [])

        # Récupérer le nombre total d'utilisateurs
        reponse_nombre = requests.get('http://127.0.0.1:5002/informations')
        if reponse_nombre.status_code != 200:
            return f"Erreur nombre: {reponse_nombre.status_code} - {reponse_nombre.reason}"

        data_nombre = reponse_nombre.json()
        nombre_utilisateurs = data_nombre.get('nombre_utilisateurs', 0)

        return render_template('index.html', utilisateurs=utilisateurs,
                               nombre_utilisateurs=nombre_utilisateurs)
    except requests.RequestException:
        return "Erreur: Impossible de se connecter au service Analytique."


    
    


if __name__ == '__main__':
    app.run(port=5003, debug=True)
