print("Sanio Frederic,1AY24AI099,SEC-O")
def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        item_total += count
    print(f"Total number of items: {item_total}")

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

# Example inventory and loot
inventory = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Add loot and display updated inventory
inventory = add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)
