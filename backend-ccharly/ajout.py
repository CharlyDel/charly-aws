from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# route pour saisir les données
@app.route('/api/v1', methods=['POST'])
def saisir_donnees():
    # récupérer les données saisies
    id = request.form['id']
    nom = request.form['nom']
    nom_de_famille = request.form['nom_de_famille']
    mail = request.form['mail']

    # créer un dictionnaire avec les données
    donnees = {
        "id": id,
        "nom": nom,
        "nom_de_famille": nom_de_famille,
        "mail": mail
    }

    # ouvrir le fichier JSON en mode écriture
    with open("donnees/data.json", "w") as f:
        # écrire les données dans le fichier au format JSON
        json.dump(donnees, f)

    # renvoyer une réponse HTTP avec les données saisies
    reponse = {"message": "Données enregistrées : id={}, nom={}, nom_de_famille={}, mail={}".format(id, nom, nom_famille, mail)}
    return jsonify(reponse)

# route pour récupérer les données enregistrées
@app.route('/api/v2', methods=['GET'])
def recuperer_donnees():
    # ouvrir le fichier JSON en mode lecture
    with open("donnees/data.json", "r") as f:
        # lire les données du fichier au format JSON
        donnees = json.load(f)

    # renvoyer les données sous forme de réponse HTTP
    return jsonify(donnees)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
