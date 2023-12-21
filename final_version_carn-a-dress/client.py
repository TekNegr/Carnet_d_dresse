import tkinter as tk 
import customtkinter as ctk
from tkinter import messagebox
from user_db import *

class Window():
    def __init__(self):
        self.win_root = ctk.ctk_tk.CTk() 
        self.win_root.title("CARN'A'DRESS")
        self.widget_array = []
        self.db_processor = DB_Processor()
        
    def run(self):
        self.pack()
        self.win_root.mainloop()
    
    def pack(self):
        for widget in self.widget_array:
            widget.pack(pady=20, padx=20)
        
    def close(self):
        self.win_root.destroy()
 
 
   
class welcome_window(Window):
    def __init__(self):
        super().__init__()
        self.win_root.geometry("800x500")
        title = """
        WELCOME TO
        CARN'A'DRESS"""
        self.title_Label = tk.Label(self.win_root, text=title, font=("Arial",32))
        self.widget_array.append(self.title_Label)
        self.question_label = tk.Label(self.win_root, text="How would you like to connect ?", font=("Arial",26))
        self.btn_login = ctk.CTkButton(self.win_root, width=100, height=50, corner_radius=10,text="Login",fg_color="#0000BB",hover_color="#F1555F", command=self.go_to_login)
        self.widget_array.append(self.btn_login)
        self.btn_signup = ctk.CTkButton(self.win_root, width=100, height=50, corner_radius=10,text="Sign Up",fg_color="#0000BB",hover_color="#F1555F", command=self.go_to_sign_up)
        self.widget_array.append(self.btn_signup)
        
        
    def go_to_sign_up(self):
        self.close()
        signup_window = SignUp_Window()
        signup_window.run()
        
    def go_to_login(self):
        self.close()
        Login_Window = login_Window()
        Login_Window.run()
        
    
           
class login_Window(Window):
    def __init__(self):
        super().__init__()
        self.win_root.geometry("800x500")
        self.Label = tk.Label(self.win_root, text="LET'S LOGIN !!!!!", font=("Arial",22))
        self.widget_array.append(self.Label)
        self.username_entry = ctk.CTkEntry(self.win_root, width=140, height=28, corner_radius=10,placeholder_text="username" )
        self.widget_array.append(self.username_entry)
        self.pwd_entry = ctk.CTkEntry(self.win_root, width=140, height=28, corner_radius=10,placeholder_text="password")
        self.pwd_entry.configure(show="*")
        self.widget_array.append(self.pwd_entry)
        self.btn_login = ctk.CTkButton(self.win_root, width=100, height=32, corner_radius=10,text="Login",fg_color="#0000BB",hover_color="#F1555F", command=self.check_login)
        self.widget_array.append(self.btn_login)
        self.change_type_accounts = ctk.CTkButton(self.win_root, width=200, height=22, corner_radius=10,text="No account yet",fg_color="#3333FF",hover_color="#F122F5", command=self.go_to_sign_up)
        self.widget_array.append(self.change_type_accounts)
        
        
    def check_login(self):
        connection_state = 0
        username = self.username_entry.get()
        mdp = self.pwd_entry.get()
        if username!="" and mdp!="":
            self.db_processor.curseur.execute("SELECT * FROM utilisateurs WHERE username = ?",(username,))
            user = self.db_processor.curseur.fetchone()
            correct_mdp = user[4]
            if mdp==correct_mdp:
                msg_title = "Success"
                message = f"Connexion made !!! Welcome {username}"
                connection_state = 1 
            else : 
                msg_title = "Oops"
                message = f"Username or Password incorrect!! please try again"
        else:
            msg_title = "????"
            message="All the fields must be filled before connecting"
        messagebox.showinfo(title=msg_title, message=message)
        if connection_state ==1:
            self.log_into_user(username)
        
        
        
    def log_into_user(self, username):
        
        self.close()
        home_window = Home_Window(username)
        home_window.run()
        
        
    def go_to_sign_up(self):
        self.close()
        signup_window = SignUp_Window()
        signup_window.run()
           
   
class SignUp_Window(Window):
    def __init__(self):
        super().__init__()
        self.win_root.geometry("800x500")
        self.Label = tk.Label(self.win_root, text="CREATE AN ACCOUNT!!!!!", font=("Arial",22))
        self.widget_array.append(self.Label)
        self.username_entry = ctk.CTkEntry(self.win_root, width=140, height=28, corner_radius=10,placeholder_text="username")
        self.widget_array.append(self.username_entry)
        self.email_entry = ctk.CTkEntry(self.win_root, width=140, height=28, corner_radius=10,placeholder_text="email")
        self.widget_array.append(self.email_entry)
        self.name_entry = ctk.CTkEntry(self.win_root, width=140, height=28, corner_radius=10,placeholder_text="Nom")
        self.widget_array.append(self.name_entry)
        self.firstname_entry = ctk.CTkEntry(self.win_root, width=140, height=28, corner_radius=10,placeholder_text="Prenom")
        self.widget_array.append(self.firstname_entry)
        self.pwd_entry = ctk.CTkEntry(self.win_root, width=140, height=28, corner_radius=10,placeholder_text="password")
        self.widget_array.append(self.pwd_entry)
        self.submit_btn = ctk.CTkButton(self.win_root, width=120, height=32, corner_radius=10,text="Create Account",fg_color="#0000BB",hover_color="#F1555F", command=self.check_signup)
        self.widget_array.append(self.submit_btn)
        self.change_type_accounts = ctk.CTkButton(self.win_root, width=200, height=22, corner_radius=10,text="Already have an account?",fg_color="#3333FF",hover_color="#F122F5", command=self.go_to_login)
        self.widget_array.append(self.change_type_accounts)
        
        
    #Check toute la base données pour trouvé     
    def check_signup(self):
        msg_title = ""
        message = ""
        field_checker = self.check_field_entry()
        if field_checker==True:
            username = self.username_entry.get()
            mail = self.email_entry.get()
            self.db_processor.curseur.execute("SELECT * FROM Utilisateurs WHERE username = ?",(username,))
            users_name = self.db_processor.curseur.fetchall()
            self.db_processor.curseur.execute("SELECT * FROM Utilisateurs WHERE email = ?",(mail,))
            users_mail = self.db_processor.curseur.fetchall()      
            
            if len(users_name)>0:
                msg_title = "Sorry.."
                message = f"Someone is already name {username}"
            elif len(users_mail)>0:
                msg_title = "Sorry.."
                message = f"There's already an account with the email : {mail}"  
            
            else: 
                nom = self.name_entry.get()
                prenom = self.firstname_entry.get()
                mdp = self.pwd_entry.get()
                self.db_processor.insert_user(username, nom, prenom, mdp, mail)
                msg_title = "Success!!"
                message = f"Congrats {username} Your account was succesfully created"
        elif field_checker==False:
            msg_title = "Oops!!"
            message = "It seems the fields are not correctly filled. Retry"      
        messagebox.showinfo(title=msg_title, message=message)
        
    #Fonction pouir verifier si tous les fields sont utilisés    
    def check_field_entry(self):
        username = self.username_entry.get()
        nom = self.name_entry.get()
        prenom = self.firstname_entry.get()
        mdp = self.pwd_entry.get()
        
        if (username != "") and (nom != "") and (prenom != "") and (mdp != ""):
            field_checker = True
        else:
            field_checker = False
            
        return field_checker
    
    def go_to_login(self):
        self.close()
        Login_Window = login_Window()
        Login_Window.run()
        

class Home_Window(Window):
    def __init__(self,username):
        super().__init__()
        self.win_root.geometry("800x500")
        self.user = User(username, self.db_processor)
        welcome_text = f"Welcome {self.user.username}"
        self.label = tk.Label(self.win_root, text=welcome_text, font=("Arial",22))
        self.widget_array.append(self.label)
        
        self.settings_btn = ctk.CTkButton(self.win_root, width=30,height=30,corner_radius=15, fg_color="#FF0000" ,text="",command=self.go_to_settings)
        self.widget_array.append(self.settings_btn)        
        #Search Bar
        self.search_frame = tk.Frame(self.win_root)
        self.search_frame.columnconfigure(0,weight=1)
        self.search_frame.columnconfigure(1,weight=1)
        self.search_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Search for contacts")
        self.search_entry.grid(row=0,column=0)
        self.search_btn = ctk.CTkButton(self.search_frame, width=30,height=30,corner_radius=15, fg_color="#666666" ,text="",command=self.Search_contact)
        self.search_btn.grid(row=0,column=1)
        
        self.widget_array.append(self.search_frame)
        
        
        self.selected_user = None
        self.create_home_window()
        
        
    def create_home_window(self):
        self.Mainframe = tk.Frame(self.win_root)
        self.Mainframe.columnconfigure(0,weight=1)
        self.Mainframe.columnconfigure(1,weight=1)
        self.createLeftBlock()
        self.createRightBlock()
        
        
    def run(self):
        self.pack()
        self.Mainframe.pack(fill="both",expand=True)
        self.win_root.mainloop()
        
        
    def createLeftBlock(self):
        self.left_frame = tk.Frame(self.Mainframe)
        if self.user.pdp_url != "" and self.user.pdp_url != None: 
            profile_pic = tk.Label(self.left_frame, image=self.user.profile_pic)
            profile_pic.pack()
        Names = f"""
        {self.user.nom} {self.user.prenom}
        @{self.user.username}
        """
        name_labels = tk.Label(self.left_frame, text = Names, font=("Arial",20))
        name_labels.pack()
        contact_list_box = tk.Listbox(self.left_frame)
        if len(self.user.contact_list)>0:
            self.get_contact_list(contact_list_box)
        self.left_frame.grid(row=0,column=0)
        
        
    def get_contact_list(self,contact_list_box : tk.Listbox):
        for contact in self.user.contact_list:
            contact_list_box.insert(tk.END,contact)
        
       
    def go_to_settings(self):
        window = Parametres_Client(self.user)  
        self.close()
        window.run() 
        
    def createRightBlock(self):
        self.right_frame = tk.Frame(self.Mainframe)
        if self.selected_user is not None:
            if self.user.pdp_url != "" and self.user.pdp_url != None:
                SU_image = tk.Label(self.right_frame, image=self.selected_user.profile_pic)
                self.widget_array.append(SU_image)
            Names = f"""
            {self.selected_user.nom} {self.selected_user.prenom}
            @{self.selected_user.username}
            """
            Name_label = tk.Label(self.right_frame, text=Names, font=("Arial",20))
            self.widget_array.append(Name_label)
            
            if self.selected_user.username in self.user.contact_list:
                add2contact_btn = ctk.CTkButton(self.right_frame, width=30,height=30,corner_radius=15, fg_color="#666666" ,text="+",command=self.add_search_to_contacts)
                self.widget_array.append(add2contact_btn)
        
        self.right_frame.grid(row=0,column=1)

        
    def Show_Contact_Info(self, username):
       Contact = User(username, self.db_processor)
       contact_Username_Label = tk.Label(self.Mainframe, text=f"@{Contact.username}", font=("Arial",22))
       contact_name_Label = tk.Label(self.Mainframe, text=f"{Contact.nom} {Contact.prenom} ", font=("Arial",22))
       add2contact_btn = ctk.CTkButton(self.Mainframe, width=30,height=30,corner_radius=15, fg_color="#666666" ,text="+",command=self.add_search_to_contacts)
       contact_Username_Label.grid(row=0, column=1)
       contact_name_Label.grid(row=1, column=1)
       add2contact_btn.grid(row=2, column=1)

       
    def add_to_contacts(self):
        self.user.add_to_contacts(self.db_processor, self.selected_user.username)
       
       
       
    #Look for searched Contact in search bar and affiche 
    def Search_contact(self):
        
        search_input = self.search_entry.get()
        if search_input != "" : 
            self.db_processor.curseur.execute("SELECT * FROM Utilisateurs WHERE username = ?",(search_input,))
            result = self.db_processor.curseur.fetchone()
            if result is not None: 
                messagebox.showinfo(title="!!!", message=f"{search_input} existe dans la db")
                self.selected_user = User(search_input, self.db_processor)
                self.createRightBlock()
                
            else:
                messagebox.showinfo(title="...", message=f"{search_input} existe pas...")
        else:
            messagebox.showinfo(title="???", message="Il faut inserer quelque chose dans la barre de recherche :)")
            
        
         
            

        
        


def main():
    window = welcome_window()
    #window = Home_Window()
    window.run()
    
    
    
    
if __name__ == "__main__":
    main()