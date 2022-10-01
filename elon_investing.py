from audioop import mul
import pandas as pd
from sqlalchemy import create_engine
from time import sleep
import sentiment

engine = create_engine('sqlite:///Liveprice.db')
elon_position = False
currentBalance = 0

while True:
    df = pd.read_sql('DOGEUSDT', engine)
    last_price = df.price.iloc[-1]
    elon = sentiment.analysis()
    if elon[0] > elon[2]:
        if not elon_position:
            multiplier = 100000000 * 0.8
            buy_price = last_price
            print('bought at: '+str(buy_price))
            in_account = buy_price * multiplier
            elon_position = True
            sleep(20)
        df = pd.read_sql('DOGEUSDT', engine)
        sell_position = df.price.iloc[-1]
        elon_position = False
        in_account = (sell_position * multiplier) - in_account
        print('sold at: '+str(sell_position))
    elif elon[0] < elon[2]:
        if not elon_position:
            multiplier = 100000000 * 1.5
            buy_price = last_price
            print('bought for: '+str(buy_price))
            in_account = buy_price * multiplier
            elon_position = True
            sleep(20)
        df = pd.read_sql('DOGEUSDT', engine)
        sell_position = df.price.iloc[-1]
        elon_position = False
        in_account = (sell_position * multiplier) - in_account
        print('sold at: '+str(sell_position))
    currentBalance += in_account
    print('total profit/loss from Elon: $'+str(currentBalance))
    sleep(3)