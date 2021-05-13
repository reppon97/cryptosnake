import requests


class CryptoSnake:
    
    def __init__(self):
        self.url = f'https://api.binance.com/api/v3/ticker/price'
        self.page = None

    def get_available_symbols(self):
        self.page = requests.get(self.url)
        list_of_symbols = [symbol['symbol'] for symbol in self.page.json()]
        return list_of_symbols

    def get_crypto_price(self, symbol):
        self.page = requests.get(f'{self.url}?symbol={symbol}')
        return self.page.json()['price']


# price = CryptoSnake()
# print(price.get_crypto_price('SHIBUSDT'))
# print(price.get_available_symbols())
