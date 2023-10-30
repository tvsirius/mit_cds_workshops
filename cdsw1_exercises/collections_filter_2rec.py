#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: tvsirius
"""


def collections_filter_2rec(task_list: list[list | str | tuple | set], elem) -> list[list | str | tuple | set]:
    """ Return a list of iterables (or strings, selected from task_list, where elem is present

    :param task_list: list of iterables (or strings)
    :param elem: element to search in the lists (str if task_list is list of strings)
    :return: a list of iterables, where elem is present

    >>> collections_filter_2rec([[]],1)
    []

    >>> collections_filter_2rec([[1]],1)
    [[1]]

    >>> collections_filter_2rec([[1,2],[2,3,4],[3,4,5],[5,6]],3)
    [[2, 3, 4], [3, 4, 5]]

    >>> collections_filter_2rec(['abc','bdf','xyz','hfv'],'f')
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

    # base case
    if len(task_list) == 0:
        return []

    # each recursion call will check first element (collection) of the list,
    # and pass the shortened list [1:] to the next call
    if elem in task_list[0]:

        # result will include L[0]
        return [task_list[0]] + collections_filter_2rec(task_list[1:], elem)

    # result without L[0]
    return collections_filter_2rec(task_list[1:], elem)
