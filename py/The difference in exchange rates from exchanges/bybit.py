import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from coinmarketcap import ticker
from API import API_BYBIT

para = ticker + "USDT"

# Установите параметры запроса
parameters = {
    "category":"spot",
    "symbol": para,
}

# Заголовок запроса
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_BYBIT,
}

url = ' https://api.bybit.com/v5/market/tickers'



def getData():
    # Inicialisate session
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters).json()
        #print(json.dumps(response, indent=4))
        return (float(response["result"]["list"][0]["bid1Price"]) + float(response["result"]["list"][0]["ask1Price"]))/2
        #return response["weightedAvgPrice"]
    except (ConnectionError, Timeout, TooManyRedirects) as err:
        print(err)   

getData()