"""
A bunch of utility functions around Python collections.

A collection can be a list or a dictionary and depending on the type of
the collection, the behaviour of some of these functions can change.
"""

import operator

from pyutils.atomic import areinstance


def to_pretty_list(lst, sep=", ", last_sep=" & "):
    if len(lst) == 1:
        return lst[0]
    return f"{sep.join(lst[:-1])}{last_sep}{lst[-1]}"


def is_subset(dictionary, other, operation=operator.le):
    """
    Compare two dictionary and check whether `other` is a
    subset of `dictionary`.
    A dictionary subset is another dictionary containing at most all the
    key-value of the prime dictionary. If the supposed subset dictionary
    contains key-value pairs NOT IN the prime dictionary, it is not a subset.

    :param dictionary: The prime dictionary which must contain the
                       subset dictionary `other`.
    :type dictionary: dict
    :param other: The other dictionary which must be a subset of
                  the prime dictionary `dictionary`
    :type other: dict
    :param operation: The comparison operation to perform, which is used
                      to compare the two dictionaries. It can be an equality
                      comparison, a "greater than", "lower or equal than", etc.
    :type operation: operator

    :return: True if the `other` dictionary is a subset of `dictionary`,
             else False.
    :rtype: bool
    """
    return operation(dictionary.items(), other.items())


def index_of(collection, item, match=False):
    """
    Find the index of the item in the collection.
    If the item is not found in the collection, -1 is returned.

    :param collection: The collection in which to find the index of `item`.
    :type collection: list or tuple or dict
    :param item: The item from `collection` whose index is returned.
    :type item: Any

    :return: The index of the item in the collection, or -1 if the item does
             not exist in the collection.
    :rtype: int
    """
    operation = operator.eq if match else operator.le
    for key, value in enumerate(collection):
        if areinstance(dict, value, item) and is_subset(item, value, operation):
            return key
        elif value == item:
            return key
    return -1


def find_one(collection, pattern):
    """
    Find the first item in the collection -a list of dictionaries- matching
    with the pattern -a subset of the item dictionary.

    :param collection: A list of dictionaries in which to find the item.
    :type collection: list
    :param pattern: Dictionary subset to compare with collection items.
                    At best an entire item, at least a dictionary subset
                    of an item.
    :type pattern: dict

    :return: The whole item from the collection, or None if not found.
    :rtype: dict
    """
    for _, value in enumerate(collection):
        if is_subset(pattern, value):
            return value
    return None


def find_all(collection, pattern, reverse=False):
    """
    Find the items in the collection -a list of dictionaries- matching
    with the pattern -a subset of the item dictionary.

    :param collection: A list of dictionaries from which to find the items.
    :type collection: list
    :param pattern: Dictionary subset to compare with collection items.
                    At best an entire item, at least a dictionary subset
                    of an item.
    :type pattern: dict

    :return: The list of items from the collection matching the pattern,
             at most the entire collection and at least an empty list.
    :rtype: list
    """
    values = []
    for _, value in enumerate(collection):
        if is_subset(pattern, value):
            condition = not reverse
        else:
            condition = reverse

        if condition:
            values.append(value)
    return values
