import os
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'cave':  Room("Cave Entrance",
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

room['cave'].n_to = room['foyer']
room['foyer'].s_to = room['cave']
room['foyer'].n_to = room['grand']
room['foyer'].e_to = room['narrow']
room['grand'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'cave' room.
# Ask for their name.

user = Player(input("What's your name? "), 'cave')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while True:
    room_sc = room[user.location]  # _sc here means shortcut
    room_name = room_sc.name
    room_desc = room_sc.description
    items = [item.name for item in room_sc.items if len(room_sc.items) > 0]
    inventory = [item.name for item in user.inventory if len(
        user.inventory) > 0]

    print(f'''You are at the {room_name}: '{room_desc}.'

Please pick a direction to go in: n(orth), e(ast), s(outh), w(est)''')
    action = input('Enter your action: ')
    os.system('cls' if os.name == 'nt' else 'clear')

    if len(action.split(' ', 1)) == 2:
        # do something here
        verb = action.split(' ', 1)[0].lower()
        subject = action.split(' ', 1)[1].lower()
        if verb == 'search':
            print(
                f'\n\nYou found the following items in the room: {items}\n\n')
        elif verb == 'examine' or verb == 'inspect':
            if subject in inventory:
                user.inventory[inventory.index(subject)].examine()
            elif subject in items:
                room_sc.items[items.index(subject)].examine()
            else:
                print('\n\nThat item is not in your pack or the room.\n\n')
        elif verb == 'take' or verb == 'get':
            if subject in items:
                item = room_sc.items.pop(items.index(subject))
                user.inventory.append(item)
                item.onTake()
            else:
                print('\n\nThat item is not in this room.\n\n')

        elif verb == 'drop':
            if subject in inventory:
                item = user.inventory.pop(inventory.index(subject))
                room_sc.items.append(item)
                item.onDrop()
            else:
                print('\n\nThat item is not in your inventory.\n\n')
    else:
        action = action[0].lower()

        # enable the user to input 'q', 'Q', 'quit' to quit the game
        if action == 'q':
            break

        elif action == 'i':
            print(f'\n\nYour inventory contains: {inventory}\n\n')

        # If the user enters a cardinal direction, attempt to move there.
        elif action == 'n' or action == 'e' or action == 's' or action == 'w':
            if hasattr(room[user.location], f'{action}_to'):
                if action == 'n':
                    user.location = room_sc.n_to.name.split(' ', 1)[
                        0].lower()
                elif action == 'e':
                    user.location = room_sc.e_to.name.split(' ', 1)[
                        0].lower()
                elif action == 's':
                    user.location = room_sc.s_to.name.split(' ', 1)[
                        0].lower()
                elif action == 'w':
                    user.location = room_sc.w_to.name.split(' ', 1)[
                        0].lower()
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
