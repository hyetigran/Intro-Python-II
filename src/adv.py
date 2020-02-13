from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all items
item = {
    "coin": Item("coin", 0, 0),
    "sword": Item("sword", 10, 0),
    "shield": Item("shield", 5, 5),
    "helm": Item("helm", 0, 10),
}

# Link items to room
room['foyer'].items = [item["coin"]]
room['overlook'].items = [item["sword"]]
room['narrow'].items = [item["shield"]]
room['treasure'].items = [item["helm"]]

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player(input("Enter your name: \n"), room["outside"])

print(f'Hello, {player.name}.')

print(player.current_room)
while True:

    cmd = input("-> ").lower()
    if cmd in ["n", "s", "e", "w"]:
        player.travel(cmd)
    elif cmd == 't':
        # print([item for item in room.items])
        # for item in room.items:
        #     print(f'Item: {item.name}')
        # player.get_item()
        print(*(item for item in room.items))
    elif cmd == "q":
        print("Goodbye!")
        exit()
    else:
        print("I did not understand that command.")
