#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program converts celsius into fahrenheit


def area_of_triangle(base_int, height_int):

    # process
    area = (base_int * height_int) / 2

    # output
    print("\nYour triangle's area is {0} cm".format(area))


def main():
    # this function calls other functions as well as
    #   takes input

    # input
    base = input("Please input the base (cm): ")
    height = input("Please input the height (cm): ")

    try:
        base_int = int(base)
        height_int = int(height)

    except Exception:
        print("\nYou have entered an invalid input.")

    finally:
        # call fucntions
        area_of_triangle(base_int, height_int)


if __name__ == "__main__":
    main()
