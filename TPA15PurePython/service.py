from datetime import datetime
from datetime import datetime, timedelta
import jwt
import requests
from flask import Flask,request, jsonify
from flasgger import Swagger, swag_from


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Le renard saute la barriere'
app.config['SWAGGER'] = {
    'title': 'Gestion d’activités basées sur la température',
    'version': '1.0'
}

swagger = Swagger(app)

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

@app.route('/signup', methods=['GET'])
def signup():
    expiration_date = datetime.utcnow() + timedelta(seconds=300)
    token = jwt.encode({'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='HS256')
    return token

@app.route('/suggest_activity/<int:temperature>/<string:birthdate>', methods=['GET'])
@swag_from({
    'responses': {
        '200': {
            'description': 'Retourne une suggestion d’activité basée sur la température',
            'schema': {
                'type': 'object',
                'properties': {
                    'activity': {
                        'type': 'string'
                    }
                }
            }
        }
    },
    'parameters': [
        {
            'name': 'temperature',
            'in': 'path',
            'type': 'integer',
            'description': 'La température actuelle'
        },
        {
            'name': 'birthdate',
            'in': 'path',
            'type': 'string',
            'description': 'La date de naissance au format JJ-MM-AAAA'
        },
        {
            'name': 'username',
            'in': 'query',
            'type': 'string',
            'description': 'Le nom d’utilisateur'
        },
        {
            'name': 'hostname',
            'in': 'query',
            'type': 'string',
            'description': 'Le nom de l’hôte'
        },
        {
            'name': 'token',
            'in': 'query',
            'type': 'string',
            'description': 'JWT pour l’authentification'
        }
    ]
})
def suggest_activity_endpoint(temperature, birthdate):
    # Vérifiez le JWT
    token = request.args.get('token')
    try:
        jwt.decode(token, key=app.config['SECRET_KEY'], algorithms=['HS256', ])
    except:
        return jsonify({'Erreur': 'Token non valide'})

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
