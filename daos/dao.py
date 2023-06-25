import pickle
import os

from abc import ABC, abstractmethod


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource = '') -> None:
        self.__cache = {}
        self.__datasource = datasource
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except ValueError:
            pass

    def get_all(self):
        return self.__cache.values()

    def update(self, key):
        if key in self.__cache:
            index = self.__cache.index(key)
            self.__cache[index] = key
            self.__dump()
 