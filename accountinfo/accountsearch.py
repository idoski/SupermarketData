import pickle
import accountinfo.account as account
from apppanel.panel import Panel
import customtkinter
from pathlib import Path

accounts = {}

try:
    account_file = Path("./saved.pkl")
    if account_file.is_file():
      with open(account_file, 'rb') as fp:
          accounts = pickle.load(fp)
except:
    print("No account file found!")

def pkl_save():
    global accounts
    with open('./saved.pkl', 'wb') as handle:
        pickle.dump(accounts,handle, protocol=pickle.HIGHEST_PROTOCOL)

def account_create(username, password):
    global accounts
    if username in accounts.keys():
        print("account exists already with this username!")
    else:
        accounts[username] = account.Account(username,password)
        pkl_save()

def account_login(username, password):
    global accounts
    if username not in accounts.keys():
        warning = Panel(1000,1000,"Error!")
        warning.resizable(False,False)
        warlabel = customtkinter.CTkLabel(warning, text="No Account Found!",font=("Roboto", 24))
        warlabel.pack(padx=10, pady=10)
    elif accounts[username] is not None and accounts[username].password == password:
        print("got account!")
        return accounts[username]
    elif accounts[username] is not None and accounts[username].password != password:
        warning = Panel(500,500,"Error!")
        warlabel = customtkinter.CTkLabel(warning, text="Wrong Password!", font=("Roboto", 24))
        warlabel.pack()

def account_delete(username):
    try:
        accounts.pop(username)
        pkl_save()
        print("Deleted " + username)
    except:
        print("Account not found!")
        