#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

     q = 0
    while q < len(text) and text[q] == ' ':
         q += 1
         

    while q < len(text):
        print(text[q], end="")
        if text[q] == "\n" or text [q] in ".?:":
            if text[q] in ".?:":
                print("\n")
            q += 1
            while c < len(text) and text[q] == ' ':
                q =+ 1
            continue
        q += 1
