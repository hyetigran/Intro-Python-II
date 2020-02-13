# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = None

    def __str__(self):
        return f"{self.title}\n\n{self.description}"

    # Call this method when user 'drops item'
    def dropped(self, item):
        return room.items.append(item)

        # Call this method when user 'drops item'
    def taken(self, item):
        items = room.items
        return [i for i in items if i != item]
