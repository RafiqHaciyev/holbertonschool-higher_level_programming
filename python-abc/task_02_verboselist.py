#!/usr/bin/python3
"""Module for extending the built-in list class."""


class VerboseList(list):
    """A list that prints notifications when modified."""

    def append(self, item):
        """Add an item and print notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extend the list and print notification."""
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Print notification and remove an item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Print notification and pop an item."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
