import utility.data as data

# functions for generate an answer to a question of the user.


def generate(vector, relevant_doc):
    """In : vector is the tf-idf vector of the question ;
    relevant_doc is the relevant document (returned from fct ..) ;
    Out : answer."""
    word = highest_tf_idf(vector)


def highest_tf_idf(vector):


# def refine(answer):
    """refine the answer (returned from generate)."""
   # if #verif que le premier chr est une lettre ,;; fct dans data
   # refine_answer = data.highercase(answer[0]) + answer[1:]

   # if '.' answer[-1:] : #dernier chr
