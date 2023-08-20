from dataclasses import dataclass
from utils.regex import WebParser
from utils.cut import get_short
from utils.messages import print_alias, print_urls, print_obj, \
    print_test, print_short


@dataclass(init=False)
class StorageObject:
    url: str = ''
    shot_url: str = ''
    alias: str = ''
    homepage: str = ''


class StorageService:
    def __init__(self):
        self.dict = dict()

    def append(self, http: str) -> None:
        pars = WebParser(http)
        st_obj = StorageObject()

        st_obj.url = http
        st_obj.alias = pars.get_alias()
        st_obj.homepage = pars.get_homepage()
        st_obj.shot_url = get_short(st_obj)

        if self.dict.get(st_obj.alias):
            self._check_append(st_obj)
        else:
            self.dict[st_obj.alias] = [st_obj]

        print_obj(st_obj)

    def _check_append(self, obj: StorageObject) -> None:
        list = self.dict[obj.alias]
        for i in list:
            if i.url == obj.url:
                return
        self.dict[obj.alias] = list.append(obj)

    def print_by_alias(self, alias: str):
        list = self.dict.get(alias, None)
        if list:
            obj = list[0]
            print_test(obj)
        else:
            print('Адрес домашней страницы не найден')

    def print_by_short(self, short: str):
        for value in self.dict.values():
            obj = self._find_shot(value, short)
            if obj:
                print_short(obj)
        if not obj:
            print('Стандартный интернет-адрес не найден')

    @staticmethod
    def _find_shot(list, short) -> StorageObject:
        for i in list:
            if i.shot_url == short:
                return i

    def print_all(self):
        print('Псевдонимы')
        for values in self.dict.values():
            iterable = iter(values)
            print_alias(iterable)

        print('\nКороткие интернет-адресса')
        for values in self.dict.values():
            iterable = iter(values)
            print_urls(iterable)

    def print_dict(self):
        for key, item in self.dict.items():
            print(key, item)
