#!/usr/bin/python3


"""
    A function that prints a text 
    with 2 new lines after each of these characters: ., ? and :
"""

def text_indentation(text):
    """  
    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """

    if not isinstance(text, (str)):
        raise TypeError("text must be string")


    for char in text:
        print(char, end="")

        if char in ('.', '?', ':'):
            print("\n\n", end="")
    

    # # Split the text using '.' or '?' or ':'
    # sentences = []
    # for delimiter in ('.', '?', ':'):
    #     sentences.extend(text.split(delimiter))

    # # Iterate through the sentences and print them with two new lines
    # for sentence in sentences:
    #     print(sentence.strip())  # Strip any leading or trailing whitespace
    #     print("\n")  # Two new lines
