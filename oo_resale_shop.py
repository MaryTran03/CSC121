from typing import Dict, Optional
from computer import *

class ResaleShop:
    def __init__(self):
        # Initialize inventory and item ID
        self.inventory: Dict[int, Dict] = {}
        self.itemID: int = 0

    def buy(self, computer) -> int:
        """
        Adds a new computer to the inventory and returns the item ID.
        """
        self.itemID += 1
        self.inventory[self.itemID] = computer

    def update_price(self, item_id: int, new_price: int):
        """
        Updates the price of a computer in the inventory if it exists.
        """
        if item_id in self.inventory:
            self.inventory[item_id].price = new_price
        else:
            print(f"Item {item_id} not found. Cannot update price.")

    def sell(self, item_id: int):
        """
        Removes a computer from the inventory if it exists.
        """
        if item_id in self.inventory:
            del self.inventory[item_id]
            print(f"Item {item_id} sold!")
        else:
            print(f"Item {item_id} not found. Please select another item to sell.")

    def print_inventory(self):
        """
        Prints all the items in the inventory.
        """
        if self.inventory:
            for item_id, details in self.inventory.items():
                print(f"Item ID: {item_id} : {vars(self.inventory[item_id])}")
        else:
            print("No inventory to display.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        """
        Refurbishes a computer by setting an appropriate price based on its year and optionally updating its OS.
        """
        if item_id in self.inventory:
            computer = self.inventory[item_id]
            if computer.year_made < 2000:
                computer.price = 0  # too old to sell, donation only
            elif computer.year_made < 2012:
                computer.price = 250  # heavily-discounted price on machines 10+ years old
            elif computer.year_made < 2018:
                computer.price = 550  # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000  # recent stuff
            if new_os:
                computer.operating_system = new_os  # update OS if provided
        else:
            print(f"Item {item_id} not found. Please select another item to refurbish.")

def main():
    # Create an instance of ResaleShop
    shop = ResaleShop()
    new_computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)

    # Example usage of the ResaleShop methods
    shop.buy(Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500))
    shop.refurbish(1)
    shop.print_inventory()

if __name__ == "__main__":
    main()
