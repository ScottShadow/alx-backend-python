#!/usr/bin/env python3
"""
This module defines a function named `to_kv` that takes a key and a value   
as input and returns a tuple where the value has been squared.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    A function that takes a key and a value and returns a tuple where the value has been squared.

    Parameters:
        k (str): The key parameter.
        v (Union[int, float]): The value parameter.

    Returns:
        Tuple[str, float]: A tuple containing the key and the squared value.
    """

    # Convert the value to a float and square it
    squared_value = float(v * v)

    # Return a tuple with the key and the squared value
    return (k, squared_value)
