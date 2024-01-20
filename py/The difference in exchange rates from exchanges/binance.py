import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from coinmarketcap import ticker
from API import API_BNC

para = ticker + "USDT"

# Установите параметры запроса
parameters = {
    "symbol": para,
}

# Заголовок запроса
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_BNC,
}

url = ' https://api.binance.com/api/v3/ticker'

def getData():
    # Inicialisate session
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters).json()
        #print(json.dumps(response, indent=4))
        return response["weightedAvgPrice"]
    except (ConnectionError, Timeout, TooManyRedirects) as err:
        print(err)    



