import os
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item('moss', 'a clump of moss')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [Item('rope', 'a length of rope')]),

    'grand': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                  [Item('egg', 'a peculiar looking egg')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [Item('gold coin', 'a single gold coin')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [Item('torch', 'a burnt out torch')]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['grand']
room['foyer'].e_to = room['narrow']
room['grand'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

user = Player(input("What's your name? "), 'outside')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while True:
    room_name = room[user.location].name
    room_desc = room[user.location].description
    items = []
    for item in room[user.location].items:
        str = f'{item.name}'
        items.append(str)

    print(f'''You are at the {room_name}: '{room_desc}.'

The following items are in the room: {items}

Please pick a direction to go in: n(orth), e(ast), s(outh), w(est)''')
    userInput = input('Enter your action: ')[0].lower()
    os.system('cls' if os.name == 'nt' else 'clear')

    if userInput == 'q':
        break

# If the user enters a cardinal direction, attempt to move to the room there.
    elif userInput == 'n' or 'e' or 's' or 'w':
        if hasattr(room[user.location], f'{userInput}_to'):
            if userInput == 'n':
                user.location = room[user.location].n_to.name.split(' ', 1)[
                    0].lower()
            elif userInput == 'e':
                user.location = room[user.location].e_to.name.split(' ', 1)[
                    0].lower()
            elif userInput == 's':
                user.location = room[user.location].s_to.name.split(' ', 1)[
                    0].lower()
            elif userInput == 'w':
                user.location = room[user.location].w_to.name.split(' ', 1)[
                    0].lower()
            elif userInput == 'q':
                break
        else:
            print('''
-----------------------
| You shall not pass! |
-----------------------
            ''')

# Print an error message if the movement isn't allowed.
    else:
        print('''
-------------------------------------
| ERROR: invalid action. Try again! |
-------------------------------------
        ''')
