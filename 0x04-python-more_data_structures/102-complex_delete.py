#!/usr/bin/python3
# File : 102-complex_delete.py
# Squared by using map
# Auth : Barnabas Abuye


def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break

    return (a_dictionary)
