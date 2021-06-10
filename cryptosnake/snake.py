import requests


class CryptoSnake:
    
    def __init__(self):
        self.pair_url = f'https://api.binance.com/api/v3/ticker/price'
        self.exchange_info_url = 'https://api.binance.com/api/v1/exchangeInfo'
        self.page = None

    def get_available_pairings(self):
        self.page = requests.get(self.pair_url)
        list_of_symbols = [symbol['symbol'] for symbol in self.page.json()]
        return list_of_symbols

    def get_available_symbols(self):
        self.page = requests.get(self.exchange_info_url)
        response = [base['baseAsset'] for base in self.page.json()['symbols']]
        return response

    def get_crypto_price(self, pair):
        self.page = requests.get(f'{self.pair_url}?symbol={pair}')
        return self.page.json()['price']

    def crypto_to_usd(self, crypto_currency):
        """
        :param crypto_currency: e.g. "BTC", "ETH", "BNB" etc. Use get_available_symbols to get a full list.
        :return: Crypto currency to USD price/value.
        """
        try:
            self.page = requests.get(f'{self.pair_url}?symbol={crypto_currency}BUSD')
            return self.page.json()['price']
        except KeyError:
            return f'No such pairing. Check if you passed right parameter (use get_all_symbols() to get a full list), '\
                   f'or try to use crypto_to_tether() method instead. ' \
                   f'Keep in mind that USDT is TetherUS, not an actual USD.\nUse get_all_pairings() method to get' \
                   f' a full list of pairings.'

    def crypto_to_tether(self, crypto_currency):
        self.page = requests.get(f'{self.pair_url}?symbol={crypto_currency}USDT')
        return self.page.json()['price']

    def crypto_to_euro(self, crypto_currency):
        """
        :param crypto_currency: e.g. "BTC", "ETH", "BNB" etc. Use get_available_symbols to get a full list.
        :return: Crypto currency to EUR price/value.
        """
        try:
            self.page = requests.get(f'{self.pair_url}?symbol={crypto_currency}EUR')
            return self.page.json()['price']
        except KeyError:
            return f'No such pairing. Check if you passed right parameter (use get_all_symbols() to get a full list), '\
                   f'or try to use crypto_to_tether() method instead. ' \
                   f'Keep in mind that USDT is TetherUS, not an actual USD.\nUse get_all_pairings() method to get' \
                   f' a full list of pairings.'


price = CryptoSnake()
print(price.get_crypto_price('ETHBUSD'))
print(price.get_available_symbols())
print(price.get_available_pairings())
print(price.crypto_to_usd('ETH'))
print(price.crypto_to_euro('ETH'))
print(price.crypto_to_tether('ETH'))
