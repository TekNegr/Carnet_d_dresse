class User():
    def __init__(self,Nom,Username,Email,Mdp):
        self.name = Nom
        self.username = Username
        self.email = Email
        self.mdp = Mdp
        
    def print(self):
        print(f"""
              User = {self.name} / @{self.username}
              Email = {self.email}
              """)