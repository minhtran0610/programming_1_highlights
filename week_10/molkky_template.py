"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""


# TODO:
# a) Implement the class Player here.

class Player:
    def __init__(self, name):
        """
        Create a Player object.

        :param name: str,
            the name of the person whom the object is representing.
        """

        self.__name = name
        self.__points = 0
        self.__scorelist = []

    def get_name(self):
        """
        Get the name of the person.
        """

        return self.__name

    def get_points(self):
        """
        Get the point of the person.
        """

        return self.__points

    def has_won(self):
        """
        Check if the player has won the match.
        """
        if self.__points == 50:
            return True
        else:
            return False

    def calculate_average(self):
        """
        Return the average point of the previous turns of the player
        """

        return sum(self.__scorelist)/len(self.__scorelist)

    def add_points(self, points):
        """
        Add the points for the player according to how much he/she gets in a
        turn

        :param points: int, the points the player gets in the turn
        """

        self.__scorelist.append(points)
        self.__points += points
        if self.__points > 50:
            self.__points = 25
            print(f"{self.__name} gets penalty points!")
        elif 40 <= self.__points <= 49:
            print(f"{self.__name} needs only {50-self.__points} points. It's better to avoid knocking down the pins with higher points.")

    def calculate_percentage(self):
        """
        Calculate the hit percentage of the player
        """
        if len(self.__scorelist) == 0:
            return 0
        else:
            hit = 0
            for point in self.__scorelist:
                if point > 0:
                    hit += 1
            return hit/len(self.__scorelist) * 100


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.
        if pts > in_turn.calculate_average():
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p,", f"hit percentage {player1.calculate_percentage():.1f}")
        print(player2.get_name() + ":", player2.get_points(), "p,", f"hit percentage {player2.calculate_percentage():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
