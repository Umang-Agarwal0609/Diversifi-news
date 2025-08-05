from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from collections import Counter  # <-- New
from database import SessionLocal
from models import NewsSentiment
from utils import get_news_headlines, analyze_sentiment

app = FastAPI()

class SymbolRequest(BaseModel):
    symbol: str

@app.post("/news-sentiment")
def get_sentiment(data: SymbolRequest):
    db: Session = SessionLocal()
    now = datetime.utcnow()

    # Check cache
    recent = db.query(NewsSentiment).filter(
        NewsSentiment.symbol == data.symbol
    ).order_by(NewsSentiment.timestamp.desc()).first()

    if recent and (now - recent.timestamp).seconds < 600:
        # Calculate overall sentiment from cached headlines
        sentiment_counts = Counter([item["sentiment"] for item in recent.headlines])
        overall_sentiment = sentiment_counts.most_common(1)[0][0]

        return {
            "symbol": recent.symbol,
            "timestamp": recent.timestamp.isoformat(),
            "overall_sentiment": overall_sentiment,
            "headlines": recent.headlines
        }

    # Fresh fetch
    raw_headlines = get_news_headlines(data.symbol)
    result = [{"title": title, "sentiment": analyze_sentiment(title)} for title in raw_headlines]

    # Compute overall sentiment
    sentiment_counts = Counter([item["sentiment"] for item in result])
    overall_sentiment = sentiment_counts.most_common(1)[0][0]

    # Store in DB
    record = NewsSentiment(
        symbol=data.symbol,
        timestamp=now,
        headlines=result
    )
    db.add(record)
    db.commit()

    return {
        "symbol": data.symbol,
        "timestamp": now.isoformat(),
        "overall_sentiment": overall_sentiment,
        "headlines": result
    }
