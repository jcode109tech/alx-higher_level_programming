#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Checks if list is empty
    if not my_list:
        return None
    
    bool_str = []
    # loops a list an find multiples of 2 
    for div in my_list:
        if div % 2 == 0:
            bool_str.append(True)
        else:
            bool_str.append(False)
        
    return bool_str
