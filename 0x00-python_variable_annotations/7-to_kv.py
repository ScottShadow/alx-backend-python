#!/usr/bin/env python3
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a key-value pair to a tuple.

    Args:
        k: The key.
        v: The value.

    Returns:
        A tuple containing the key and the value.
    """
    return (k, float(v*v))
