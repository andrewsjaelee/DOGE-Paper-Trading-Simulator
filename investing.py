import pandas as pd
from sqlalchemy import create_engine
import tweetScraper

engine = create_engine('sqlite:///Liveprice.db')

# elon_tweet = tweetScraper.main()

in_position = False

cash = int(input('Enter how much you want to gamble '))
print('Press crtl + c, to immediately leave trade (wall street hack ;P)')

while cash: 
    df = pd.read_sql('DOGEUSDT', engine)
    last_price = df.price.iloc[-1] 
    if not in_position:
        # if last_price < df.price.mean()
        if last_price:
            buyprice = last_price
            in_position = True
            print('Bought for: '+str(buyprice))
    elif in_position:
        if last_price > 1.002 * buyprice or last_price < 0.998 * buyprice:
            sellprice = last_price
            in_position = False
            profit = (sellprice - buyprice) * cash
            print('Sold, profit is: '+str(profit))
            cash = False
    elif KeyboardInterrupt:
        break

