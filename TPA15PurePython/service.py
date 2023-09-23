from datetime import datetime

import requests
from flask import Flask,request, jsonify

app = Flask(__name__)

def suggest_activity(temperature):
    """Renvoie une suggestion d'activité en fonction de la température."""
    if temperature >= 25:
        return "Natation"
    elif 18 <= temperature < 25:
        return "Tennis"
    elif 2 <= temperature < 18:
        return "Randonnée dans les bois"
    else:
        return "Ski"


@app.route('/suggest_activity/<int:temperature>/<string:birthdate>', methods=['GET'])
def suggest_activity_endpoint(temperature, birthdate):
    """Endpoint pour obtenir une suggestion d'activité."""
    try:
        # Convertir la date de naissance en objet date
        birthdate_obj = datetime.strptime(birthdate, "%d-%m-%Y").date()

        # Vérifiez si la température est dans une plage acceptable
        if temperature < -30 or temperature > 50:
            return jsonify(error="La température fournie est en dehors de la plage acceptable (-30 à 50 °C)."), 400

        # Récupérez les données supplémentaires de l'utilisateur
        username = request.args.get('username')
        hostname = request.args.get('hostname')



        # Valider que toutes les données nécessaires sont présentes
        if not username or not hostname or not birthdate_obj:
            return jsonify(error="Des données nécessaires manquent."), 400

        activity = suggest_activity(temperature)

        # Créez un objet pour stocker toutes les données
        data = {
            "username": username,
            "hostname": hostname,
            "birthdate": birthdate_obj.strftime("%d-%m-%Y"),

        }

        # Imprimez les données pour vérification
        print(data)

        # Appelez le service DAO pour insérer les données dans la BD
        response = requests.post('http://127.0.0.1:5001/insert-data', json=data)
        if response.status_code != 200:
            return jsonify(error=f"Erreur lors de l'insertion des données. Response: {response.text}"), 500
        return jsonify(activity=activity)
    except Exception as e:
        # Capturez toute autre erreur inattendue
        import traceback
        traceback.print_exc()
        return jsonify(error=f"Une erreur inattendue s'est produite: {str(e)}"), 500

if __name__ == '__main__':
    app.run(debug=True)
