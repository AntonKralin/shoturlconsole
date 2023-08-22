"""module to generate shot url"""
from random import choice
from settings import MAX_LENGTH, CHARACTERS


def get_short(storage_object) -> str:
    """generate shot url from StorageObject

    Args:
        storage_object (StorageObject): StorageObject

    Returns:
        str: shot url
    """
    domain = storage_object.alias
    if len(domain) > 5:
        domain = domain[:3] + '.' + domain[3:5]
    randoms = get_random()
    return domain + '/' + randoms


def get_random() -> str:
    """generate random string with MAX_LENGTH from settigs.py

    Returns:
        str: random string
    """
    result = ""
    for _ in range(MAX_LENGTH):
        result += choice(CHARACTERS)
    return result
