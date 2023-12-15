
"""
# Python project : My first chatBot.

# pythonProject-pychatbot-DONNAT-LEMONT-int1
# Teammates : DONNAT Arthur, LEMONT Mathis ; On (Discord and) Github.


# role of this file :
# data.py : functions for process the date / .txt files.
"""

import os


def list_of_files(directory, extension):
    """role : ,
    In, parameters : ,
    Out, returned result : ."""
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


files = list_of_files('speeches/', '.txt')


def get_president_name(file):
    """role : ,
    In, parameters : ,
    Out, returned result : ."""
    name = file[11:-4]

    if '0' <= name[-1] <= '9':
        name = name[:-1]

    return name


president_surname = { 'Chirac': "Jacques", "Giscard d'Estaing": "Valérie", 'Hollande': "François", "Macron": "Emmanuel", "Mitterand": "François", "Sarkozy": "Nicolas" }


def get_president_surname(name):
    """role : ,
    In, parameters : ,
    Out, returned result : ."""
    return president_surname[name]


def print_president_list():
    """role : ,
    In, parameters : ,
    Out, returned result : ."""
    last = ""
    for i in files:
        txt = get_president_name(i)
        if txt != last:
            print(txt)
            last = txt


def lowercase_to_uppercase(string):
    """role : change lowercase of a string into uppercase,
    In, parameters : a string,
    Out, returned result : the new modified string."""
    new_string = ""
    for character in string:
        if 'a' <= character <= 'z':
            new_string += chr(ord(character)-32)
        else:
            new_string += character
    return new_string


def uppercase_to_lowercase(string):
    """role : change uppercase of a string into lowercase,
    In, parameters : a string,
    Out, returned result : the new modified string."""
    new_string = ""
    for character in string:
        if 'A' <= character <= 'Z':
            new_string += chr(ord(character) + 32)
        else:
            new_string += character
    return new_string


def is_letter(character):
    """role : verify if a character is a letter or not,
    In, parameters : a character,
    Out, returned result : a boolean"""
    if ('A' <= character <= 'Z') or ('a' <= character <= 'z'):
        return True
    else:
        return False


def cleaned_file():
    """role : ,
    In, parameters : ,
    Out, returned result : ."""
    for i in files:
        f = open(f"speeches/{i}", 'r', encoding='utf-8')
        lower = f.read().lower()

        writed = open(f"cleaned/{i}", 'w', encoding='utf-8')
        encoded = lower.encode('ascii', 'ignore')
        writed.write(encoded.decode())