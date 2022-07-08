#!/usr/bin/python3
# File : 0-square_matrix_simple.py
# Squared simple
# Auth : Barnabas Abuye


def square_matrix_simple(matrix=[]):
    return ([list(map(lambda x: x * x, row)) for row in matrix])
