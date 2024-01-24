#!/usr/bin/python3

def best_score(a_dictionary):

    largest_value = 0
    largest_key = None

    if not a_dictionary:
        return
    else:
        for (key, value) in a_dictionary.items():
            if value > largest_value:
                largest_value = value
                largest_key = key

    return largest_key
