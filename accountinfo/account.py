class Account:
    
    def __init__(self, username, password) -> None:
        super().__init__()
        self.username = username
        self.password = password
        
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password