#!/usr/bin/python3
"""Module for Abstract Base Class demonstration."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses."""
        pass


class Dog(Animal):
    """Subclass of Animal representing a Dog."""

    def sound(self):
        """Implementation of sound for Dog."""
        return "Bark"


class Cat(Animal):
    """Subclass of Animal representing a Cat."""

    def sound(self):
        """Implementation of sound for Cat."""
        return "Meow"
