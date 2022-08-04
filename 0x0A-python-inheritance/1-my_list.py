#!/usr/bin/python3
# 1-my_list.py
# Barnabas
"""Defines an inherited list class MyList."""


class MyList(list):
    """Contains list
    """

    def print_sorted(self):
        """Prints self in sorted format
        """

        print(sorted(self))
