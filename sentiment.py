from lib2to3.pgen2 import token
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import tweetScraper

def analysis():
    tweet = tweetScraper.main()

    roberta = 'cardiffnlp/twitter-roberta-base-sentiment'

    model = AutoModelForSequenceClassification.from_pretrained(roberta)
    tokenizer = AutoTokenizer.from_pretrained(roberta)

    labels = ['Negative', 'Neutral', 'Positive']

    # sentiment analysis
    encoded_tweet = tokenizer(tweet, return_tensors='pt')

    output = model(**encoded_tweet)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    for i in range(len(scores)):
        l = labels[i]
        s = scores[i]
        labels[i] = scores[i]
    return (labels)

analysis()
