class Day():
    
    def __init__(self, day_num) -> None:
        super().__init__()
        self.day_num = day_num
        self.locked = False
        self.items = {}
        
    def create_item(self,item_name, amount):
        if self.locked is False:
            self.items[item_name] = amount
            print("Item created!")
        else:
            print("locked")
        
    def change_item(self, item_name, amount):
        if self.locked is False:
            self.items[item_name] = amount
        else:
            print("locked!")
            
    def lock(self):
        self.locked = True
    
    