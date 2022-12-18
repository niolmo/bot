import json

import requests

from config import exchanges


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            sym = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена!")

        if base == sym:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')
        headers = {
            "apikey": "5yesDL0ujwSaNRwXKF5LbaN5n4dHNHm5"
        }

        r = requests.get(f"https://api.apilayer.com/exchangerates_data/latest?base={base}&symbols={sym}", headers)
        resp = json.loads(r.content)
        new_price = resp['rates'][sym] * float(amount)
        new_price = round(new_price, 3)
        message = f"Цена {amount} {base} в {sym} : {new_price}"
        return message
