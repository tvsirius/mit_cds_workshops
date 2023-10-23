#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: tvsirius
"""


def mystery_4(L: list[list | str | tuple | set], elem) -> list[list | str | tuple | set]:
    """ Return a list of iterables (list,tuples,sets) or strings selected from original list, containing elem

    :param L: list of iterable sets or strings (if str then elem must be string)
    :param elem: element to
    :return: return a list of iterables containing elem
    """

    assert isinstance(L, list), "L must be list"
    assert (len(L) == 0) or (min([isinstance(L[i], (list, tuple, set)) for i in range(len(L))])) or (
            min([isinstance(L[i], str) for i in range(len(L))]) and isinstance(elem,
                                                                               str)), "L elements must be iterable or strings when elem is string"

    # list for results
    result_list = []

    # iteration all L element, which are also collections
    for subset in L:

        # if elem in subset - append
        if elem in subset:
            result_list.append(subset)

    return result_list
