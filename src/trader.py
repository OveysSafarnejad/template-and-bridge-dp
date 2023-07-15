from abc import ABC, abstractmethod
from typing import List

from exchange import Exchange


class Trader(ABC):

    def __init__(self, exchange: Exchange):
        self.exchange = exchange

    @abstractmethod
    def should_sell(self, prices: List[int]) -> bool:
        ...

    @abstractmethod
    def should_buy(self, prices: List[int]) -> bool:
        ...

    def process(self):
        """Base template workflow for all implementations goes here"""
        self.exchange.connect()
        prices = self.exchange.get_prices()
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy!")
        elif should_sell:
            print(f"You should sell!")
        else:
            print(f"No action needed.")


class MinMaxTrader(Trader):

    def should_buy(self, prices: List[int]) -> bool:
        return prices[-1] == min(prices)

    def should_sell(self, prices: List[int]) -> bool:
        return prices[-1] == max(prices)


class AverageTrader(Trader):

    @staticmethod
    def list_average(prices: List[float]) -> float:
        return sum(prices) / len(prices)

    def should_buy(self, prices: List[int]) -> bool:
        return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[int]) -> bool:
        return prices[-1] > self.list_average(prices)
