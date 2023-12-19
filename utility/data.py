
"""
# Python project : My first chatBot.

# pythonProject-pychatbot-DONNAT-LEMONT-int1
# Teammates : DONNAT Arthur, LEMONT Mathis ; On (Discord and) GitHub.


# role of this file :
# data.py : functions for process the date / .txt files.
"""

import os


def list_of_files(directory, extension):
    """role : get the files name in the directory and of the type extension choose ,
    In, parameters : a directory and an extension (like .txt) ,
    Out, returned result : list of files names."""
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def get_president_name(file):
    """role : get president names from the files name,
    In, parameters : list of files names,
    Out, returned result : . list of presidents names."""
    name = file[11:-4]

    if '0' <= name[-1] <= '9':
        name = name[:-1]

    return name


president_surname = {'Chirac': "Jacques", "Giscard d'Estaing": "Valérie", 'Hollande': "François", "Macron": "Emmanuel",
                     "Mitterand": "François", "Sarkozy": "Nicolas"}


def get_president_surname(name):
    """role : get president surname,
    In, parameters : a president name.,
    Out, returned result : the president surname."""
    return president_surname[name]


def print_president_list():
    """role : print the list of presidents names,
    In, parameters : none,
    Out, returned result : none. (because it's a print) """
    last = ""
    files_names = list_of_files("./speeches", "txt")
    for file_name in files_names:
        txt = get_president_name(file_name)
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


def remove_accents(string):
    """role : remove all accents of a string,
        In, parameters : a string,
        Out, returned result : the new modified string."""
    accents = {'ç': 'c', 'é': 'e', 'è': 'e', 'ê': 'e', 'à': 'a', 'â': 'a', 'ù': 'u', 'û': 'u', 'î': 'i', 'ï': 'i',
               'ô': 'o', 'ö': 'o', 'œ': 'oe', 'É': 'E', 'È': 'E', 'Ê': 'E', 'À': 'A', 'Â': 'A', 'Ù': 'U', 'Û': 'U',
               'Î': 'I', 'Ï': 'I', 'Ô': 'O', 'Ö': 'O', 'Œ': 'OE'}
    new_string = ""
    for character in string:
        if character in accents:
            new_string += accents[character]
        else:
            new_string += character
    return new_string


def remove_punctuations(string):
    """role : remove all punctuations of a string,
            In, parameters : a string,
            Out, returned result : the new modified string."""
    """For each file stored in the "cleaned" directory, run through its text
    and remove any punctuation characters. The final result should be a file with words
    separated by spaces. Please note that some characters, such as the apostrophe (')
    or the dash (-), requires special treatment to avoid concatenating two words
    (e.g. "elle-même" should become "elle même" and not "ellemême").
    Changes made at this phase should be stored in the same files in the "cleaned" directory"""
    new_string = ""
    for character in string:
        if character == "-" or character == "'":
            new_string += " "
        elif character == "." or character == "," or character == ";" or character == "!" or character == "?" or character == ":":
            new_string += ""
        else:
            new_string += character
    return new_string


def remove_mutlispaces(string):
    """role : Remove les espaces superflues.
        In, parameters : a string,
        Out, returned result : the new modified string."""
    new_string = ""
    precedent_character_was_a_space = False
    for character in string:
        if character == " " and precedent_character_was_a_space:
            new_string += ""
        elif character == " " and not precedent_character_was_a_space:
            new_string += character
            precedent_character_was_a_space = True
        else:
            precedent_character_was_a_space = False
            new_string += character
    return new_string


def cleaned_file(repertoire="./speeches/"):
    """role : Cette fonction nettoie les fichiers du répertoire repertoire (default : "./speeches/")
    et les écrit dans le répertoire cleaned.,
    In, parameters : repertoire des fichiers à nettoyer,
    Out, returned result : no returned result. la fct met les fichiers nettoyer dans le répertoire cleaned."""
    files_names = list_of_files(repertoire, "txt")
    for file_name in files_names:
        with open(repertoire + file_name, 'r', encoding='utf-8') as f1, open("./cleaned/" + file_name[:-4] + '_cleaned.txt', 'w', encoding='utf-8') as f2:
            for line in f1:
                new_line = remove_punctuations(line)  # Remove all punctuations
                new_line = remove_accents(new_line)   # Remove all accents.
                new_line = uppercase_to_lowercase(new_line)   # Convert the texts to lower case
                new_line = remove_mutlispaces(new_line)   # Remove les espaces superflues.

                f2.write(new_line)
