"""
COMP.CS.100 Programming 1
Tran Sy Minh, minh.s.tran@tuni.fi, student id 050359358
6.16. Implement a program that formats text in a fully justified typesetting.
"""


def input_text():
    """
    Let the user enter the text.

    :return input_list :list,
        The text entered by the user contains in a list, and each element of
        the list is a word of the text.
    """

    print("Enter text rows. Quit by entering an empty row.")
    input_list = []
    exit_input = False

    # Let the user enter each line of the text.
    while not exit_input:
        input_row = input()
        if input_row == "":
            exit_input = True
        else:
            for word in input_row.split(" "):
                if word != "":
                    input_list.append(word)

    return input_list


def divide_text(input_list, num_of_chars):
    """
    Divide the text into smaller segments

    :param input_list: list,
        List of words in the text.

    :param num_of_chars: int,
        The number of characters in one row.

    :return divided_text: list,
        The text, formatted in double-ended list, with each list element as a
        row of the text.
    """

    divided_text = []
    row = []
    chars_in_words = 0

    # To determine the words in each row, the number of characters in words
    # must be enough in order that spacings are available between the words,
    # which means the characters for spaces must be more than the number of
    # gaps between words.
    for word in input_list:
        row.append(word)
        chars_in_words += len(word)

        # Checking the condition mention above. If the row is full, a new list
        # for the next row is created.
        if (num_of_chars - chars_in_words < (len(row)-1)) or \
                (chars_in_words + (len(row) - 1) > num_of_chars):
            not_suitable_word = row.pop()
            divided_text.append(row.copy())
            row = [not_suitable_word]
            chars_in_words = len(not_suitable_word)

    # Check if the last row has been added to the list as it might haven't
    # satisfied the condition of a full row yet.
    if len(row) >= 1:
        divided_text.append(row)

    return divided_text


def print_text(divided_text, num_of_chars):
    """
    Print the text which have been segmented by divide_text before.

    :param divided_text: list,
        Segmented word list returned by divide_text.

    :param num_of_chars: int,
        The number of characters in one row.
    """

    # Take the last row out as it is different from the others.
    last = divided_text.pop()

    # Loop through the rows and print them
    for row in divided_text:
        if len(row) == 1:
            print(row[0])
        else:
            chars_in_words = 0

            for word in row:
                chars_in_words += len(word)
            spacing_characters = num_of_chars - chars_in_words
            # Using division to find the shortest length of the spacings.
            # The shorter length can be obtained by dividing the number of
            # characters for spacings by the number of spacings.
            shorter = spacing_characters // (len(row)-1)
            # Using modulo to calculate the number of the longer spacings.
            longer_spacing = spacing_characters % (len(row)-1)

            # Print the row using the 2 types of spacing.
            for i in range(longer_spacing):
                print(row[i], end=" "*(shorter+1))
            for i in range(longer_spacing, len(row)-1):
                print(row[i], end=" "*shorter)
            print(row[len(row)-1])

    # Print the last row (without "extra" spaces)
    last_string = ""
    for word in last:
        last_string += word + " "
    print(last_string[:(len(last_string)-1)])


def main():

    # Retrieve word list and number of characters from the user
    input_list = input_text()
    num_of_chars = int(input("Enter the number of characters per line: "))
    divided_text = divide_text(input_list, num_of_chars)
    print_text(divided_text, num_of_chars)


if __name__ == "__main__":
    main()
