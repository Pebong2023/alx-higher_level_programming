#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Find the key with the highest value in a dictionary.
    """
    if not a_dictionary:
        return None

    max_key = max(a_dictionary, key=a_dictionary.get)
    return (max_key)
