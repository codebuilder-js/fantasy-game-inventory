playerInventory = {'arrow': 12,
                   'gold coin': 42,
                   'rope': 1,
                   'torch': 6,
                   'dagger': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    totalItems = 0

    print('Inventory:')

    for item, value in inventory.items():
        print(f' - {item} {value}')
        totalItems += value

    print(f'Total number of items: {totalItems}')

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

addToInventory(playerInventory, dragonLoot)
displayInventory(playerInventory)