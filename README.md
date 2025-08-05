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
