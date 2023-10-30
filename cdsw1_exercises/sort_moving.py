#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: tvsirius
"""


def sort_moving(task_list: list, result_list: list = None) -> list:
    """ Sort a list task_list and append a sorted list in the end of list result_list (if non empty), and return modified result_list.
    To make just a sort you should call it with result_list=None

    :param task_list: List to be sorted
    :param result_list: List, in the end of which will sorted result_list be appended
    :return: result_list+sorted task_list

    >>> sort_moving([])
    []

    >>> sort_moving([1])
    [1]

    >>> sort_moving([1,8,66,-2,3])
    [-2, 1, 3, 8, 66]

    >>> sort_moving(['r','a','z','f'],[1,2,'o'])
    [1, 2, 'o', 'a', 'f', 'r', 'z']
    """

    # assert correct params
    assert isinstance(task_list, list), "task_list must be list"
    assert isinstance(result_list, (list | None )), "result_list must be list"

    # make empty list for result, if result_list None
    if result_list is None:
        result_list = []

    # base case
    if len(task_list) == 0:
        return result_list

    # sort by getting the smallest element of task_list and appending to the result_list,
    # so it will append elements in ascending order
    smaller_element = min(task_list)
    task_list.remove(smaller_element)
    result_list.append(smaller_element)

    # recursion will keep going on until base case len(task_list)==0
    return sort_moving(task_list, result_list)
