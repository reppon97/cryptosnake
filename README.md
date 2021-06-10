### Simple, unofficial python wrapper for [Binance API](https://binance-docs.github.io/apidocs/spot/en/#change-log).

You'll find this easy-to-use package helpful if you're interested in general market data and cryptocurrency values. You don't need to have a Binance account or API Key since you can't purchase/trade cryptocurrencies using this package.

-------------

## Installation

python3 -m pip install cryptosnake

### or

pip3 install cryptosnake

-----------------

## Usage

```

from cryptosnake import CryptoSnake

snake = CryptoSnake()

# Crypto to USDT. Takes currency as an argument.
snake.crypto_to_tether('ETH')

# Crypto to BUSD. Takes currency as an argument. Keep in mind that it is BUSD, not USDT and make sure that API provides you the info you need.
snake.crypto_to_usd('ADA')

# Crypto to euro. 
snake.crypto_to_euro('BTC')

# Get a list of available symbols
snake.get_available_symbols()

# Get a list of available pairings
snake.get_available_pairings()

# Get crypto price. Takes crypto pairing as an argument
snake.get_crypto_price('ETHUSDT')

```

### Donate

If this package was useful, and you'd like to help out, feel free to donate.

* ETH: 0x47b9afb6a0580e79ac228f0ce233323549f30284

* BTC: 1FosbV9CXXwTiLvVa33QyUGvqeF6zhA629

* ADA: DdzFFzCqrhssxaX8qbkwKrG5ZWjeZCBnRVEcV12f2D2TdQttkgjDukZqHv9sTEwdNq8KwXbCEGZboE6rEwLXDYSiVWiVA7RvmyYpoWiA

* LTC: LZNHh8bVZtdeegDPnaMZu1aHYMwKpYsUiW

