#!/usr/bin/python3
"""

function prints a text with 2 new lines after each of \
these characters: ., ? and :
"""


def text_indentation(text):
    """
    Args:
        text (str): the text to be checked and
    """
    if not type(text) is str:
        raise TypeError("text must be a string")
    text = text.replace('? ', "?\n\n").\
        replace(':', ":\n\n").replace('.', ".\n\n")
    seperated = text.splitlines(True)
    final_text = ""
    for i in seperated:
        final_text += i.strip(' ')
    print(final_text, end="")
