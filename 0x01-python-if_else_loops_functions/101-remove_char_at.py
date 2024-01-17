#!/usr/bin/python3
def remove_char_at(input_str, n):
    # Check if n is a valid index within the string
    if 0 <= n < len(input_str):
        # Using string slicing to remove the character at position n
        return input_str[:n] + input_str[n+1:]
    else:
        # If n is out of range, return the original string
        return input_str
