from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
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
        return {
            "symbol": recent.symbol,
            "timestamp": recent.timestamp.isoformat(),
            "headlines": recent.headlines
        }

    # Fresh fetch
    raw_headlines = get_news_headlines(data.symbol)
    result = [{"title": title, "sentiment": analyze_sentiment(title)} for title in raw_headlines]

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
        "headlines": result
    }
