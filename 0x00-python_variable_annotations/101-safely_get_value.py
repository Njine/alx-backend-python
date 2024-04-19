#!/usr/bin/env python3
'''Task 11's module.
'''
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''Retrieves a value from a dict using a given key.

    Args:
        dct (Mapping): The input mapping (dictionary-like object).
        key (Any): The key to retrieve the value for.
        default (Def, optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Res: The value corresponding to the key if found, otherwise the default value.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
