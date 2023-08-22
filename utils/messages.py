"""module for print information"""
from requests import request


def print_urls(iterable):
    """recursion print (url, shot_url)

    Args:
        iterable: iterable list
    """
    try:
        storage_object = next(iterable)
        print(f'({storage_object.url}, {storage_object.shot_url})')
        print_urls(iterable)

    except StopIteration:
        return


def print_alias(iterable):
    """recursion print (alias, homepage)

    Args:
        iterable: iterable list
    """
    try:
        storage_object = next(iterable)
        print(f'({storage_object.alias}, {storage_object.homepage})')
        print_alias(iterable)

    except StopIteration:
        return


def print_obj(storage_object):
    """print shot url, alias, url of StorageObject

    Args:
        storage_object (StorageObject)
    """
    print('Короткий интернет адресс:', storage_object.shot_url)
    print('Превдоним домашней страницы:', storage_object.alias)
    print('Стандартрый интернет адресс:', storage_object.url)


def print_test(storage_object):
    """print homepage, alias, status code of url
    from StorageObject

    Args:
        storage_object (StorageObject)
    """
    print('Адрес домашней страницы', storage_object.homepage)
    print('Псевдоним домашней страницы', storage_object.alias)
    request_object = request('GET', storage_object.homepage, timeout=60)
    print('Код ответа страницы', request_object.status_code)


def print_short(storage_object):
    """print short url, url, status code of url
    from StorageObject

    Args:
        storage_object (StorageObject)
    """
    print('Короткий интернет адресс:', storage_object.shot_url)
    print('Стандартрый интернет адресс', storage_object.url)
    request_object = request('GET', storage_object.homepage, timeout=60)
    print('Код ответа страницы', request_object.status_code)
