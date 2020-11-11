class Inventory:

    in_inventory = ['Raincoat (worn)', 'Padlock key', 'Parcel']

    @staticmethod
    def take(pack, item):
        pack.append(item)

    @staticmethod
    def remove_item(pack, item):
        pack.remove(item)

