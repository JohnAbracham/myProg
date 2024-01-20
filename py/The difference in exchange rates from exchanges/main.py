import json
import time
import os

# CoinMarketCap
import coinmarketcap

# Exchangers
import binance
import bybit

#Tables
from prettytable import PrettyTable

#Token
from coinmarketcap import ticker

# Clear console 
clear_cmd = lambda: os.system('cls')

# Ограничить вывод символов после запятой
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

# Получить всю основную информацию с CoinMarketCap
def printDataCoinMarcetCap():

    global price_cmk
    global symbol_cmk

    table = PrettyTable()  # Определяем таблицу.
    data = coinmarketcap.getData() # Получаем данные через API

    # Определить таблицу
    table.field_names = ["Symbol","Price","percent_change_1h","percent_change_24h","volume_24h","market_cap","total_supply","max_supply","last_updated"]
    table.add_row([data[0],toFixed(data[1],3),toFixed(data[2],3),toFixed(data[3],3),toFixed(data[8],3),toFixed(data[9],3),toFixed(data[11],3),data[12],data[13]])

    print(table)
    symbol_cmk = data[0]
    price_cmk = data[1]


# Модули бирж
def moduleExchange():

    global price_binance
    global price_bybit

    table1 = PrettyTable() # Определяем таблицы

    table1.field_names = (["Symbol","Exchanger","Price","Difference(CoinMarketCap), $", "Difference(CoinMarketCap), %"]) # Определить таблицу

    price_binance = binance.getData()
    price_bybit = bybit.getData()

    table1.add_row([ticker,"Binance", toFixed(float(price_binance),4), toFixed(float(price_binance)-float(price_cmk),4), toFixed((float(price_binance)*100/float(price_cmk)-100),4)])
    table1.add_row([ticker,"Bybit", toFixed(float(price_bybit),4), toFixed(float(price_bybit)-float(price_cmk),4), toFixed((float(price_bybit)*100/float(price_cmk)-100),4)])

    print(table1)

# Основная функция
def main():

        while True:
            # Clear window console
            clear_cmd()
            try:
                # Вывод coinmarketcap
                printDataCoinMarcetCap()
                moduleExchange()         
            
                # Time for sleep
                time.sleep(60)
            except KeyboardInterrupt:
                print('[+]\tClose programm')
                os._exit(130)
                

if __name__ == "__main__":
    main()