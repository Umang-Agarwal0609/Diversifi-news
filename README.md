# Diversifi News Sentiment API

This repository contains a FastAPI-based backend service that fetches recent stock-related news headlines and performs sentiment analysis using a pre-trained machine learning model. It caches results for performance optimization and computes an overall sentiment score from individual headline sentiments.


## Setup Instructions
---

Follow the steps below to set up and run the application locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Diversifi-news.git
cd Diversifi-news
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI server

```bash
uvicorn main:app --reload
```

### 5. Access the API documentation

Open your browser and go to:  
`http://127.0.0.1:8000/docs`


## News Source and Sentiment Analysis
---

### News Retrieval

The application retrieves recent news headlines using web scraping based on the given stock symbol. Supported symbols include examples like `"TCS"`, `"INFY"`, or `"RELIANCE"`.

### Sentiment Analysis

Each headline is analyzed using a transformer-based sentiment model. The output includes:

- Headline title
- Sentiment label: Positive, Neutral, or Negative

An additional field, `overall_sentiment`, is included in the response. It is calculated using a **majority vote** from all individual sentiment results.


## Use of AI Tools
---

The application uses the Hugging Face `transformers` library and the `distilbert-base-uncased-finetuned-sst-2-english` model for sentiment classification. This model is pre-trained and fine-tuned for binary sentiment analysis tasks and provides accurate predictions for short texts such as news headlines.


## Docker Support
---

The application includes a `Dockerfile` and can be run in a containerized environment using Docker.

### Build the Docker image

```bash
docker build -t diversifi-app .
```

### Run the Docker container

```bash
docker run -p 8000:8000 diversifi-app
```


## Deployment
---

The live API documentation application has been deployed having Docker integration [Link to the Deployed Version]([https://render.com](https://diversifi-backend.onrender.com/docs)) . The live API documentation is available at:

```
https://diversifi-backend.onrender.com/docs
```

You can test the `/news-sentiment` POST endpoint by entering a stock symbol (e.g., `"TCS"` or `"INFY"`) and viewing the sentiment results.


## Project Structure
---

```
├── main.py             # FastAPI application entry point
├── utils.py            # Scraping and sentiment functions
├── models.py           # SQLAlchemy ORM models
├── database.py         # DB connection and session logic
├── requirements.txt    # Python package dependencies
├── Dockerfile          # Docker configuration
└── README.md           # Project documentation
```
