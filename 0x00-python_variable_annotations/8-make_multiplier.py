#!/usr/bin/env python3
"""
A module that defines a function for creating a function that mlt a given
number by a multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given number by a multiplier.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a number and multiplies
        it by the multiplier.
    """
    return (lambda x: x * multiplier)
