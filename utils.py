import requests
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def get_news_headlines(symbol):
    url = f"https://news.google.com/search?q={symbol}+stock+India"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = list({a.get_text() for a in soup.find_all("a") if a.get_text()})
    return titles[:3]

def analyze_sentiment(text):
    score = sia.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"
