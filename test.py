import tweetScraper
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tweet = 'NEED TO FIX THE TWEET SCRAPPER'

tweet_words = []

for word in tweet.split(' '):
    if word.startswith('@') and len(word) > 1:
        word = '@user'
    elif word.startswith('http'):
        word='http'
    tweet_words.append(word)
    
tweet_proc = " ".join(tweet_words)

print(tweet_proc)

