"""module to storage data"""
from dataclasses import dataclass
from utils.regex import WebParser
from utils.cut import get_short
from utils.messages import print_alias, print_urls, print_obj, \
    print_test, print_short


@dataclass(init=False)
class StorageObject:
    """class to keep information
    fields:
        url: standart url
        shot_url: shot url
        alias: alias
        homepage: homepage
    """
    url: str = ''
    shot_url: str = ''
    alias: str = ''
    homepage: str = ''


class StorageService:
    """class to keep dictionaryionary {alias:[list of StorageObject]}
    """
    def __init__(self):
        self.dictionary = {}

    def append(self, http: str) -> None:
        """add new StorageObject to distionary from web url, 
        and print what add

        Args:
            http (str): web url site
        """
        parser = WebParser(http)
        storage_object = StorageObject()

        storage_object.url = http
        storage_object.alias = parser.get_alias()
        storage_object.homepage = parser.get_homepage()
        storage_object.shot_url = get_short(storage_object)

        if self.dictionary.get(storage_object.alias):
            self._check_append(storage_object)
        else:
            self.dictionary[storage_object.alias] = [storage_object]

        print_obj(storage_object)

    def _check_append(self, storage_object: StorageObject) -> None:
        """Checks if the dictionaryionary contains the same site in StorageObject, 
        if not append append it
        
        Args:
            storage_object (StorageObject): StorageObject with url
        """
        array = self.dictionary[storage_object.alias]
        for index in array:
            if index.url == storage_object.url:
                return
        self.dictionary[storage_object.alias] = array.append(storage_object)

    def print_by_alias(self, alias: str) -> None:
        """print information by alias of website

        Args:
            alias (str): alias of website
        """
        array = self.dictionary.get(alias, None)
        if array:
            storage_object = array[0]
            print_test(storage_object)
        else:
            print('Адрес домашней страницы не найден')

    def print_by_short(self, short: str) -> None:
        """print information by shot url of website

        Args:
            short (str): shot ulr of website
        """
        for value in self.dictionary.values():
            storage_object = self._find_shot(value, short)
            if storage_object:
                print_short(storage_object)
        if not storage_object:
            print('Стандартный интернет-адрес не найден')

    @staticmethod
    def _find_shot(array, short) -> StorageObject:
        """search shot url in list of StorageObject

        Args:
            array: list of StorageObject
            short: shot url of website

        Returns:
            StorageObject: contain shot url
        """
        for index in array:
            if index.shot_url == short:
                return index

    def print_all(self) -> None:
        """print all information
        """
        print('Псевдонимы')
        for values in self.dictionary.values():
            iterable = iter(values)
            print_alias(iterable)

        print('\nКороткие интернет-адресса')
        for values in self.dictionary.values():
            iterable = iter(values)
            print_urls(iterable)
