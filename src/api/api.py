import sys
import os
from flask import Flask, jsonify, request
from bson import json_util, ObjectId
from flask_cors import CORS

# Ajouter le chemin du dossier racine au sys.path pour accéder au module src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Importation du module MongoDB
from src.api.mongodb_connection import connect_to_mongodb

app = Flask(__name__)
client = connect_to_mongodb()
CORS(app)

db = client["votre_base_de_donnees"]
collection = db["votre_collection"]

# Fonction pour convertir l'ObjectId en chaîne de caractères
def convert_objectid_to_str(document):
    document['_id'] = str(document['_id'])  # Convertit l'ObjectId en chaîne
    return document

@app.route('/sites', methods=['GET'])
def get_sites():
    # Récupérer tous les documents de la collection
    sites = list(collection.find())
    
    # Convertir chaque document pour remplacer les ObjectId par des chaînes de caractères
    sites = [convert_objectid_to_str(site) for site in sites]
    
    return jsonify(sites)

@app.route('/site', methods=['POST'])
def add_site():
    data = request.get_json()
    collection.insert_one(data)
    return jsonify({"message": "Site ajouté avec succès !"})

@app.route('/site/<site_id>', methods=['GET'])
def get_site(site_id):
    # Convertir site_id en ObjectId
    try:
        site_id = ObjectId(site_id)
    except Exception as e:
        return jsonify({"erreur": "Format de site_id invalide"}), 400

    # Recherche du site par ObjectId
    site = collection.find_one({"_id": site_id})

    if not site:
        return jsonify({"erreur": "Site non trouvé"}), 404

    # Convertir l'ObjectId en chaîne
    site = convert_objectid_to_str(site)
    
    return jsonify(site)

@app.route('/site/<site_id>', methods=['PUT'])
def update_site(site_id):
    data = request.get_json()

    # Convertir site_id en ObjectId
    try:
        site_id = ObjectId(site_id)
    except Exception as e:
        return jsonify({"erreur": "Format de site_id invalide"}), 400

    # Mise à jour du site avec l'ObjectId
    collection.update_one({"_id": site_id}, {"$set": data})
    return jsonify({"message": "Site mis à jour avec succès !"})

@app.route('/site/<site_id>', methods=['DELETE'])
def delete_site(site_id):
    # Convertir site_id en ObjectId
    try:
        site_id = ObjectId(site_id)
    except Exception as e:
        return jsonify({"erreur": "Format de site_id invalide"}), 400

    # Suppression du site avec l'ObjectId
    collection.delete_one({"_id": site_id})
    return jsonify({"message": "Site supprimé avec succès !"})

if __name__ == "__main__":
    app.run(debug=True)
