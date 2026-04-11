#!/usr/bin/python3
"""Module for exploring Multiple Inheritance and MRO."""


class Fish:
    """Parent class for fish-like behavior."""

    def swim(self):
        """Standard swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Standard fish habitat."""
        print("The fish lives in water")


class Bird:
    """Parent class for bird-like behavior."""

    def fly(self):
        """Standard flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Standard bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Subclass inheriting from both Fish and Bird."""

    def fly(self):
        """Override bird fly behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override fish swim behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override both parents' habitat behavior."""
        print("The flying fish lives both in water and the sky!")
