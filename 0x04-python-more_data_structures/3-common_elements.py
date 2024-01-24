#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Use a set comprehension to find common elements
    set_comm = {i for i in set_1 if i in set_2}

    return set_comm
