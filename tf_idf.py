
"""
# Python project : My first chatBot.

# pythonProject-pychatbot-DONNAT-LEMONT-int1
# Teammates : DONNAT Arthur, LEMONT Mathis ; On (Discord and) Github.


# role of this file :
# tf_idf.py : tf_idf matrix functions.
"""

import math
from data import *
# import os
# import numpy as np


def term_frequency(chaine:str)->dict:
    """role : ,
    In, parameters : ,
    Out, returned result : ."""

    """
    fonction qui calcule la frequence d'apparition de chaque caractere dans une chaine de caracteres

    parametres :
    chaine (str) : La chaine de caracteres a analyser.

    retourne :
    frequency (dict) : Un dictionnaire associant a chaque caractere sa frequence d'apparition.
    """
    frequency = {}
    for i in range(len(chaine)):
        if chaine[i] not in frequency:
            frequency[chaine[i]] = 1
        else:
            frequency[chaine[i]] += 1

    frequency = dict(sorted(frequency.items(), key=lambda item: item[0]))
    return frequency



def words_and_unique_words_in_directory(directory_path):
    # Initialiser une liste pour stocker la liste de listes de mots et la liste de mots sans doublons
    files_words_list = []
    unique_words = []

    # Parcourir tous les fichiers du répertoire
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)

        # Lire le contenu du fichier et ajouter les mots à la liste de listes
        with open(filepath, 'r', encoding='utf-8') as file:
            file_content = file.read().lower().split()
            file_words = []

            # Ajouter les mots à la liste sans doublons
            for word in file_content:
                if word not in file_words:
                    file_words.append(word)
                
                # Ajouter les mots à la liste générale sans doublons
                if word not in unique_words:
                    unique_words.append(word)

            files_words_list.append(file_words)

    return files_words_list, unique_words




def inverse_document_frequency():
    word_counts = {}
    for i in range (len(unique_words)):
        files_with_word = 0
        for j in range (len(files_words_list)):
            for k in range (len(files_words_list[j])):
                if unique_words[i] == files_words_list[j][k]:
                    files_with_word += 1
                break
        word_counts[unique_words[i]] = math.log10(len(files_words_list) / files_with_word)

    word_counts = dict(sorted(word_counts.items(), key=lambda item: item[0]))












def tf_idf_matrix(directory: str) -> list:
    """role : ,
    In, parameters : ,
    Out, returned result : ."""

    """
    ecrire une fonction qui prend en parametre le repertoire ou se trouve l’ensemble des fichiers du corpus et qui retourne une liste de listes representant la matrice TF-IDF.

    parametres :
    directory (str) : Le chemin du repertoire contenant les fichiers à analyser.

    retourne :
    tf_idf_matrix (list) : Une liste de listes représentant la matrice TF-IDF.
    """
    idf_scores = inverse_document_frequency(directory)
    tf_idf_matrix = []
    tf_idf_dict = {}

    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as file:
            tf_scores = term_frequency(file.read().split())
            tf_idf_scores = []
            tf_idf_scores_dict = {}
            for word in tf_scores:
                try:
                    #? Si le mot n'est pas unique on passe au suivant
                    # if tf_scores[word] != 1:
                    #     continue
                    tf_idf_scores.append(tf_scores[word] * idf_scores[word])
                    tf_idf_scores_dict[word] = tf_scores[word] * idf_scores[word]
                except:
                    pass
            tf_idf_matrix.append(tf_idf_scores)
            tf_idf_dict[filename] = tf_idf_scores_dict

    return tf_idf_matrix, tf_idf_dict


def analyse_tf_idf(tf_idf_dict, option):
    """role : ,
    In, parameters : ,
    Out, returned result : ."""

    """
    implemented features.
    In : -tf_idf_dict : ...  ; -option : number (1 to 6) of a feature to run.
    """
    if option == 'all':
        _, tf_idf_dict = tf_idf_matrix("./cleaned")
        analyse_tf_idf(tf_idf_dict, 1)
        analyse_tf_idf(tf_idf_dict, 2)
        analyse_tf_idf(tf_idf_dict, 3)
        analyse_tf_idf(tf_idf_dict, 4)
        analyse_tf_idf(tf_idf_dict, 5)
        analyse_tf_idf(tf_idf_dict, 6)

    if option == 1:
        # 1. Afficher la liste des mots les moins importants dans le corpus de documents.
        least_important_words = [word for document in tf_idf_dict for word, tf_idf_score in tf_idf_dict[document].items() if tf_idf_score < 0]
        # enleve si ya des doublons
        least_important_words = list(dict.fromkeys(least_important_words))
        print("Mots les moins importants : ", least_important_words)

    elif option == 2:
        # 2. Afficher le(s) mot(s) ayant le score TD-IDF le plus eleve
        highest_tf_idf_score = max(tf_idf_score for document in tf_idf_dict for tf_idf_score in tf_idf_dict[document].values())
        highest_tf_idf_words = [word for document in tf_idf_dict for word, tf_idf_score in tf_idf_dict[document].items() if tf_idf_score == highest_tf_idf_score]
        print("Mots avec le score TF-IDF le plus eleve : ", highest_tf_idf_words)

    elif option == 3:
        # 3. Indiquer le(s) mot(s) le(s) plus repete(s) par le president Chirac
        chirac_documents = [document for document in tf_idf_dict if "Chirac" in document]
        chirac_most_repeated_words = [max(tf_idf_dict[document], key=tf_idf_dict[document].get) for document in chirac_documents]
        print("Mots les plus repetes par le president Chirac : ", chirac_most_repeated_words)

    elif option == 4:
        # 4. Indiquer le(s) nom(s) du (des) president(s) qui a (ont) parle de la « Nation » et celui qui l’a repete le plus de fois
        presidents_mentioned_nation = [get_president_name(document) for document in tf_idf_dict if 'Nation' in tf_idf_dict[document]]
        print("Presidents qui ont parle de la Nation : ", presidents_mentioned_nation)

    elif option == 5:
        # 5. Indiquer le premier president a parler du climat et/ou de l’ecologie
        first_president_to_mention_climate = next((get_president_name(document) for document in tf_idf_dict if 'climat' in tf_idf_dict[document] or 'écologie' in tf_idf_dict[document]), None)
        print("Premier president a parler du climat ou de l'ecologie : ", first_president_to_mention_climate)

    elif option == 6:
        # 6. Hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les presidents ont evoques.
        words_mentioned_by_all_presidents = [word for word in tf_idf_dict[next(iter(tf_idf_dict))] if all(word in tf_idf_dict[document] for document in tf_idf_dict) and any(tf_idf_dict[document][word] != 0 for document in tf_idf_dict)]
        print("Mots evoques par tous les presidents : ", words_mentioned_by_all_presidents)

    else:
        print("This feature doesn't exist.")
