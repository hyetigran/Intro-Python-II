# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []

    def travel(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that directoin.")

    # * Add `get [ITEM_NAME]` and `drop [ITEM_NAME]` commands to the parser
    def get_item(self, item):
        room_items = self.current_room.items
        for item in room_items:
            if item.name == item:
                self.inventory.append(item)
                room_items.remove(item)
                item.take()
                return None
        print(f'\nItem: {item} is not in {self.curren_room.name}\n')

    def drop_item(self, item):
        inventory = self.inventory
        return [i for i in inventory if i != item]
