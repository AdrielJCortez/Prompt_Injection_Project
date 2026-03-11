class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
    
    def is_admin(self):
        return self.role == "admin"