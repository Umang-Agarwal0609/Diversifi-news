from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class NewsSentiment(Base):
    __tablename__ = "news_sentiments"
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    timestamp = Column(DateTime)
    headlines = Column(JSON)
