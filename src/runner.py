from trader import MinMaxTrader, AverageTrader
from exchange import BinanceExchange, OtherExchange


def main() -> None:
    trader = MinMaxTrader(exchange=BinanceExchange())
    trader.process()
    print(100 * '-')

    trader = AverageTrader(exchange=BinanceExchange())
    trader.process()
    print(100 * '-')

    trader = MinMaxTrader(exchange=OtherExchange())
    trader.process()
    print(100 * '-')

    trader = AverageTrader(exchange=OtherExchange())
    trader.process()


if __name__ == "__main__":
    main()
