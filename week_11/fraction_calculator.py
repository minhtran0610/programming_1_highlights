"""
COMP.CS.100 Programming 1
Tran Sy Minh, minh.s.tran@tuni.fi, student id 050359358
11.10. Implement a fraction calculator that contains a simple command
line interpreter.
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        Simplify the fraction.
        """
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)
        numerator = self.__numerator // gcd
        denominator = self.__denominator // gcd

        return Fraction(numerator, denominator)

    def complement(self):
        """
        Calculate the complement of the fraction

        :returns: object, a new Fraction object for the complemented fraction.
        """
        return Fraction(0-self.__numerator, self.__denominator)

    def reciprocal(self):
        """
        Calculate the reciprocal of the fraction

        :returns: object, a new Fraction object for the reciprocated fraction.
        """
        return Fraction(self.__denominator, self.__numerator)

    def multiply(self, frac2):
        """
        Multiply the fraction with another fraction.

        :param frac2: Fraction object:
            The second fraction as a Fraction object
        :return: Fraction object, the result fraction as a Fraction object.
        """
        numerator = self.__numerator * frac2.__numerator
        denominator = self.__denominator * frac2.__denominator
        return Fraction(numerator, denominator)

    def divide(self, frac2):
        """
        Divide the fraction with another fraction.

        :param frac2: Fraction object:
            The second fraction as a Fraction object
        :return: Fraction object, the result fraction as a Fraction object.
        """
        return self.multiply(frac2.reciprocal())

    def add(self, frac2):
        """
        Add the fraction with another fraction.

        :param frac2: Fraction object:
            The second fraction as a Fraction object
        :return: Fraction object, the result fraction as a Fraction object.
        """
        numerator = self.__numerator * frac2.__denominator + self.__denominator * frac2.__numerator
        denominator = self.__denominator * frac2.__denominator
        return Fraction(numerator, denominator)

    def deduct(self, frac2):
        """
        Subtract the fraction with another fraction.

        :param frac2: Fraction object:
            The second fraction as a Fraction object
        :return: Fraction object, the result fraction as a Fraction object.
        """
        numerator = self.__numerator * frac2.__denominator - self.__denominator * frac2.__numerator
        denominator = self.__denominator * frac2.__denominator
        result = Fraction(numerator, denominator)
        return result

    def __float__(self):
        return self.__numerator/self.__denominator

    def __lt__(self, frac2):
        """
        Check if a fraction is less than another fraction

        :return True if self < frac2
        """
        return float(self.deduct(frac2)) < 0

    def __str__(self):
        """
        Return the string representation of the objective

        :return: str, the string representation of the object.
        """
        return f"{self.__numerator}/{self.__denominator}"


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def name_in_dict(name, dictionary):
    """
    Check if a name is in the dictionary

    :param name: str,
        The name to check
    :param dictionary:
        The targeted dictionary
    :return True if name is in dictionary
    """

    if name in dictionary.keys():
        return True
    else:
        return False


def command_line_interpreter():
    """
    Implement a command line interpreter, let the user enters the fractions

    :return fraction_dict: dict,
        Dict of fractions related to its name.
    """

    fraction_dict = {}

    stop = False
    while not stop:
        input_command = input("> ")

        # Quit command
        if input_command == "quit":
            print("Bye bye!")
            return

        # Add command
        elif input_command == "add":
            # Let the user input the fraction and the name
            fraction_str = input("Enter a fraction in the form integer/integer: ")
            fraction_name = input("Enter a name: ")
            # Add the fraction and its name into the dict
            (num_str, den_str) = fraction_str.split("/")
            fraction_dict[fraction_name] = Fraction(int(num_str), int(den_str))

        # Print command
        elif input_command == "print":
            # Let the user input the name
            fraction_name = input("Enter a name: ")
            # Print the fraction if the name of the fraction exists
            if name_in_dict(fraction_name, fraction_dict):
                print(f"{fraction_name} = {fraction_dict[fraction_name].__str__()}")
            else:
                print(f"Name {fraction_name} was not found")

        # List command
        elif input_command == "list":
            for fraction_name in sorted(fraction_dict):
                print(f"{fraction_name} = {fraction_dict[fraction_name].__str__()}")

        # * command
        elif input_command == "*":
            frac1_name = input("1st operand: ")
            # Check if name of operand 1 is in the dictionary.
            if not name_in_dict(frac1_name, fraction_dict):
                print(f"Name {frac1_name} was not found")
            else:
                # Check if name of operand 2 is in the dictionary
                frac2_name = input("2nd operand: ")
                if not name_in_dict(frac2_name, fraction_dict):
                    print(f"Name {frac2_name} was not found")
                else:
                    # Multiply the 2 operands
                    frac1 = fraction_dict[frac1_name]
                    frac2 = fraction_dict[frac2_name]
                    result = frac1.multiply(frac2)
                    print(f"{frac1.__str__()} * {frac2.__str__()} = {result.__str__()}")
                    print(f"simplified {result.simplify().__str__()}")

        # File command
        elif input_command == "file":
            file_name = input("Enter the name of the file: ")

            try:
                file = open(file_name, mode="r")

                # Loop through the rows and add the names and the fractions to
                # the dictionary
                for row in file:
                    [name_str, frac_str] = row.rstrip().split("=")
                    [nom_str, den_str] = frac_str.split("/")

                    fraction_dict[name_str] = Fraction(int(nom_str), int(den_str))

                file.close()

            except IOError:
                print("Error: the file cannot be read.")

            except ValueError:
                print("Error: the file cannot be read.")

        # Wrong commands
        else:
            print("Unknown command!")


def main():
    command_line_interpreter()


if __name__ == "__main__":
    main()




