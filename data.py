import os


def list_of_files(directory, extension):
    """
    cette fonction retourne la liste des noms de fichiers se terminant par l'extension donnee dans un repertoire donne.
    
    paramètres :
    directory (str) : Le chemin du repertoire contenant les fichiers a analyser.
    extension (str) : L'extension du fichier

    retourne :
    files_names (liste) : Une liste de noms de fichiers se terminant par l'extension donnee.
    
    """
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


files = list_of_files('speeches/', '.txt')


def get_president_name(file):
    """
    cette fonction retourne le nom du president a partir du nom du fichier.

    parametres :
    file (str) : Le nom du fichier à analyser.

    retourne :
    name (str) : Le nom du président.
    
    """
    name = file[11:-4]

    if name[-1].isdigit():
        name = name[:-1]

    return name


president_surname = {'Chirac': "Jacques", "Giscard d'Estaing": "Valérie", 'Hollande': "François", "Macron": "Emmanuel", "Mitterand": "François", "Sarkozy": "Nicolas"}


def get_president_surname(name):
    """
    cette fonction retourne le nom de famille du president a partir du nom du president.

    parametres :
    name (str) : Le nom du president a analyser.

    retourne :
    president_surname[name] (str) : Le nom de famille du president.
    
    """
    return president_surname[name]


def print_president_list():
    """   
    Cette fonction affiche la liste des présidents à partir des noms des fichiers.

    """
    last = ""
    for i in files:
        txt = get_president_name(i)
        if txt != last:
            print(txt)
            last = txt


def cleaned_file():
    """
    Cette fonction nettoie les fichiers du répertoire speeches et les écrit dans le répertoire cleaned.

    """
    ecrit = {'ç': 'c', 'é': 'e', 'è': 'e', 'ê': 'e', 'à': 'a', 'â': 'a', 'ù': 'u', 'û': 'u', 'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o', 'œ': 'oe', 'É': 'E', 'È': 'E', 'Ê': 'E', 'À': 'A', 'Â': 'A', 'Ù': 'U', 'Û': 'U', 'Î': 'I', 'Ï': 'I', 'Ô': 'O', 'Ö': 'O', 'Œ': 'OE'}
    for i in files:
        f = open(f"speeches/{i}", 'r', encoding='utf-8')
        lower = f.read().lower()

        writed = open(f"cleaned/{i}", 'w', encoding='utf-8')
        lower = lower.replace("'", ' ')
        lower = lower.replace("-", ' ')
        lower = lower.replace("!", ' ')
        for key, value in ecrit.items():
            lower = lower.replace(key, value)
        lower = ' '.join(lower.split())
        encoded = lower.encode('ascii', 'ignore')
        writed.write(encoded.decode())
