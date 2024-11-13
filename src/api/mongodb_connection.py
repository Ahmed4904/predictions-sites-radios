# src/api/mongodb_connection.py
from pymongo import MongoClient

def connect_to_mongodb():
    CONNECTION_STRING = 'mongodb+srv://boubacarsow:boubacar@cluster0.zaueiei.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
    
    try:
        client = MongoClient(CONNECTION_STRING)
        print("Connexion à MongoDB réussie.")
        return client
    except Exception as e:
        print(f"Erreur lors de la connexion à MongoDB: {e}")
        return None

# Appel de la fonction sans paramètre puisque la chaîne de connexion est intégrée
client = connect_to_mongodb()


