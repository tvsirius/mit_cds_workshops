#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: tvsirius
"""


def filter_collections_recursion(task_list: list[list | str | tuple | set], elem) -> list[list | str | tuple | set]:
    """ Return a list of iterables (or strings, selected from task_list, where elem is present

    :param task_list: list of iterables (or strings)
    :param elem: element to search in the lists (str if task_list is list of strings)
    :return: a list of iterables, where elem is present

    >>> filter_collections_recursion([[]],1)
    []

    >>> filter_collections_recursion([[1]],1)
    [[1]]

    >>> filter_collections_recursion([[1,2],[2,3,4],[3,4,5],[5,6]],3)
    [[2, 3, 4], [3, 4, 5]]

    >>> filter_collections_recursion(['abc','bdf','xyz','hfv'],'f')
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

    # check condition on first element
    if elem in task_list[0]:
        # recursion with shortening list, condition success
        return [task_list[0]] + filter_collections_recursion(task_list[1:], elem)

    # recursion with shortening list, condition fail
    return filter_collections_recursion(task_list[1:], elem)
