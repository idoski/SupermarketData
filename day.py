class Day():
    
    def __init__(self, day_num) -> None:
        super().__init__()
        self.day_num = day_num
        self.num_items = 0
        self.items = {}
        
    def create_item(self,item_name):
        self.items[item_name] = 0
        print("Item created!")
        
    def inc_item(self, item_name, amount):
        self.items[item_name] += amount
        
    def dec_item(self, item_name, amount):
        self.items[item_name] -= amount