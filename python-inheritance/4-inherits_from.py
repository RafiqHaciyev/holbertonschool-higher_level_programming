#!/usr/bin/python3
"""This module defines an inherits_from function"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherited from a_class

    Args:
        obj: the object to check
        a_class: the class to compare against

    Returns:
        True if obj is instance of a subclass of a_class, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
