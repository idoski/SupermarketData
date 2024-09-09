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
        newday_button.pack(pady=5, padx=5, anchor="nw")
        self.days = {}
        
    
    # Create day function
    def new_day(self):
        day_object = day.Day("Default")
        print(day_object)
        tempPanel = panel.Panel(1000,1000,"New Day")
        tempPanel.focus()
        name = ctk.CTkEntry(master= tempPanel, placeholder_text="Day Number/Name")
        name.pack(pady=12, padx=10)
        
        i_name = ctk.CTkEntry(master= tempPanel, placeholder_text="Item name")
        i_name.pack(pady=12, padx=10)
        
        i_amount = ctk.CTkEntry(master= tempPanel, placeholder_text="Amount")
        i_amount.pack(pady=12, padx=10)
        
        save_i = ctk.CTkButton(master=tempPanel, text="Add Item", command=lambda: saving_i(self, day_object, i_name.get(), i_amount.get()))
        save_i.pack(pady=12, padx=10)
        
        save_day = ctk.CTkButton(master=tempPanel, text="Save Day", command=lambda: self.save(day_object))
        save_day.pack(pady=12, padx=10)
        
        def saving_i(self, day, item, amount):
            day.create_item(item, amount)
            print("item saved!")

    
    def save(self, day_object):
        self.days[day_object.day_num] = day_object
        self.refresh()
        
    def refresh(self):
        for item in self.days.values():
            button = ctk.CTkButton(master=self, text="{item.day_num}", command=lambda: self.day_search(item.day_num))
            button.pack(pady=5, padx=5, anchor="nw")
            print("day saved")
            
    def day_search(day_name):
        pass
    
    