def exclusive_or(string:str, list1:list[str], list2:list[str])->bool:
    """
    Return True if the string is in only one of the lists, and False otherwise.

    Parameters:
    string (str): The string to search for in the lists.
    list1 (list): The first list of strings.
    list2 (list): The second list of strings.

    Returns:
    bool: True if the string is in only one of the lists, and False otherwise.
    
    >>> exclusive_or('abc',['a','b','abc'],['b','d','v'])
    True

    >>> exclusive_or('abc',['a','b','ac'],['b','d','v','11'])
    False

    >>> exclusive_or('abc',['a','b','abc'],['b','abc','d','v','11'])
    False
    """
    # Check if the inputs are of the expected types
    assert isinstance(string, str), "The first input must be a string"
    assert isinstance(list1, list) and all(isinstance(i, str) for i in list1), "The second input must be a list of strings"
    assert isinstance(list2, list) and all(isinstance(i, str) for i in list2), "The third input must be a list of strings"

    # Check if the string is in only one of the lists
    return (string in list1 and string not in list2) or (string in list2 and string not in list1)