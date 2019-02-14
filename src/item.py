# This will be the base class for specialized item types
# to be declared later.


class Item():
    def __init__(self, name, description):
        self.name = name  # should be one word
        self.description = description

    def examine(self):
        print(f'\n\nIt is {self.description}.\n\n')

    def onTake(self):
        print(f'\n\n{self.name.upper()} was added to your inventory.\n\n')

    def onDrop(self):
        print(f'\n\n{self.name.upper()} was dropped.\n\n')
