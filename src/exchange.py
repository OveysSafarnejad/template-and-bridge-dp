from abc import ABC, abstractmethod


class Exchange(ABC):
    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def get_prices(self):
        ...


class BinanceExchange(Exchange):

    def connect(self):
        print(f'connecting to {self.__class__.__name__}.')

    def get_prices(self):
        print(f'getting prices from {self.__class__.__name__} exchange.')
        return [10, 12, 18, 14]


class OtherExchange(Exchange):

    def connect(self):
        print(f'connecting to {self.__class__.__name__}.')

    def get_prices(self):
        print(f'getting prices from {self.__class__.__name__} exchange.')
        return [20, 34, 35, 67]
