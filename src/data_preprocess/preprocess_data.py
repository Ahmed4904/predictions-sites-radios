import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    # Suppression des colonnes inutiles
    df = df.drop(['Nom_site', 'Identifiant (code_site)', 'Longitude', 'Latitude'], axis=1)

    # Encodage des variables catégorielles (exemple avec 'Cluster')
    df['Cluster'] = df['Cluster'].map({'Urbain': 1, 'ZT': 2, 'ZI': 3, 'rural': 4, 'ZB': 5})

    # Standardisation des données numériques
    numeric_columns = ['Taux_de_blocage', 'Trafic_Data_mensuel_moyen_Go', 'HBA']
    scaler = StandardScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

    print("Prétraitement des données terminé.")
    return df
