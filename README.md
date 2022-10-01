# DOGE Paper Trading Simulator

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

Optionally, you can visualize the price of DOGE through the `visualizer.ipynb` notebook.

To try the different strategies, simply run either the `elon_investing.py` or `investing.py`

## Elon Musk Tweet Sentiment Strategy
The `elon_investing.py` script uses `sentiment.py` and `tweetScraper.py` to determine the how much DOGE you buy. 

When `tweetScraper.py` is called, it returns the most recent tweet that includes ‘Elon Musk’. Now we can use the roBerta sentiment analyzer to score the tweet as either `Negative’, ‘Neutral’, or ‘Positive’.


A more negative tweet will result in purchasing less DOGE, vice-versa.

## Backtesting the Strategies 
### Momentum Swing Strategy

### Elon Tweet Sentiment Strategy

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
