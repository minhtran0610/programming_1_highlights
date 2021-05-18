"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Project: accesscontrol, program template
"""

DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}

class Accesscard:
    """
    This class models an access card which can be used to check
    whether a card should open a particular door or not.
    """

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.

        :param id: str, card holders personal id
        :param name: str, card holders name

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME OR THE
        PARAMETERS!
        """

        self.__id = id
        self.__name = name
        self.__access_codes = []

    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        for example:
        777, Thelma Teacher, access: OPET, TE113, TIE
        Note that the space characters after the commas and semicolon need to
        be as specified in the task description or the test fails.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE PRINTOUT FORMAT!
        """

        print(f"{self.__id}, {self.__name}, access: {self.create_access_string()}")

    def create_access_string(self):
        """
        Create a string of access codes that the cardholder has

        :return access_str: str,
            The access codes string
        """
        access_str = ""
        for code in sorted(self.__access_codes):
            access_str += (code + ", ")

        access_str = access_str[:-2]
        return access_str

    def get_name(self):
        """
        :return: Returns the name of the accesscard holder.
        """

        return self.__name

    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.

        :param new_access_code: str, the accesscode to be added in the card.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """
        # The adding can only be done if the access code is not in the card yet
        if not self.new_code_already_available(new_access_code):
            if new_access_code in DOORCODES:
                # If the new access code is a door code, check if that code is
                # unnecessary (when there's already an area code that gives
                # access to that door)
                if not self.new_door_code_unnecessary(new_access_code):
                    self.__access_codes.append(new_access_code)
            else:
                # If the new access code is an area code, delete all the door
                # code that this area code gives access to.
                self.existing_door_code_unnecessary(new_access_code)
                self.__access_codes.append(new_access_code)
        else:
            pass

    def new_code_already_available(self, new_code):
        """
        Check if a code is already in the card

        :param new_code: str,
            The new code which is to be added
        :return True if the code is already in the card
        """
        for code in self.__access_codes:
            if code == new_code:
                return True

        return False

    def new_door_code_unnecessary(self, new_door_code):
        """
        Check if a door code that is going to be added is unnecessary

        :param new_door_code: str,
            The door code which is going to be added
        :return True if the new door code is unnecessary
        :return False if the new door code is not
        """
        # The door code will become unnecessary if the card already has an area
        # code granted access to this room
        for code in self.__access_codes:
            if code in DOORCODES[new_door_code]:
                return True

        return False

    def existing_door_code_unnecessary(self, new_area_code):
        """
        Check if existing door codes becomes unnecessary because of new
        door code and remove them.

        :param new_area_code:
            The area code that is to be added
        """
        # When a new area code is added, there's a chance that some door codes
        # will become unnecessary. This method removes them from the card
        for code in self.__access_codes:
            if code in DOORCODES:
                if new_area_code in DOORCODES[code]:
                    self.__access_codes.remove(code)

    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: str, the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        # Check if the card has the door code or an area code that grants
        # access to this door
        if door in self.__access_codes:
            return True
        else:
            for code in self.__access_codes:
                if code in DOORCODES[door]:
                    return True

        return False

    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: Accesscard, the accesscard whose access rights are added to this card.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        # Merge the access of one card to another by adding each of this card's
        # access codes
        for code in card.__access_codes:
            self.add_access(code)


# TODO: Implement helper functions here.

def read_input_file(file_name):
    """
    Read the input file, create the Accesscards object and return a dictionary
    contains all the objects

    :param file_name: str,
        The name of the input file
    :return access_cards_dict:
        The dictionary that contains all the access cards.
    """

    access_cards_dict = {}

    # Open the file
    try:
        f = open(file_name, mode='r')

        # In each row, extract the information, create the Accesscard objects
        # and add them to the dict, with the key is the ID of the card and the
        # value is the Accesscard objects
        for row in f:
            id, name, access_codes_string = row.rstrip().split(";")
            access_card = Accesscard(id, name)
            access_cards_dict[id] = access_card

            for code in access_codes_string.split(','):
                access_card.add_access(code)

        return access_cards_dict

    # If any error occurs, print the error message
    except OSError:
        print("Error: file cannot be read.")


def check_valid_id(id, database):
    """
    Check if the ID of the card is valid

    :param id: str,
        The ID of the access card
    :param database: dict,
        The access cards database
    :return True if the ID is valid
    """
    if id in database:
        return True

    return False


def check_valid_door_code(door_code, database):
    """
    Check if a door code is a valid door code
    
    :param door_code: str,
        The door code to be checked
    :param database: dict,
        The access code database
    :return True if the door code is valid
    """
    if door_code in database:
        return True
    
    return False


def check_valid_access_code(access_code, database):
    """
    Check if an access code is valid
    
    :param access_code: str,
        The access code to be checked
    :param database: str,
        The access code database
    :return True if the access code is valid
    """
    # Check if the code is a valid door code
    if access_code in database:
        return True
    # Check if the code is a valid area code
    else:
        for code in database:
            if access_code in database[code]:
                return True
    
    return False


def main():
    # TODO: Implement the reading of the inputfile and
    # storing the information into a data structure.
    access_card_dict = read_input_file('accessinfo.txt')

    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:
            # Loop through the dict in sorted order and print the information
            # of the card using method .info()
            for id in sorted(access_card_dict):
                access_card_dict[id].info()

        elif command == "info" and len(strings) == 2:
            card_id = strings[1]
            # Check if the card id is valid
            if check_valid_id(card_id, access_card_dict):
                access_card_dict[card_id].info()
            else:
                print("Error: unknown id.")

        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]
            # Check if the card ID is valid. If not, print the error message
            if check_valid_id(card_id, access_card_dict):
                # Check if the door code is valid. If not, print the error
                # message
                if check_valid_door_code(door_id, DOORCODES):
                    # Check the accessibility of the card. Print the
                    # corresponding message
                    if access_card_dict[card_id].check_access(door_id):
                        print(f"Card {card_id} ( {access_card_dict[card_id].get_name()} ) has access to door {door_id}")
                    else:
                        print(f"Card {card_id} ( {access_card_dict[card_id].get_name()} ) has no access to door {door_id}")
                else:
                    print("Error: unknown doorcode.")
            else:
                print("Error: unknown id.")

        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]
            # Check if the ID is valid. If not, print the error message
            if check_valid_id(card_id, access_card_dict):
                # Check if the access code is valid. If not, print the error
                # message. If the code is valid, add it to the card
                if check_valid_access_code(access_code, DOORCODES):
                    access_card_dict[card_id].add_access(access_code)
                else:
                    print("Error: unknown accesscode.")
            else:
                print("Error: unknown id.")

        elif command == "merge" and len(strings) == 3:
            card_id_to = strings[1]
            card_id_from = strings[2]
            # Check if the IDs are valid. If not, print the error message
            if check_valid_id(card_id_from, access_card_dict) or check_valid_id(card_id_to, access_card_dict):
                # Merge the access codes of the 2 cards
                access_card_dict[card_id_to].merge(access_card_dict[card_id_from])
            else:
                print("Error: unknown id.")

        elif command == "quit":
            print("Bye!")
            return

        else:
            print("Error: unknown command.")


if __name__ == "__main__":
    main()
