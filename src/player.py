# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, item):
        self.name = name
        self.current_room = current_room
        self.items = [item]

    def travel(self, direction):
        next_room = getattr(current_room, f"{direction}_to")
        if next_room is not None:
            player.current_room = next_room
        else:
            print("You cannot move in that directoin.")

    # * Add `get [ITEM_NAME]` and `drop [ITEM_NAME]` commands to the parser
    def get_item(self, item):
        return player.item.append(item)

    def drop_item(self, item):
        items = player.items
        return [i for i in items if i != item]
