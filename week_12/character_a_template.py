"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""

class Character:
    # TODO: the class implementation goes here.
    def __init__(self, name):
        """
        Create a class for the character using the character's name.

        :param name: str,
            The name of the character
        """
        self.__name = name
        self.__item_dict = {}

    def give_item(self, item):
        """
        Give an item to the character.

        :param item: str,
            The item given to the character
        """
        if item not in self.__item_dict:
            self.__item_dict[item] = 1
        else:
            self.__item_dict[item] += 1

    def remove_item(self, item):
        """
        Remove an item from the character.

        :param item: str,
            The item to be removed from the character
        """
        self.__item_dict[item] -= 1

    def printout(self):
        """
        Print the information of the character
        """
        print(f"Name: {self.__name}")
        if self.__item_dict == {}:
            print("  --nothing--")
        else:
            for item in sorted(self.__item_dict):
                if self.has_item(item):
                    print(f"  {self.__item_dict[item]} {item}")

    def get_name(self):
        """
        Return the name of the character
        """
        return self.__name

    def has_item(self, item):
        """
        Check if the character has a particular item

        :param item: str,
            The item to be checked
        :return True if the character has the item
        :return False if the character doesn't have the item
        """
        if item not in self.__item_dict or self.__item_dict[item] == 0:
            return False
        else:
            return True

    def how_many(self, item):
        """
        Return the number of the particular item the character has
        """
        if self.has_item(item):
            return self.__item_dict[item]
        else:
            return 0


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
