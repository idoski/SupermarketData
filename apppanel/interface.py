import customtkinter as ctk
import accountinfo.account as ac
import accountinfo.accountsearch as accs
import apppanel.panel as panel
import day

class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x900")
        self.title("Bargain Bros LLC")
        newday_button = ctk.CTkButton(master=self, text="New Day", command=lambda: self.new_day())
        newday_button.pack(pady=12, padx=10)
        self.days = {}
        
    
    # Create day function
    def new_day(self):
        day_object = day.Day(len(self.days))
        tempPanel = panel.Panel(800,600,"New Day")
        name = ctk.CTkEntry(master= tempPanel, placeholder_text="Day Number/Name")
        name.pack(pady=12, padx=10)
            
        add_button = ctk.CTkButton(master=tempPanel, text="Add Item", command=lambda: self.add(self))
        add_button.pack(pady=12, padx=10)
        
        save_day = ctk.CTkButton(master=tempPanel, text="Save", command=lambda: self.save(self, day_object))
        save_day.pack(pady=12, padx=10)
    
    
    # Add Function
    def add(self, day_object):
        tempPanel = panel.Panel(800,600,"Add Item")
        name = ctk.CTkEntry(master= tempPanel, placeholder_text="Item name")
        name.pack(pady=12, padx=10)
        
        amount = ctk.CTkEntry(master= tempPanel, placeholder_text="Amount")
        amount.pack(pady=12, padx=10)
        
        save_item = ctk.CTkButton(master=tempPanel, text="Save", command=lambda: save_it(self))
        save_item.pack(pady=12, padx=10)
        
        def save_it(self):
            day_object.create_item(name, amount)
    
    
    def save(self, day_object):
        self.days[day_object.day_num] = day_object
        self.refresh()
        
    def refresh(self):
        for item in self.days.items():
            ctk.CTkLabel(master=self, text=item.day_num)
    
    