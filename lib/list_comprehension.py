# list_comprehension.py

def return_evens(sequence):
    """
    Returns a list of all the even elements in the given sequence of integers.
    """
    evens = [num for num in sequence if num % 2 == 0]
    return evens

def make_exclamation(sentences):
    """
    Adds an exclamation mark at the end of each sentence in the given list of strings.
    """
    exclaimed = [sentence + '!' for sentence in sentences]
    return exclaimed

