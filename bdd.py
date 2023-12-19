import sqlite3
import json
from sqlite3 import Error

# Connexion à la base de données SQLite
connexion_sqlite = sqlite3.connect('Clients_Users.sqlite')
curseur_sqlite = connexion_sqlite.cursor()

# Lecture du fichier JSON exporté depuis MongoDB
with open('Clients.Users.json', 'r') as fichier_json:
    donnees_clients_users = json.load(fichier_json)

# Création de la table "Clients_Users" dans SQLite
curseur_sqlite.execute('''
    CREATE TABLE IF NOT EXISTS Clients_Users (
        _id INTEGER PRIMARY KEY,
        nom TEXT,
        prenom TEXT,
        mot_de_passe TEXT
    )
''')

# Insertion des données dans la table "Clients_Users"
for client in donnees_clients_users:
    curseur_sqlite.execute('''
        INSERT INTO Clients_Users (_id, nom, prenom, mot_de_passe)
        VALUES (?, ?, ?, ?)
    ''', (client.get('_id'), client.get('nom'), client.get('prenom'), client.get('mot_de_passe')))

# Validation des changements
connexion_sqlite.commit()

# Fonction pour créer la table Utilisateurs
def creer_table_utilisateurs(connexion):
    try:
        curseur = connexion.cursor()
        curseur.execute('''
            CREATE TABLE IF NOT EXISTS Utilisateurs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                prenom TEXT,
                mot_de_passe TEXT
            )
        ''')
        connexion.commit()
        print("Table Utilisateurs créée avec succès.")
    except Error as e:
        print(e)

# Fonction pour insérer un nouvel utilisateur
def inserer_utilisateur(connexion, nom_utilisateur, prenom_utilisateur, mot_de_passe):
    try:
        curseur = connexion.cursor()
        curseur.execute('''
            INSERT INTO Utilisateurs (nom, prenom, mot_de_passe) VALUES (?, ?, ?)
        ''', (nom_utilisateur, prenom_utilisateur, mot_de_passe))
        connexion.commit()
        print(f"Utilisateur {prenom_utilisateur} {nom_utilisateur} inséré avec succès.")
    except Error as e:
        print(e)

# Utilisation de la fonction pour créer la table "Utilisateurs"
creer_table_utilisateurs(connexion_sqlite)

# Utilisation de la fonction pour insérer un nouvel utilisateur
inserer_utilisateur(connexion_sqlite, 'John', 'Doe', 'mot_de_passe_de_john')

# Validation des changements
connexion_sqlite.commit()

# Fermeture de la connexion SQLite
connexion_sqlite.close()
