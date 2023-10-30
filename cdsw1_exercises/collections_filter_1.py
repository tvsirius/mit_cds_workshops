#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: tvsirius
"""


def collections_filter_1(task_list: list[list | str | tuple | set], elem) -> list[list | str | tuple | set]:
    """ Return a list of iterables (list,tuples,sets) or strings selected from original list, containing elem

    :param task_list: list of iterable sets or strings (if str then elem must be string)
    :param elem: element to
    :return: return a list of iterables containing elem
    >>> collections_filter_1([[]],1)
    []

    >>> collections_filter_1([[1]],1)
    [[1]]

    >>> collections_filter_1([[1,2],[2,3,4],[3,4,5],[5,6]],3)
    [[2, 3, 4], [3, 4, 5]]

    >>> collections_filter_1(['abc','bdf','xyz','hfv'],'f')
    ['bdf', 'hfv']
    """

    # assert correct params
    assert isinstance(task_list, list), "task_list must be list"
    if isinstance(elem, str):
        for list_item in task_list:
            assert isinstance(list_item, str), "If elem is str, list elements must be strings"
    else:
        for list_item in task_list:
            assert isinstance(list_item, (list, tuple, set)), "If elem is not string, list elements must be iterables"

    # will store matching list here
    result_list = []

    # check subsets one by one, and put matching to the result list
    for subset in task_list:
        if elem in subset:
            # gathering matching subsets
            result_list.append(subset)

    return result_list
