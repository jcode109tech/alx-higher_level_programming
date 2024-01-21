#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Checks if list is empty
    if not my_list:
        return my_list
    
    # Handle out of bound index
    if idx < 0 and idx > len(my_list):
        return my_list 
    else:
        # deletes at a specific index
        del my_list[idx]
    
    return my_list