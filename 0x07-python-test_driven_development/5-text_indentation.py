#!usr/bin/python3
"""
Contains one module
"""


def text_indentation(text):
    """
    Prints a text with two new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    delimiters = ['.', '?', ':']
    length = len(text)

    output = []
    for i in range(length):
        output.append(text[i])
        if text[i] in delimiters:
            output.append("\n")
            print(''.join(output).lstrip())
            output = []
    print(''.join(output).lstrip())
