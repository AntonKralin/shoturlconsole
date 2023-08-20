from random import choice
from settings import MAX_LEN, CHARACTERS


def get_short(obj) -> str:
    domain = obj.alias
    if len(domain) > 5:
        domain = domain[:3] + '.' + domain[3:5]
    rand = get_random()
    return domain + '/' + rand


def get_random():
    rez = ""
    for i in range(MAX_LEN):
        rez += choice(CHARACTERS)
    return rez
