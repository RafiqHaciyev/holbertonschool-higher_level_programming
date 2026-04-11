#!/usr/bin/python3
"""Module for demonstrating the Mixin design pattern."""


class SwimMixin:
    """Mixin to add swimming functionality."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin to add flying functionality."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a Dragon, composed of multiple behaviors."""

    def roar(self):
        """Specific behavior for a Dragon."""
        print("The dragon roars!")
