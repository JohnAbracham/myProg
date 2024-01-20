import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from API import API_CMK

# Изменить для получению другой валюты
ticker = "XRP"

# Установите параметры запроса
parameters = {
    "symbol": ticker,
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_CMK,
}

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'


def getData():
    # Inicialisate session
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters).json()
        #print(json.dumps(response, indent=4))
        return [response["data"][ticker][0]["symbol"], # 0
        response["data"][ticker][0]["quote"]["USD"]["price"], # 1
        response["data"][ticker][0]["quote"]["USD"]["percent_change_1h"], # 2
        response["data"][ticker][0]["quote"]["USD"]["percent_change_24h"], # 3
        response["data"][ticker][0]["quote"]["USD"]["percent_change_7d"], # 4
        response["data"][ticker][0]["quote"]["USD"]["percent_change_30d"], # 5
        response["data"][ticker][0]["quote"]["USD"]["percent_change_60d"], # 6
        response["data"][ticker][0]["quote"]["USD"]["percent_change_90d"], # 7
        response["data"][ticker][0]["quote"]["USD"]["volume_24h"], # 8
        response["data"][ticker][0]["quote"]["USD"]["market_cap"], # 9
        response["data"][ticker][0]["circulating_supply"], # 10
        response["data"][ticker][0]["total_supply"], # 11
        response["data"][ticker][0]["max_supply"], # 12
        response["data"][ticker][0]["last_updated"]] # 13
        
        #print(json.dumps(price, indent=4))
    except (ConnectionError, Timeout, TooManyRedirects) as err:
        print(err)
