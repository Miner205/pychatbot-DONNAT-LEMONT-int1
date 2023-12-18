"""
# Python project : My first chatBot.

# pythonProject-pychatbot-DONNAT-LEMONT-int1
# Teammates : DONNAT Arthur, LEMONT Mathis ; On (Discord and) Github.


# role of this file :
# data.py : functions for process the date / .txt files.
"""

def calculate_term_frequency(input_string: str) -> dict:
    """
    Computes the frequency of each character in the given string.

    Parameters:
    - input_string (str): The input string to analyze.

    Returns:
    - frequency (dict): A dictionary associating each character with its frequency of occurrence.
    """
    frequency = {}
    for i in range(len(input_string)):
        if input_string[i] not in frequency:
            frequency[input_string[i]] = 1
        else:
            frequency[input_string[i]] += 1

    frequency = dict(sorted(frequency.items(), key=lambda item: item[0]))
    return frequency


def calculate_words_and_unique_words(directory_path):
    """
    Reads text files in the specified directory and returns a list of lists of words in each file and a list of unique words.

    Parameters:
    - directory_path (str): The path to the directory containing text files.

    Returns:
    - files_words_list (list): A list of lists of words in each file.
    - unique_words (list): A list of unique words across all files.
    """
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


def calculate_inverse_document_frequency(files_words_list, unique_words):
    """
    Computes the inverse document frequency for each unique word.

    Parameters:
    - files_words_list (list): A list of lists of words in each file.
    - unique_words (list): A list of unique words across all files.

    Returns:
    - word_counts (dict): A dictionary associating each unique word with its inverse document frequency.
    """
    word_counts = {}
    for i in range(len(unique_words)):
        files_with_word = 0
        for j in range(len(files_words_list)):
            for k in range(len(files_words_list[j])):
                if unique_words[i] == files_words_list[j][k]:
                    files_with_word += 1
                break
        word_counts[unique_words[i]] = math.log10(len(files_words_list) / files_with_word)

    word_counts = dict(sorted(word_counts.items(), key=lambda item: item[0]))
    return word_counts


def calculate_tf_idf_matrix(directory_path):
    """
    Computes the TF-IDF matrix for a collection of documents in the specified directory.

    Parameters:
    - directory_path (str): The path to the directory containing text files.

    Returns:
    - tf_idf_matrix (list): The TF-IDF matrix for the documents in the directory.
    """
    files_words_list, unique_words = calculate_words_and_unique_words(directory_path)
    idf_values = calculate_inverse_document_frequency(files_words_list, unique_words)
    tf_idf_matrix = []

    for i in range(len(files_words_list)):
        tf_idf_vector = []

        for word in unique_words:
            tf = files_words_list[i].count(word) / len(files_words_list[i])
            idf = idf_values[word]
            tf_idf_vector.append(tf * idf)

        tf_idf_matrix.append(tf_idf_vector)

    return tf_idf_matrix


def analyze_tf_idf(tf_idf_dict, option):
    """
    Executes implemented features based on the provided option.

    Parameters:
    - tf_idf_dict (dict): The TF-IDF dictionary.
    - option (str or int): The number (1 to 6) corresponding to the feature to run.
    """
    if option == 'all':
        _, tf_idf_dict = calculate_tf_idf_matrix("./cleaned")
        analyze_tf_idf(tf_idf_dict, 1)
        analyze_tf_idf(tf_idf_dict, 2)
        analyze_tf_idf(tf_idf_dict, 3)
        analyze_tf_idf(tf_idf_dict, 4)
        analyze_tf_idf(tf_idf_dict, 5)
        analyze_tf_idf(tf_idf_dict, 6)

    if option == 1:
        # Feature 1: Display the list of least important words in the document corpus.
        least_important_words = [word for document in tf_idf_dict for word, tf_idf_score in tf_idf_dict[document].items() if tf_idf_score < 0]
        # Remove duplicates
        least_important_words = list(dict.fromkeys(least_important_words))
        print("Least important words: ", least_important_words)

    elif option == 2:
        # Feature 2: Display the word(s) with the highest TF-IDF score.
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
