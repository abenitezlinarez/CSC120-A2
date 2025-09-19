from Computer import Computer
from typing import Optional
class resale_shop:
    inventory : list = []
    def __init__(self):
        self.inventory = []
        
    def buy(self, Computer: Computer):
        self.inventory.append(Computer)
        return self.inventory.index(Computer)

    def update_price(self, item_id: int, new_price: int):
        if self.inventory[item_id] is not None:
            self.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def sell(self,item_id: int):
        if item_id < len(self.inventory) :
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: {self.inventory.index(item)}')
                item.printComputer()
        else:
            print("No inventory to display.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if self.inventory[item_id] is not None:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

def main():
    computer1: Computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,"macOS Big Sur", 2013, 1500, 1)
    my_shop = resale_shop()
    my_shop.print_inventory()
       # Add it to the resale store's inventory
    print("Buying", computer1.description)
    print("Adding to inventory...")
    computer_id = my_shop.buy(computer1)
    print("Done.\n")
    print("Checking inventory...")
    my_shop.print_inventory()
    print("Done.\n")
     # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    my_shop.refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    my_shop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    my_shop.sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    my_shop.print_inventory()
    print("Done.\n")

    #my_shop.sell(computer_id)
    print("hi")

main()
