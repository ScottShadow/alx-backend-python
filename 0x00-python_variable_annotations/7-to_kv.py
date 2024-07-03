#!/usr/bin/env python3
"""
This module defines a function named `to_kv` that takes a key and a value   
as input and returns a tuple where the value has been squared.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a key (str) and a value (int or float) as input and returns a tuple
    where the value has been squared.

    :param k: The key (str)
    :param v: The value (int or float)
    :return: A tuple (key, squared_value)
    """
    # Convert the value to a float and square it
    squared_value = float(v * v)

    # Return a tuple with the key and the squared value
    return (k, squared_value)
