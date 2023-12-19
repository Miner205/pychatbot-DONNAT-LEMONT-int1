"""
# Python project : My first chatBot.

# pythonProject-pychatbot-DONNAT-LEMONT-int1
# Teammates : DONNAT Arthur, LEMONT Mathis ; On (Discord and) Github.


# role of this file :
# data.py : functions for process the date / .txt files.
"""
import os
import math
from . import data

def calculate_term_frequency(input_string: str) -> dict:
    """Role: Calculate the term frequency for each character in the input string.
    In, parameters: input_string - a string.
    Out, returned result: A dictionary containing the frequency of each character."""
    frequency = {}
    for char in input_string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

def words_and_unique_words_in_directory(directory_path):
    """Role: Retrieve the list of words for each file in the given directory and unique words across all files.
    In, parameters: directory_path - the path to the directory containing files.
    Out, returned result: A tuple containing a list of words for each file and a list of unique words."""
    files_words_list = []
    unique_words = set()

    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)

        with open(filepath, 'r', encoding='utf-8') as file:
            file_content = file.read().split()
            file_words = list(set(file_content))

            unique_words.update(file_words)
            files_words_list.append(file_words)

    return files_words_list, list(unique_words)

def inverse_document_frequency(files_words_list, unique_words):
    """Role: Calculate the inverse document frequency for unique words.
    In, parameters: files_words_list - a list of words for each file, unique_words - a list of unique words.
    Out, returned result: A dictionary containing the inverse document frequency values for each unique word."""
    word_counts = {word: 0 for word in unique_words}
    for word in unique_words:
        for file_words in files_words_list:
            if word in file_words:
                word_counts[word] += 1

    for word, count in word_counts.items():
        word_counts[word] = math.log10(len(files_words_list) / count) if count > 0 else 0

    return word_counts

def calculate_tf_idf_matrix(directory_path):
    """Role: Calculate the TF-IDF matrix for files in the given directory.
    In, parameters: directory_path - the path to the directory containing files.
    Out, returned result: A matrix containing TF-IDF values for each word in each file."""
    files_words_list, unique_words = words_and_unique_words_in_directory(directory_path)
    idf_values = inverse_document_frequency(files_words_list, unique_words)
    tf_idf_matrix = []

    for file_words in files_words_list:
        tf_idf_vector = {}
        for word in unique_words:
            tf = file_words.count(word) / len(file_words)
            idf = idf_values[word]
            tf_idf_vector[word] = tf * idf

        tf_idf_matrix.append(tf_idf_vector)

    return tf_idf_matrix

def presidents_mentioned_climate(tf_idf_matrix):
    """Role: Identify the first and most mentioned president regarding climate or ecology.
    In, parameters: tf_idf_matrix - a matrix containing TF-IDF values for each word in each file.
    Out, returned result: A tuple containing the first president who mentioned it and the president who mentioned it the most."""
    occurrences_by_president = {}

    files_names = data.list_of_files("./speeches", "txt")

    for i, document in enumerate(tf_idf_matrix):
        if i < len(files_names):  # Check if the index is within the bounds of the list
            president_name = data.get_president_name(files_names[i])
            # Counting occurrences of "climate" and "ecology" in the document
            occurrences_by_president[president_name] = document.get("climate", 0) + document.get("ecology", 0)

    if not occurrences_by_president:
        return None, None

    # Find the president who mentioned it first
    first_occurrence_president = min(occurrences_by_president, key=occurrences_by_president.get)
    
    # Find the president who mentioned it the most
    most_occurrences_president = max(occurrences_by_president, key=occurrences_by_president.get)

    return first_occurrence_president, most_occurrences_president

def words_mentioned_by_all_presidents(tf_idf_matrix):
    """Role: Identify the words mentioned by all presidents.
    In, parameters: tf_idf_matrix - a matrix containing TF-IDF values for each word in each file.
    Out, returned result: A list of words mentioned by all presidents."""
    words_mentioned_by_all = set(tf_idf_matrix[0].keys())

    for president_tf_idf in tf_idf_matrix[1:]:
        words_mentioned_by_all.intersection_update(president_tf_idf.keys())

    result = list(words_mentioned_by_all)
    return result
    
def analyse_tf_idf(tf_idf_matrix, option):
    """Role: Analyze the TF-IDF matrix based on the chosen option.
    In, parameters: tf_idf_matrix - a matrix containing TF-IDF values for each word in each file, option - an integer representing the chosen analysis option.
    Out, returned result: Print the analysis results based on the chosen option."""
    if option == 1:
        all_word_scores = [(word, tf_idf_score) for document in tf_idf_matrix for word, tf_idf_score in document.items()]

        # Sort the list based on TF-IDF scores in ascending order
        sorted_word_scores = sorted(all_word_scores, key=lambda x: x[1])

        # Print the 10 words with the smallest TF-IDF scores
        print("10 words with the smallest TF-IDF scores:")
        for word, tf_idf_score in sorted_word_scores[:10]:
            print(f"{word}: {tf_idf_score}")

    elif option == 2:
        highest_tf_idf_score = max(tf_idf_score for document in tf_idf_matrix for tf_idf_score in document.values())
        highest_tf_idf_word = max((word for document in tf_idf_matrix for word, tf_idf_score in document.items() if tf_idf_score == highest_tf_idf_score))
        print("Word with the highest TF-IDF score: ", highest_tf_idf_word)

    elif option == 3:
        all_words = [word for document in tf_idf_matrix for word, _ in document.items()]

        # Modified function for question 3
        word_counts = {}
        for word in all_words:
            word_counts[word] = word_counts.get(word, 0) + 1

        most_repeated_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        print("5 most repeated words: ", most_repeated_words)

    elif option == 4:
        file_names = data.list_of_files("./speeches", "txt")
        if file_names:
            occurrences_per_president = [(data.get_president_name(file_name), file_name.count("nation")) for file_name in file_names]
            occurrences_per_president.sort(key=lambda x: x[1], reverse=True)

            if occurrences_per_president:
                first_occurrence = occurrences_per_president[0][0]
                most_occurrences = occurrences_per_president[0][0]
                print("First president who mentioned 'nation':", first_occurrence)
                print("President who mentioned 'nation' the most times:", most_occurrences)
            else:
                print("No occurrences of 'nation' found in any file.")
        else:
            print("No files found in the 'speeches' directory.")

    elif option == 5:
        first_occurrence, most_occurrences_president = presidents_mentioned_climate(tf_idf_matrix)
        
        if first_occurrence:
            print("First president to mention climate or ecology:", first_occurrence)
            print("President who mentioned it the most:", most_occurrences_president)
        else:
            print("No presidents mentioned climate or ecology.")

    elif option == 6:
        words_mentioned_by_all_presidents_result = words_mentioned_by_all_presidents(tf_idf_matrix)
        print(f"Words mentioned by all presidents: {words_mentioned_by_all_presidents_result}")
    else:
        print("This feature doesn't exist.")