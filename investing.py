import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///Liveprice.db')

in_position = False
currentBalance = 0

while True: 
    df = pd.read_sql('DOGEUSDT', engine)
    last_price = df.price.iloc[-1] 
    if not in_position:
        if last_price < df.price.mean():
            buyprice = last_price
            in_position = True
            print('Bought for: '+str(buyprice))
    elif in_position:
        if last_price > 1.003 * buyprice or last_price < 0.997 * buyprice:
            sellprice = last_price
            in_position = False
            profit = (sellprice - buyprice) * 100000000
            currentBalance += profit
            print('total profit/loss: $'+str(profit))
