import time, datetime

import ccxt


def print_ohlcv(ohlcv):
    date = ccxt.Exchange.iso8601 (ohlcv[0])

    print("Time - {}".format(date))
    print("    Open   : {}".format(ohlcv[1]))
    print("    High   : {}".format(ohlcv[2]))
    print("    Close  : {}".format(ohlcv[3]))
    print("    Low    : {}".format(ohlcv[4]))
    print("    Volume : {}".format(ohlcv[5]))


def main():
    exchange = ccxt.kraken()

    #timestamps are multiplied by 1000 to represent miliseconds
    last_time = int(time.time() - 60) * 1000

    if exchange.hasFetchOHLCV:
        data = exchange.fetch_ohlcv("BTC/USD", '1m', since=last_time)

        for d in data:
            print_ohlcv(d)

    print(exchange.iso8601(exchange.milliseconds()))

if __name__ == "__main__":
    main()
