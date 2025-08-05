# Diversifi News Sentiment API

This repository contains a FastAPI-based backend service that fetches recent stock-related news headlines and performs sentiment analysis using a pre-trained machine learning model. It also caches the results in a local SQLite database for performance optimization and computes an overall sentiment score based on the aggregated results.

---

## Setup Instructions

Follow the steps below to set up and run the application locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Diversifi-news.git
cd Diversifi-news
2. Create a virtual environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the FastAPI server
bash
Copy
Edit
uvicorn main:app --reload
5. Access the API documentation
Open your browser and navigate to:

arduino
Copy
Edit
http://127.0.0.1:8000/docs
News Source and Sentiment Analysis
News Retrieval
The application retrieves recent news headlines based on the provided stock symbol using web scraping techniques. It is capable of fetching news for symbols such as "TCS", "INFY", or "RELIANCE".

Sentiment Analysis
Each headline is analyzed using a transformer-based sentiment analysis model. The output for each headline includes:

Title

Predicted sentiment (Positive, Neutral, or Negative)

An additional field, overall_sentiment, is calculated based on a majority vote from all individual sentiment predictions. This provides a summary-level view of the overall market sentiment for the given stock symbol.

Use of AI Tools
The application uses the Hugging Face transformers library and specifically leverages the distilbert-base-uncased-finetuned-sst-2-english model for sentiment classification. This model is pre-trained on a large corpus and fine-tuned for sentiment analysis tasks.

Docker Support (Optional)
The application can be containerized using Docker for easy deployment.

Build the Docker image
bash
Copy
Edit
docker build -t diversifi-app .
Run the Docker container
bash
Copy
Edit
docker run -p 8000:8000 diversifi-app
Deployment
The application is deployed on Render using Docker and is accessible at:

arduino
Copy
Edit
https://diversifi-backend.onrender.com/docs
This deployment includes the full functionality of the API, including real-time headline retrieval and sentiment analysis.

Project Structure
bash
Copy
Edit
├── main.py             # Entry point of the FastAPI application
├── utils.py            # Utility functions for scraping and sentiment
├── models.py           # SQLAlchemy models
├── database.py         # Database setup and session management
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker build instructions
└── README.md           # Project documentation
