#!/usr/bin/python3
def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None

    # Initialize the biggest number with the first element
    biggest = my_list[0]

    # Iterate through the list starting from the second element
    for num in my_list:
        if num > biggest:
            biggest = num

return biggest
