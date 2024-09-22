import datetime

""" TODO: Multiline Comment
     Create a Function that take 2 Input From User. First User name and Second User age. Then Find the User Date-Of-Birth Year.
"""


def user():
    """ Function take input from user and return user Date-Of-Birth. """
    user_name = str(input("Enter Username: "))
    user_age = int(input("Enter user age: "))
    # Operations.
    x = datetime.datetime.now().year
    a = x - user_age
    return a


# TODO: Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("User Date-Of-Birth", user())
