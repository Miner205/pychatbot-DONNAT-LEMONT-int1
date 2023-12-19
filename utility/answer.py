
"""
# Python project : My first chatBot.

# pythonProject-pychatbot-DONNAT-LEMONT-int1
# Teammates : DONNAT Arthur, LEMONT Mathis ; On (Discord and) GitHub.


# role of this file :
# answer.py : functions for generate an answer to a question of the user.
"""

import utility.data as data
import utility.tf_idf as tf_idf


def generate(question_vector, name_relevant_doc):
    """role : ,
    In, parameters : question_vector is the tf-idf vector of the question,
    name_relevant_doc is the name (in cleaned) of the relevant document (returned from ... function),
    Out, returned result : answer."""
    word = highest_tf_idf(question_vector)


def highest_tf_idf(vector):   # à mettre dans tf_idf.py?
    """role : ,
    In, parameters : ,
    Out, returned result : ."""


def refine(answer):
    """role : refine the answer (in generate function),
    In, parameters : an answer,
    Out, returned result : the refine answer."""
    if : #verif que le premier chr est une lettre ,;; fct dans data
   # refine_answer = data.highercase(answer[0]) + answer[1:]

   # if '.' answer[-1:] : #dernier chr
