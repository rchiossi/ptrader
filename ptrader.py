import time, datetime

import ccxt


def print_ohlcv(ohlcv):
    date = datetime.datetime.fromtimestamp(int(ohlcv[0]) / 1000).strftime('%Y-%m-%d %H:%M:%S')

    print("Time - {}".format(date))
    print("    Open   : {}".format(ohlcv[1]))
    print("    High   : {}".format(ohlcv[2]))
    print("    Close  : {}".format(ohlcv[3]))
    print("    Low    : {}".format(ohlcv[4]))
    print("    Volume : {}".format(ohlcv[5]))


def main():
    exchange = ccxt.kraken()

    #timestamps are multiplied by 100 to represent miliseconds
    last_time = int(time.time() * 1000) - 60000

    if exchange.hasFetchOHLCV:
        data = exchange.fetch_ohlcv("BTC/USD", '1m', since=last_time)

        for d in data:
            print_ohlcv(d)

    print(int(time.time()))

if __name__ == "__main__":
    main()
