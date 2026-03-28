#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create an empty list to store the True/False results
    result_list = []

    for num in my_list:
        if num % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)

    return result_list
