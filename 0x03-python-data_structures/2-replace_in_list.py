#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Modifies a list a specific index
    if idx < 0 or idx >= len(my_list):
        return my_list
    # changes index value
    my_list[idx] = element
    # returns new list
    return my_list
