# DOGE Paper Trading Simulator
<p align="center">
<img width="253" alt="Screen_Shot_2022-09-30_at_8 19 11_PM-removebg-preview" src="https://user-images.githubusercontent.com/97712948/193384507-dfe6e656-ea99-4723-b364-15e1391c6213.png">
 </p>

A paper trading cryptocurrency simulator for the DOGEUSDT Token. Testing two investing strategies, the first being a  momentum swing trading algorithm, and the other being an Elon Musk Tweet Sentiment strategy. 

## Setup

To run this money maker, the required modules you need to install are:
```bash
pip install pandas
pip install sqlaclchemy
pip install unicorn-binance_websocket_api
pip install scipy
pip instal transformers
```

## How it works
First you need to run the `data.ipynb` notebook to get live DOGEUSDT data into your `Liveprice.db`.

Optionally, you can visualize the price of DOGE through the `visualizer.ipynb` notebook. The visualization should like the example below.
<p align="center">
  <img width="615" alt="Screen Shot 2022-09-30 at 5 55 31 PM" src="https://user-images.githubusercontent.com/97712948/193379232-df6fc8d7-7f04-4c7b-828d-41c8265a3b40.png">
 </p>

To try the different strategies, simply run either the `elon_investing.py` or `investing.py`

## Elon Musk Tweet Sentiment Strategy
The `elon_investing.py` script uses `sentiment.py` and `tweetScraper.py` to determine the how much DOGE you buy. 

When `tweetScraper.py` is called, it returns the most recent tweet that includes ‘Elon Musk’. Now we can use the roBerta sentiment analyzer to score the tweet as either `Negative’, ‘Neutral’, or ‘Positive’.


A more negative tweet will result in purchasing less DOGE, vice-versa.

## Backtesting the Strategies
### Momentum Swing Strategy
<p align="center">
  <img width="282" alt="Screen Shot 2022-09-30 at 5 42 41 PM" src="https://user-images.githubusercontent.com/97712948/193379483-c0c1fd06-2a38-4e37-a842-2d969ca07b18.png">
</p>
We find a lot less trades executing with this strategy because it only buys DOGE when it is below the mean price.

### Elon Tweet Sentiment Strategy
<p align="center">
  <img width="281" alt="Screen Shot 2022-09-30 at 5 54 46 PM" src="https://user-images.githubusercontent.com/97712948/193379531-e3b39554-de69-4c70-a549-e495b8ab919d.png">
</p>

### Implications
The return of both strategies are dependent on high short-term volatility, hence, if there was upward momentum in the short-run, we will likely see the Momentum Strategy executing few trades with relatively positive returns. Likewise for the Elon Strategy, however, if we ran `elon_investing.py` during a period of downward momentum we would see a compounding negative return.
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
