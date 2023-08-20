from requests import request


def print_urls(list):
    try:
        obj = next(list)
        print(f'({obj.url}, {obj.shot_url})')
        print_urls(list)

    except StopIteration:
        return


def print_alias(list):
    try:
        obj = next(list)
        print(f'({obj.alias}, {obj.homepage})')
        print_alias(list)

    except StopIteration:
        return


def print_obj(obj):
    print('Короткий интернет адресс:', obj.shot_url)
    print('Превдоним домашней страницы:', obj.alias)
    print('Стандартрый интернет адресс:', obj.url)


def print_test(obj):
    print('Адрес домашней страницы', obj.homepage)
    print('Псевдоним домашней страницы', obj.alias)
    req = request('GET', obj.homepage)
    print('Код ответа страницы', req.status_code)


def print_short(obj):
    print('Короткий интернет адресс:', obj.shot_url)
    print('Стандартрый интернет адресс', obj.url)
    req = request('GET', obj.homepage)
    print('Код ответа страницы', req.status_code)
