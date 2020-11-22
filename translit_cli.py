"""
Command line transliteration
"""
import os
import re
import sys
from tkinter import Tk

import translit as trn


def prepare_name(name):
    """Make full name short. and clear all nonsense"""
    split_name = name.strip().lower().split()
    split_name = clear_non_alphabetic_chars(split_name)
    full_name_len = len(split_name)

    for i in range(1, full_name_len):
        split_name[i] = split_name[i][0]
    return split_name


def clear_non_alphabetic_chars(name_list):
    """Remove all non alphabetic characters"""
    new_name_list = []
    for val in name_list:
        val = re.sub(r'\W+', '', val)
        if val.isalpha():
            new_name_list.append(val)
    return new_name_list


def do_translit(split_name):
    """Do the transliteration for each name"""
    translit_name = []
    for name in split_name:
        translit_name.append(trn.translit(name))
    return translit_name


def do_dots(split_name):
    """Add dots to all letter in list from the second one"""
    name_len = len(split_name)
    for i in range(1, name_len):
        split_name[i] = split_name[i] + "."
    return split_name


def join_name(split_name):
    """Make a full name as a string"""
    # Add space to last name
    split_name[0] = split_name[0] + " "
    name = "".join(split_name)
    return name


def capitalize_name(name):
    """Returns capitalized name"""
    return name.title()


def start(original_name):
    """It is the main running procedure"""
    split_name = prepare_name(original_name)
    split_name = do_translit(split_name)
    split_name = do_dots(split_name)
    name = join_name(split_name)
    name = capitalize_name(name)
    return name


def get_clipboard():
    root = Tk()
    # keep the window from showing
    root.withdraw()
    try:
        clipboard = root.clipboard_get()
    except:
        sys.exit("Something wrong with clipboard. Program aborted.")
    root.destroy()
    return clipboard


def set_clipboard(text):
    # Set clipboard
    # is this a workaround solution? It works though.
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


# Gather our code in a main() function
def main():
    """ The MAIN function """

    # if no argument is given use clipboard
    if len(sys.argv) == 1:
        # get the clipboard
        original_name = get_clipboard()

        # Debug mode. Print input value
        print("Original name: " + str(original_name))

        # Do the business
        result = start(original_name)

        set_clipboard(result)

        # output the result
        print("Translit name: " + result)
    else:
        # If any arguments is given use sys.arg's
        pass
        # set clipboard to translated name
        # pyperclip.copy(translit_name)


# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()
