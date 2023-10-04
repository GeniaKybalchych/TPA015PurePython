import requests

from flask import Flask, jsonify


app = Flask(__name__)


# 1. chercher l'api du service DAO
service_dao_url = 'http://127.0.0.1:5001/get-data'


reponse = requests.get(service_dao_url)

#  methode GET pour afficher les tous les utilisateurs
@app.route('/utilisateurs', methods=['GET'])
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
    app.run(port=5002, debug=True)