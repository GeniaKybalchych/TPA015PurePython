import requests

from flask import Flask, jsonify

from flasgger import Swagger, swag_from

app = Flask(__name__)

#documentation swagger
app.config ['SWAGGER'] = {
    'title': 'Service analityque',
    'version':1.0
}


# chercher l'api du service DAO
service_dao_url = 'http://127.0.0.1:5001/get-data'


reponse = requests.get(service_dao_url)

#  methode GET pour afficher les tous les utilisateurs
@app.route('/utilisateurs', methods=['GET'])
@swag_from({
    'description': "Ajoute un nouvel utilisateur",
    'responses': {
        '200': {'description': 'Utilisateur ajouté'},
        '500': {'description': 'Erreur lors de l’ajout'}
    }
})

def get_all_demandes():
    try:
        reponse = requests.get(service_dao_url)
        if reponse.status_code == 200:
            return jsonify({'demandes': reponse.json()})
        else:
            return jsonify({'message':'Aucune demande trouvée'}),400

    except requests.RequestException:
        return jsonify({'message': 'Service DAO non disponible'}), 500



#  methode GET pour afficher combien il y ad' utilisateurs
@app.route('/informations', methods=['GET'])
@swag_from({
    'description': "Renvoie le nombre d'utilisateurs",
    'responses': {
        '200': {'description': 'Nombre d’utilisateurs renvoyé'},
        '400': {'description': 'Erreur dans les données'},
        '500': {'description': 'Erreur du serveur'}
    }
})


def get_count_utilisateur() :
    try:
        reponse = requests.get(service_dao_url)
        if reponse.status_code == 200:
            utilisateurs = reponse.json()
            nombre_utilisateurs = len(utilisateurs)
            return jsonify({'nombre_utilisateurs': nombre_utilisateurs})
        else:
            return jsonify({'message': 'information non disponible '}), 400

    except requests.RequestException:
        return jsonify({'message': 'Service DAO non disponible'}), 500

if __name__ == '__main__':
    swagger = Swagger(app)
    app.run(port=5002, debug=True)