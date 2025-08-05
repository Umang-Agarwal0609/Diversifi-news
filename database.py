from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine("sqlite:///sentiment.db")
SessionLocal = sessionmaker(bind=engine)

# Create table if not exists
Base.metadata.create_all(bind=engine)
