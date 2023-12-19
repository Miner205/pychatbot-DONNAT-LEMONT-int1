"""
# Python project : My first chatBot.

# pythonProject-pychatbot-DONNAT-LEMONT-int1
# Teammates : DONNAT Arthur, LEMONT Mathis ; On (Discord and) GitHub.


# role of this file :
# main.py : for run the project.
"""

import utility.data as data
import utility.tf_idf as tf_idf
import utility.processing as process

from time import sleep


def menu():
    """role : affiche le menu de toutes les features / actions possibles. (display with format),
    In, parameters : none,
    Out, returned result : none (il n'y a rien a retourné ; car il n'y a que des affichages à faire)."""
    print("Choose a feature between : ")
    features = ["0 : Stop the program.",
                "1 : Display the list of least important words in the document corpus.",
                "2 : Display the word(s) with the highest TD-IDF score.",
                "3 : Indicate the most repeated word(s) by President Chirac.",
                "4 : Indicate the name(s) of the president(s) who spoke of the 'Nation' and the one who repeated it the most time.",
                "5 : Identify the first president to talk about climate ('climat') and/or ecology ('écologie').",
                "6 : Display word(s) mentioned by all the president."]

    x = -1
    tf_idf_matrix = tf_idf.calculate_tf_idf_matrix("./cleaned")

    while x != 0:
        for feature in features:
            print("| {:^120} |".format(feature))
        x = int(input("Enter the number of the chosen feature : "))
        if x != 0:
            tf_idf_dict = tf_idf_matrix  # Assign tf_idf_matrix directly to tf_idf_dict
            tf_idf.analyse_tf_idf(tf_idf_dict, x)
        # sleep(5)


if __name__ == '__main__':
    data.cleaned_file()
    menu()
