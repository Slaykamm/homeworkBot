class ConversionException(Exception):
    pass
import requests
import json
from config import keys


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
            

    

        if quote == base:
            raise ConversionException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать Валюту {quote}')

        try:
            base_ticker = keys[base]

        except KeyError:
            raise ConversionException(f'Не удалось обработать Валюту {base}')
    
        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Указано не верно количество {amount}')  

        r=requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
