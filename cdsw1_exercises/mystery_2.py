#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: tvsirius
"""


def mystery_2(L: list[list | str | tuple | set], elem) -> list[list | str | tuple | set]:
    """ Return a list of iterables (or strings, selected from L, where elem is present

    :param L: list of iterables (or strings)
    :param elem: element to search in the lists (str if L is list of strings)
    :return: a list of iterables, where elem is present
    """

    assert isinstance(L, list), "L must be list"
    assert (len(L) == 0) or (min([isinstance(L[i], (list, tuple, set)) for i in range(len(L))])) or (
                min([isinstance(L[i], str) for i in range(len(L))]) and isinstance(elem,
                                                                                   str)), "L elements must be iterable or strings when elem is string"

    # base case
    if len(L) == 0:
        return []
    else:

        # checking elem in first list
        if elem in L[0]:
            # recursion with including L[0]
            return [L[0]] + mystery_2(L[1:], elem)
        else:
            # recursion without including L[0]
            return mystery_2(L[1:], elem)
