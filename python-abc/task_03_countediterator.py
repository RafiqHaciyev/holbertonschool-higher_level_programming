#!/usr/bin/python3
"""Module for a counter-enhanced iterator."""


class CountedIterator:
    """An iterator that keeps track of the number of items fetched."""

    def __init__(self, iterable):
        """Initialize the iterator and counter.

        Args:
            iterable: The object to be turned into an iterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the current count of items iterated."""
        return self.count

    def __next__(self):
        """Fetch the next item and increment the counter."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
