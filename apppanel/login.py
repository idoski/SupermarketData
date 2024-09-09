import customtkinter as ctk
import accountinfo.account as ac
import accountinfo.accountsearch as accs
import apppanel.panel as panel

class LoginPanel(ctk.CTkToplevel):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("500x500")
        self.title("Login Panel")
        
        # For checking if the account creation window exists
        self.create_window = None
        # Setup the login frame        
        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=60, fill="both", expand = True)


        self.label = ctk.CTkLabel(master=self.frame, text="Bargin Bros LLC", font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)


        self.username = ctk.CTkEntry(master=self.frame, placeholder_text="Username")
        self.username.pack(pady=12, padx=10)

        self.password = ctk.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.password.pack(pady=12, padx=10)
        
    def selfdes(self, window):
        window.withdraw()
        window.destroy()
    # Function to create the account creation window
    def create_account(self):
        
        # If statment checks if window exists
        if self.create_window is None or not self.create_window.winfo_exists():
            self.create_window = panel.Panel(800,600,"Create Account")
            
            label = ctk.CTkLabel(master=self.create_window, text="Create an Account", font=("Roboto", 24))
            label.pack(pady=12, padx=10)


            username = ctk.CTkEntry(master=self.create_window, placeholder_text="Username")
            username.pack(pady=12, padx=10)

            password = ctk.CTkEntry(master=self.create_window, placeholder_text="Password")
            password.pack(pady=12, padx=10)
        
            createButton = ctk.CTkButton(master=self.create_window, text="Create Account", command=lambda: [accs.account_create(username.get(),password.get()), self.selfdes(self.create_window)])
            createButton.pack(pady=12, padx=10)

        else:
            self.create_window.focus()