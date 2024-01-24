#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # Check if the key exists in the dictionary
    # if key in a_dictionary:
    #     # Key exists, replace the value
    #     a_dictionary[key] = value

    a_dictionary.update({key: value})

    return (a_dictionary.copy())
