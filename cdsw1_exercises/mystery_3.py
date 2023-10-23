#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: tvsirius
"""


def mystery_3(L1: list, L2: list = None) -> list:
    """ Sort a list L1 and append a sorted list in the end of list L2 (if non empty), and return modified L2.
    To make just a sort you should call it with L2=None

    :param L1: List to be sorted
    :param L2: List, in the end of which will sorted L2 be appended
    :return: L2+sorted L1
    """

    assert isinstance(L1, list), "L1 must be list"

    # check, when L2 in not None
    if L2 is None:
        L2 = []

    assert isinstance(L2, list), "L2 must be list"

    # base case
    if len(L1) == 0:
        return L2

    else:
        # getting smallest element and appending it to L2
        smaller_element = min(L1)
        L1.remove(smaller_element)
        L2.append(smaller_element)

        # recursion call, with keeping L2 with stored sorted elements, and shortening L1
        return mystery_3(L1, L2)
