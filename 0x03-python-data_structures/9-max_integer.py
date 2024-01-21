#!/usr/bin/python3
            
def max_integer(my_list=[]):
    # checks if string is empty
    if not my_list:
        return None
    
    # varialbe storage for max value
    max_value = my_list[0]

    # Tranverse thorugh a list to find largest value
    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value


