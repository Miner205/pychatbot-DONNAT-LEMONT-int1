"""
# Python project : My first chatBot.

# pythonProject-pychatbot-DONNAT-LEMONT-int1
# Teammates : DONNAT Arthur, LEMONT Mathis ; On (Discord and) Github.


# role of this file :
# data.py : functions for process the date / .txt files.
"""
import math
import os

def term_frequency(chaine: str) -> dict:
    """
    Computes the frequency of each character in the given string.

    Parameters:
    - chaine (str): The input string to analyze.

    Returns:
    - frequency (dict): A dictionary associating each character with its frequency of occurrence.
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
    files_words_list = []
    unique_words = []

    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)

        with open(filepath, 'r', encoding='utf-8') as file:
            file_content = file.read().lower().split()
            file_words = []

            for word in file_content:
                if word not in file_words:
                    file_words.append(word)

                if word not in unique_words:
                    unique_words.append(word)

            files_words_list.append(file_words)

    return files_words_list, unique_words

def inverse_document_frequency(files_words_list, unique_words):
    word_counts = {}
    for i in range(len(unique_words)):
        files_with_word = 0
        for j in range(len(files_words_list)):
            for k in range(len(files_words_list[j])):
                if unique_words[i] == files_words_list[j][k]:
                    files_with_word += 1
                    break  # Fixed: Move break inside the loop
        word_counts[unique_words[i]] = math.log10(len(files_words_list) / files_with_word)

    word_counts = dict(sorted(word_counts.items(), key=lambda item: item[0]))
    return word_counts

def calculate_tf_idf_matrix(directory_path):
    files_words_list, unique_words = words_and_unique_words_in_directory(directory_path)
    idf_values = inverse_document_frequency(files_words_list, unique_words)
    tf_idf_matrix = []

    for i in range(len(files_words_list)):
        tf_idf_vector = {}
        # Change tf_idf_vector from list to dictionary

        for word in unique_words:
            tf = files_words_list[i].count(word) / len(files_words_list[i])
            idf = idf_values[word]
            tf_idf_vector[word] = tf * idf
            # Store the TF-IDF values in a dictionary with words as keys

        tf_idf_matrix.append(tf_idf_vector)

    return tf_idf_matrix

def calculate_tf_idf_matrix(directory_path):
    files_words_list, unique_words = words_and_unique_words_in_directory(directory_path)
    idf_values = inverse_document_frequency(files_words_list, unique_words)
    tf_idf_matrix = []

    for i in range(len(files_words_list)):
        tf_idf_vector = {}
        # Change tf_idf_vector from list to dictionary

        for word in unique_words:
            tf = files_words_list[i].count(word) / len(files_words_list[i])
            idf = idf_values[word]
            tf_idf_vector[word] = tf * idf
            # Store the TF-IDF values in a dictionary with words as keys

        tf_idf_matrix.append(tf_idf_vector)

    return tf_idf_matrix

def calculate_tf_idf_matrix(directory_path):
    files_words_list, unique_words = words_and_unique_words_in_directory(directory_path)
    idf_values = inverse_document_frequency(files_words_list, unique_words)
    tf_idf_matrix = []

    for i in range(len(files_words_list)):
        tf_idf_vector = {}
        # Change tf_idf_vector from list to dictionary

        for word in unique_words:
            tf = files_words_list[i].count(word) / len(files_words_list[i])
            idf = idf_values[word]
            tf_idf_vector[word] = tf * idf
            # Store the TF-IDF values in a dictionary with words as keys

        tf_idf_matrix.append(tf_idf_vector)

    return tf_idf_matrix

def analyse_tf_idf(tf_idf_dict, option):
    if option == 'all':
        _, tf_idf_dict = calculate_tf_idf_matrix("./cleaned")
        analyse_tf_idf(tf_idf_dict, 1)
        analyse_tf_idf(tf_idf_dict, 2)
        analyse_tf_idf(tf_idf_dict, 3)
        analyse_tf_idf(tf_idf_dict, 4)
        analyse_tf_idf(tf_idf_dict, 5)
        analyse_tf_idf(tf_idf_dict, 6)

    if option == 1:
        # Extract all words and their TF-IDF scores into a list of tuples
        all_word_scores = [(word, tf_idf_score) for document in tf_idf_dict for word, tf_idf_score in document.items()]

        # Sort the list based on TF-IDF scores in ascending order
        sorted_word_scores = sorted(all_word_scores, key=lambda x: x[1])

        # Print the 10 words with the smallest TF-IDF scores
        print("10 words with the smallest TF-IDF scores:")
        for word, tf_idf_score in sorted_word_scores[:10]:
            print(f"{word}: {tf_idf_score}")

    elif option == 2:
        highest_tf_idf_score = max(tf_idf_score for document in tf_idf_dict for tf_idf_score in tf_idf_dict[document].values())
        highest_tf_idf_words = [word for document in tf_idf_dict for word, tf_idf_score in tf_idf_dict[document].items() if tf_idf_score == highest_tf_idf_score]
        print("Words with the highest TF-IDF score: ", highest_tf_idf_words)

    elif option == 3:
        chirac_documents = [document for document in tf_idf_dict if "Chirac" in document]
        chirac_most_repeated_words = [max(tf_idf_dict[document], key=tf_idf_dict[document].get) for document in chirac_documents]
        print("Words most repeated by President Chirac: ", chirac_most_repeated_words)

    elif option == 4:
        presidents_mentioned_nation = [get_president_name(document) for document in tf_idf_dict if 'Nation' in tf_idf_dict[document]]
        print("Presidents who mentioned the Nation: ", presidents_mentioned_nation)

    elif option == 5:
        first_president_to_mention_climate = next((get_president_name(document) for document in tf_idf_dict if 'climat' in tf_idf_dict[document] or 'écologie' in tf_idf_dict[document]), None)
        print("First president to mention climate or ecology: ", first_president_to_mention_climate)

    elif option == 6:
        words_mentioned_by_all_presidents = [word for word in tf_idf_dict[next(iter(tf_idf_dict))] if all(word in tf_idf_dict[document] for document in tf_idf_dict) and any(tf_idf_dict[document][word] != 0 for document in tf_idf_dict)]
        print("Words mentioned by all presidents: ", words_mentioned_by_all_presidents)

    else:
        print("This feature doesn't exist.")