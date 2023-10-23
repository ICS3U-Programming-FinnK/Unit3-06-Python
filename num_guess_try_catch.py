#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: October 23rd, 2023
# this program checks if the number the user guessed is correct with the try case statement..
import random
random.randint(0,9)


def main():
    # user inputs the number between 0 to 9
    integer_as_string = input("enter an number between 0 to 9: ")
    print("")

    # terminal will process of there is a real number inputted, if not, it will give an error.
    # and the output will appear
    try:
        integer_as_number = int(integer_as_string)
        print("You entered a number correctly")
    except Exception:
        print("you did not type in a number")
    finally:
        print("thank you for trying out my program!")


if __name__ == "__main__":
    main()
