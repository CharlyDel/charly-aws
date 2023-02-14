from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api/v1', methods=['GET'])
def get_data():
    with open("donnees/data.json") as f:
        data = json.load(f)
        results = [{'id': item['id'], 'nom': item['nom'], 'nom_de_famille': item['nom_de_famille'], 'email': item['email']} for item in data]
    return jsonify(results)

if __name__ == '__main__':
    app.run(port=8080)