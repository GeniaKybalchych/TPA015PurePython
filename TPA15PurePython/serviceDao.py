# Install requests
from datetime import datetime

from model import create_app

from flask import Flask, jsonify, request

from model import User, db

app = create_app()

@app.route('/insert-data', methods=['POST'])
def insert_data():
    try:
        data = request.json
        # Convertir la date de chaîne de caractères au format `DD-MM-YYYY` en un objet `datetime.date`
        birthdate_obj = datetime.strptime(data['birthdate'], "%d-%m-%Y").date()

        # Convertir l'objet `datetime.date` en chaîne de caractères au format `YYYY-MM-DD`
        formatted_birthdate = birthdate_obj.strftime("%Y-%m-%d")
        new_entry = User(username=data['username'],
                         hostname=data['hostname'],
                         birthdate=formatted_birthdate)

        db.session.add(new_entry)
        db.session.commit()

        return jsonify(status="success", message="Data inserted successfully."), 200
    except Exception as e:
        # Log the error for debugging:
        app.logger.error(f"Error while inserting data: {str(e)}")
        return jsonify(status="error", message=str(e)), 500


# 1. Créer une route pour la requête GET
@app.route('/get-data', methods=['GET'])
def get_all_data():
    userDemandes = User.query.all()
    listUserDemandes = []
    for demandes in userDemandes:
        listUserDemandes.append({'username': demandes.username,
                                 'hostname': demandes.hostname,
                                 'birthdate': demandes.birthdate})

        if len(listUserDemandes) == 0:
            return jsonify({'message': 'Aucune demande trouvée'})

    return jsonify({'userDemandes': listUserDemandes})


if __name__ == '__main__':
    app.run(port=5001, debug=True)