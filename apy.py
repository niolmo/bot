import requests
import json

base_key = "USD"
sym_key = "RUB"
amount = 100

headers= {
  "apikey": "5yesDL0ujwSaNRwXKF5LbaN5n4dHNHm5"
}

r = requests.get(f"https://api.apilayer.com/exchangerates_data/latest?base={base_key}&symbols={sym_key}", headers)
resp = json.loads(r.content)
new_price = resp['rates'][sym_key] * amount
