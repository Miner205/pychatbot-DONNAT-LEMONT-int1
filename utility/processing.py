
"""
# Python project : My first chatBot.

# pythonProject-pychatbot-DONNAT-LEMONT-int1
# Teammates : DONNAT Arthur, LEMONT Mathis ; On (Discord and) Github.


# role of this file :
# processing.py :              .
"""

import unicodedata


def question_to_list(question):
    """role : ,
    In, parameters : ,
    Out, returned result : ."""
    question = question.split(" ")
    i = 0

    while i < len(question):
        question[i] = question[i].lower()
        if question[i] == '':
            del question[i]

        cleaned_string = ''.join(c for c in unicodedata.normalize('NFD', question[i]) if unicodedata.category(c) != 'Mn')

        # Remove special characters
        cleaned_string = ''.join(e for e in cleaned_string if e.isalnum() or e.isspace())

        question[i] = cleaned_string

        i += 1

    if question[-1] == '':
        del question[-1]

    return question
