"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       Minh Tran
Email:      minh.s.tran@tuni.fi
Student Id: 050359358

Implement a program capable of printing energy consumption
histograms based on the data the user entered.
"""


def main():
    # Print the instructions
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()

    # Retrieve data from the user
    input_data = get_input()

    # Run the program. The possibility of having no input must be checked.
    if len(input_data) != 0:
        print_histogram(input_data)
    else:
        print("Nothing to print. Done.")


def get_input():
    """
    This function takes the user's energy consumption data and returns the data
    as a list.
    """
    input_data = []

    # A while loop to let the user continuously enter the energy consumption.
    # Exit the loop when the input is a blank line
    while True:
        energy_consumption_str = input("Enter energy consumption (kWh): ")
        if energy_consumption_str == "":
            break
        else:
            energy_consumption = int(energy_consumption_str)
            if energy_consumption < 0:
                print(f"You entered: {energy_consumption}. Enter non-negative numbers only!")
            else:
                input_data.append(energy_consumption)
    return input_data


def class_minimum_value(class_number):
    """
    This function determines the minimum value of the class.

    :param class_number: int,
        Expresses which consumption class (1, 2, 3, ...) should the minimum
        value be calculated.
    """

    smallest_value = 10 ** class_number // 100 * 10
    return smallest_value


def class_maximum_value(class_number):
    """
    This function determines the minimum value of the class.

    :param class_number: int,
        Expresses which consumption class (1, 2, 3, ...) should the maximum
        value be calculated.
    """

    largest_value = 10 ** class_number - 1
    return largest_value


def categorize(input_data):
    """
    This function categorize the input data.

    :param input_data: list,
        The numbers which the users entered.
    """

    # Create a double-ended list to store the categorised data. Each class
    # is a list contained by an outer list. The indexes indicate the length of
    # the numbers: length = index + 1 (as the index starts from 0).
    category_list = [[] for i in range(len(str(max(input_data))))]

    # Categorise the data using the length of the numbers.
    for data in input_data:
        category_list[len(str(data))-1].append(data)
    return category_list


def print_histogram(input_data):
    """
    This function prints the complete histogram

    :param input_data: list,
        The numbers which the users entered.
    """

    # To print the whole histogram, print each line of the histogram according
    # to each group.
    category_list = categorize(input_data)
    for i in range(len(category_list)):
        print_single_histogram_line(i+1, len(category_list[i]), len(str(max(input_data))))


def print_single_histogram_line(class_number, count, largest_class_number):
    """
    This function prints one correctly indented line of the histogram.

    :param class_number: int,
        Expresses which consumption class (1, 2, 3, ...)
        should the histogram line be printed for. The <class_number> is used
        to decide which value range (0-9, 10-99, 100-999, ...) should be
        printed in front of the histogram markers ("*").

    :param count: int,
        How many of the values entered by the user belong to <class_number>.

    :param largest_class_number: int,
        What is the largest class out of all input values
        the user entered. This is needed when deciding the indentations
        for all other histogram lines.  For example, if the largest
        number the user entered was 91827364 (8 digits) the value
        of this parameter should be 8.
    """

    # <range_string> represents the range of the values the line's
    # histogram will represent in the printout.  For example "1000-9999".

    min_value = class_minimum_value(class_number)
    max_value = class_maximum_value(class_number)
    range_string = f"{min_value}-{max_value}"

    # This value defines the print width for all the other <range_string>'s.

    largest_width = 2 * largest_class_number + 1

    # Now all the preparations have been done and we can print the
    # histogram line with the correct number of whitespaces in the
    # beginning of the line followed by the correct number of '*'
    # characters. ">" character in the following f-string places
    # <range_string>'s value to the right edge of the output field
    # (filler white spaces will be printed in the beginning).

    print(f"{range_string:>{largest_width}}: {'*' * count}")


if __name__ == "__main__":
    main()
