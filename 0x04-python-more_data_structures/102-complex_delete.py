#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    if a_dictionary is not None and type(a_dictionary) is dict:

        item_delete = {key: val for (key, val) in a_dictionary.items()
                       if value == val}

        for (key, val) in item_delete.items():
            del a_dictionary[key]

        return a_dictionary.copy()
