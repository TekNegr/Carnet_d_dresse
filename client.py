import sqlite3
import tkinter as tk 
from tkinter import messagebox
from user import User


#root = tk.Tk()

#root.geometry("800x500")

#root.title("Car-Dress")

#label =  tk.Label(root, text="Welcome to the CA!", font=('Arial',22))
#label.pack()




class Client():
    def __init__(self) :
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Carnet d'adresse")
        
users = []

#Client page class for Signing up
class Sign_Up_Client(Client):
    def __init__(self):
        super().__init__()
        self.Label = tk.Label(self.root, text="Create your Account now!", font=('Arial',18), padx=10, pady=10)
        self.Name_Entry = tk.Entry(self.root)
        self.Name_Entry.insert(0, "Nom")
        
        self.Mail_Entry = tk.Entry(self.root)
        self.Mail_Entry.insert(0, "Mail")
        
        self.Username_Entry = tk.Entry(self.root)
        self.Username_Entry.insert(0, "Username")
        
        self.Pwd_Entry = tk.Entry(self.root)
        self.Pwd_Entry.insert(0, "Password")
        
        self.checkstate = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Je respecte la CGU", font=('Arial',16), padx=10, pady=10 , variable=self.checkstate)
        
        self.Submit_button = tk.Button(self.root, text="login", font=('Arial',18), padx=10, pady=10, command=self.create_user_check)
        
        
        
        
    def create_user_check(self):
        name = self.Name_Entry.get()
        username = self.Username_Entry.get()
        mail = self.Mail_Entry.get()
        pwd = self.Pwd_Entry.get()
        
        if (name!=None and username!=None and (mail!=None) and (pwd!=None) ):
            if self.checkstate.get() != 0:
                created_user = self.submit_user
                users.append(created_user)
                message="Profil créé avec Success!"
            else: 
                message="Vous devez accepter la CGU"
            
        else:
            message="Erreur! Un champ est vide"
        messagebox.showinfo(title="Message", message=message)    
        
        
    def submit_user(self):
        name = self.Name_Entry.get()
        username = self.Username_Entry.get()
        mail = self.Mail_Entry.get()
        pwd = self.Pwd_Entry.get()
        created_user = User(name,username,mail,pwd)
        return created_user
    
    def pack(self):
        self.Label.pack()
        self.Name_Entry.pack()
        self.Username_Entry.pack()
        self.Mail_Entry.pack()
        self.Pwd_Entry.pack()
        self.check.pack()
        self.Submit_button.pack()
        

class Home_Client(Client):
    def init(self, user: User):
        super().init()
        self.user = user
        welcome_message = f"Welcome {self.user.name}!!!"
        self.label = tk.Label(self.root, text="Please Login!", font=('Arial',18))
        self.Mainframe = tk.Frame(self.root)
        self.Mainframe.rowconfigure(0, weight=1)
        self.Mainframe.columnconfigure(0,weight=1)
        self.Mainframe.columnconfigure(1,weight=1)
        self.contact_list = tk.Listbox(self.Mainframe, width=50, height=100, font=("Arial",18))
        
        
    def pack(self):
        self.label.pack()
        self.Mainframe.pack()
        self.contact_list.pack()
        
    



#Client page class for Login
class Login_Client(Client):
    def __init__(self):
        super().__init__()     
        self.label = tk.Label(self.root, text="Please Login!", font=('Arial',18))
        self.loginEntry = tk.Entry(self.root)
        self.loginEntry.insert(0, "Username")
        self.PwdEntry = tk.Entry(self.root)
        self.PwdEntry.insert(0, "Password")
        self.checkstate = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Je respecte la CGU", font=('Arial',16), variable=self.checkstate)
        self.loginBtn = tk.Button(self.root, text="login", font=('Arial',18), command=self.check_login)

      
     #prototype for function to check the validity of the login (isn't adapted to the user class yet)         
  
    def check_login(self):
        if self.checkstate.get()==0:
            message = "Vous devez check la box pour pouvoir utiliser votre compte"
        else: 
            username = self.loginEntry.get()
            message = f"Bienvenu {username}"
        messagebox.showinfo(title="Message", message=message)
            
#Printing of the Page 
    def pack(self):
       self.label.pack()
       self.loginEntry.pack()
       self.PwdEntry.pack() 
       self.check.pack() 
       self.loginBtn.pack()
   


#Testing of the Client
#client = Login_Client()
#client = Sign_Up_Client()
user = User("Henin","N1","n1@mail.com","123kk")
client = Home_Client(user)
client.pack()       

client.root.mainloop()