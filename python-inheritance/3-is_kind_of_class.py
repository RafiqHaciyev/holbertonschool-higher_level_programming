#!/usr/bin/python3
"""This module defines an is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclasses

    Args:
        obj: the object to check
        a_class: the class to compare against

    Returns:
        True if obj is an instance of a_class or inherited, False otherwise
    """
    return isinstance(obj, a_class)
