import datetime

""" TODO: Multiline Comment
     Create a Function that take a Input From User. First User name and Second User age. Then Find the User Date-Of-Birth Year.
"""


def user():
    """ Function take input from user and return user Date-Of-Birth. """
    user_age = int(input("Enter user age: "))
    x = datetime.datetime.now().year
    a = x - user_age
    return a


""" TODO: Multiline Comment
     Print The Sum. Current Number and The Previous Number.
"""


def addition(num1: int):
    """ Function take input as a parameter and return the sum Of Current number and the Previous number. """
    current_number = num1
    previous_number = current_number - 1
    a = current_number + previous_number
    return a


""" TODO: Multiline Comment
     Print all character in a String that present an even index number.
"""


def character_print():
    """ Function take input from user and print the even index character one by one. """
    user_string = str(input("Enter a String: "))
    for element in range(len(user_string)):
        if element % 2 == 0:
            print(user_string[element + 1])


# TODO: Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
    # print("User Date-Of-Birth IN Year: ", user())
    # print(F"Print The Sum: {addition(10)}")
    # character_print()
