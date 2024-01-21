#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Handle if list is empty
    if not my_list:
        return None
    
    # Handles index range of a list 
    if idx < 0 and idx >= (len(my_list)-1):
        return my_list
    
    # Makes a new copy of list
    new_list = my_list[:]
    new_list[idx] = element

    return new_list