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
        for i in room_items:
            if item == i.name:
                self.inventory.append(i)
                room_items.remove(i)
                i.take()
                return None
        print(f'\n{item} is not in {self.current_room.title}\n')

    def drop_item(self, item):
        room_items = self.current_room.items
        for i in self.inventory:
            if i.name == item:
                self.inventory.remove(i)
                room_items.append(i)
                i.discard()
                return None
        print(f'\n{item} is not in {self.current_room.title}\n')
