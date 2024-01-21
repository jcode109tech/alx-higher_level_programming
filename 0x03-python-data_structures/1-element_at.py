#!/usr/bin/python3

def element_at(my_list, idx):
    # check if the index is greater than or equal to the number of elements
    if idx < 0 or idx >= len(my_list):
        return None
    
    return my_list[idx]



