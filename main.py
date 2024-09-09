# Imports
import customtkinter
import apppanel.login as lp
import accountinfo.accountsearch as accs
from apppanel.interface import Interface

# CTK settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

curr_account = None
app = Interface()
app.withdraw()

def log_close():
    print("closing!")
    global curr_account
    if curr_account is None:
        lwind.withdraw()
        lwind.quit()
        app.withdraw()
        app.quit()
    else:
        lwind.withdraw()
        lwind.quit()
# Simple function to stop any weird processes from continuing after program is closed
def close():
    print("closing")
    app.withdraw()
    app.quit()
        
# Login logic, only lasts as long as you arent logged in
if curr_account is None:
    def login(entry1, entry2):
        username = entry1.get()
        password = entry2.get()
        logged_account = accs.account_login(username, password)
        if logged_account is not None:
            global curr_account
            curr_account = logged_account
            lwind.destroy()
            app.deiconify()

    lwind = lp.LoginPanel()
    lwind.attributes('-topmost',True)

    loginButton = customtkinter.CTkButton(master=lwind.frame, text="Login", command=lambda: login(lwind.username, lwind.password))
    loginButton.pack(pady=12, padx=10)
        
    accountCreation = customtkinter.CTkButton(master=lwind.frame, text="Create account", font=("Roboto", 12), width=0, height=0, command=lambda: lwind.create_account())
    accountCreation.pack(pady=12, padx=10)
    lwind.protocol("WM_DELETE_WINDOW", log_close)
#----------------END LOGIN--------------------
    
app.protocol("WM_DELETE_WINDOW", close)
app.mainloop()