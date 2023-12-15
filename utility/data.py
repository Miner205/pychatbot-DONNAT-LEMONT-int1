import os

# functions for process the date / .txt files.

def list_of_files(directory, extension):
    """

    """
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


files = list_of_files('speeches/', '.txt')


def get_president_name(file):
    """

    """
    name = file[11:-4]

    if '0' <= name[-1] <= '9':
        name = name[:-1]

    return name


president_surname = { 'Chirac': "Jacques", "Giscard d'Estaing": "Valérie", 'Hollande': "François", "Macron": "Emmanuel", "Mitterand": "François", "Sarkozy": "Nicolas" }


def get_president_surname(name):
    return president_surname[name]


def print_president_list():
    last = ""
    for i in files:
        txt = get_president_name(i)
        if txt != last:
            print(txt)
            last = txt

def lowercase(str):
    newstr = str
    for char in str:
#    if :
    return newstr


def highercase(str):
    newstr = str
    return


def is_letter():
    """verif si un charact est une lettre"""


def cleaned_file():
    for i in files:
        f = open(f"speeches/{i}", 'r', encoding='utf-8')
        lower = f.read().lower()

        writed = open(f"cleaned/{i}", 'w', encoding='utf-8')
        encoded = lower.encode('ascii', 'ignore')
        writed.write(encoded.decode())