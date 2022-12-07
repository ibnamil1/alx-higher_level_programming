#!/usr/bin/python3
# 0-square_matrix_simple.py
#Ibnamil<limanibrahim92@gmail.com>

def square_matrix_simple(matrix=[]):
    """compute the square values of all integers of a matrix"""
    return ([list(map(lambda x: x * x, row)) for row in matrix])
