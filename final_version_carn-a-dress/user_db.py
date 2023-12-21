import sqlite3
import json
from sqlite3 import Error
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

class DB_Processor():
    def __init__(self):
        # Connexion à la base de données SQLite - XAVIER
        connexion_sqlite = sqlite3.connect('Clients_Users.sqlite')
        self.connexion = connexion_sqlite
        self.curseur = self.connexion.cursor()
        self.create_table_user()
        #self.insert_user('JoDonut','John', 'Doe', 'mot_de_passe_de_john')
        #self.insert_user('Mister_KK','KK', 'pipi', 'mot_de_passe_de_KK')
    
    # Fonction pour créer la table Utilisateurs - XAVIER    
    def create_table_user(self):
        try:
            self.curseur.execute('''
            CREATE TABLE IF NOT EXISTS Utilisateurs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                nom TEXT,
                prenom TEXT,
                mot_de_passe TEXT,
                email TEXT,
                PDP_url TEXT,
                contact_list JSON 
                
            )
        ''')
            self.connexion.commit()
            print("Table Utilisateurs créée avec succès.")
        except Error as e:
            print(e)
            
    # Fonction pour insérer un nouvel utilisateur - XAVIER
    def insert_user(self,username, nom_utilisateur, prenom_utilisateur, mot_de_passe,email):
        try:
            self.curseur.execute('''
                INSERT INTO Utilisateurs (username, nom, prenom, mot_de_passe,email) VALUES (?,?, ?, ?,?)
            ''', (username,nom_utilisateur, prenom_utilisateur, mot_de_passe,email))
            self.connexion.commit()
            print(f"Utilisateur {prenom_utilisateur} {nom_utilisateur} : @{username} inséré avec succès.")
        except Error as e:
            print(e)
            
    #Fonction pour chercher et afficher tous les utilisateurs dans la base de données - HENINTSOA        
    def fetch_users(self):
        try:
            self.curseur.execute('SELECT * FROM Utilisateurs')
            users = self.curseur.fetchall()
            
            if len(users) >0:
                print("All users : ")
                for user in users:
                    print(f"Username : {user[1]} - Nom : {user[2]} - Prenom : {user[3]} - MDP : {user[4]}")
            else:
                print("No users found")
        except Error as e:
            print(e)

    def fetch_user(self, username):
        try:
            self.curseur.execute('SELECT * FROM Utilisateurs WHERE username = ?',(username))
            user = self.curseur.fetchone()
            
            if user:
                print("user found: ")
                print(f"Username : {user[1]} - Nom : {user[2]} - Prenom : {user[3]} - MDP : {user[4]} - EMAIL {user[5]}")
            else:
                print("No users found")
        except Error as e:
            print(e)
      
      
    #Recherche tous les contacts d'un utilisateur      
    def fetch_contacts(self, username):
        self.curseur.execute('SELECT contact_list FROM Utilisateurs WHERE username = ?',(username,))
        result = self.curseur.fetchone()[0]
        if result is not None:
            contact_list = json.loads(result)
        else : 
            contact_list = []
        return contact_list
    
    #update la liste des contacts
    def update_contacts(self, username, contact_list):
        self.curseur.execute('UPDATE Utilisateurs SET contact_list = ? WHERE username = ?',(contact_list, username))
        self.connexion.commit()
        print("Contacts updated succesfully")
        
        


    
    
class User():
    def __init__(self,username, db_Processor: DB_Processor):
        db_Processor.curseur.execute("SELECT * FROM Utilisateurs WHERE username = ?",(username,))
        user = db_Processor.curseur.fetchone()
        if user is not None:
            self.username = username
            self.nom = user[2]
            self.prenom = user[3]
            self.mdp = user[4]
            self.email = user[5]
            self.pdp_url = user[6]
            if self.pdp_url != "" and self.pdp_url != None:
                self.fetch_profile_pic()
            self.contact_list = db_Processor.fetch_contacts(self.username)
            
        else:
            messagebox.showinfo(title="Oops",message="Error - No account found")
        
      
    def fetch_profile_pic(self):
        response = requests.get(self.pdp_url)
        profile_image = Image.open(BytesIO(response.content))
        profile_image = Image.resize((100,100))
        profile_pic = ImageTk.PhotoImage(profile_image)
        self.profile_pic = profile_pic
        
    #a tester    
    def show_contacts(self, db_Processor: DB_Processor):
        for contact in self.contact_list:
            db_Processor.curseur.execute("SELECT * FROM Utilisateurs WHERE username = ?",(contact,))
            user = db_Processor.curseur.fetchone()
            print(f"Contact : @{user[1]} {user[2]} {user[3]}")
       
    #a tester        
    def add_to_contacts(self, db_Processor: DB_Processor, username):
        if username not in self.contact_list:
            self.contact_list.append(username)
            db_Processor.update_contacts(self.username, self.contact_list)
            msg_title = "Success"
            message = "Contact added succesfully"
        else:
            msg_title ="oops"
            message = "Contact already in the list"
        messagebox.showinfo(title=msg_title, message=message)
     
     #a tester       
    def remove_from_contacts(self, db_Processor : DB_Processor, username):
        if username in self.contact_list:
            self.contact_list.remove(username)
            db_Processor.update_contacts(self.username, self.contact_list)
            msg_title = "Success"
            message = "Contact deleted succesfully"
        else:
            msg_title ="oops"
            message = "Contact not in the list"
            messagebox.showinfo(title=msg_title, message=message)
            
        
        
        
    
        


db_user = DB_Processor()
db_user.fetch_users()
db_user.connexion.commit()
db_user.connexion.close()