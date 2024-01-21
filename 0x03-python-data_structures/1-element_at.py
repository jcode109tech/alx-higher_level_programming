#!/usr/bin/python3

def element_at(my_list, idx):
    # Return an element at a specifc index
    if idx < 0 and idx > (len(my_list) - 1):
        return None
    
    return my_list[idx]


