#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: tvsirius
"""


def mystery_1(L: list) -> list:
    """ Sorts a list in place and returns a sorted list

    :param L: list of elements, that allow comparasions (int, float, char)
    :return: sorted list
    """

    # check if L is list
    assert isinstance(L, list), "L must be list"

    # get list size
    list_size = len(L)

    # outer iteration through the list
    for i in range(list_size):

        # the c last elements are already sorted, as each iteration moves the biggest element to the end
        for j in range(0, list_size - i - 1):

            # compare L[j] with next, and swap if L[j] is greater
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]

    # returning the sorted list
    return L
