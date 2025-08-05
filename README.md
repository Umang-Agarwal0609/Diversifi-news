# 📈 Diversifi News Sentiment API

This is a FastAPI-based backend service that fetches the latest stock-related news headlines for a given symbol and performs sentiment analysis on them using a pre-trained AI model. It also caches the results for performance and returns an **overall sentiment** derived from individual headlines.

---

## 🛠 Setup Instructions

Follow the steps below to run the project locally:

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
4. Run the FastAPI app
bash
Copy
Edit
uvicorn main:app --reload
5. Open Swagger Docs in Browser
Go to: http://127.0.0.1:8000/docs

📡 What Was Used
🔎 For News:
Web scraping is used to extract the latest stock headlines from sources like Google News or Yahoo Finance.

You can pass a symbol like TCS or RELIANCE to the /news-sentiment endpoint and receive the latest headlines.

💬 For Sentiment Analysis:
Sentiment is determined using a transformers-based pre-trained model.

The sentiment for each headline can be positive, neutral, or negative.

🤖 How AI Tools Were Used
The model used is: distilbert-base-uncased-finetuned-sst-2-english from Hugging Face Transformers

It performs text classification to detect the sentiment of each headline.

Based on all predictions, an overall_sentiment field is calculated using a majority vote among individual sentiments.

🐳 Docker Support (Optional Bonus)
To build the Docker image:
bash
Copy
Edit
docker build -t diversifi-app .
To run the container:
bash
Copy
Edit
docker run -p 8000:8000 diversifi-app
🌍 Live Demo (Render Deployment)
API deployed and live at:

👉 https://diversifi-backend.onrender.com/docs

Use the /news-sentiment POST endpoint to test with a symbol like "INFY" or "TCS".

🧠 Features
✅ Live news headline scraping

✅ Sentiment analysis using AI

✅ Caching with SQLite (expires after 10 minutes)

✅ REST API with automatic docs via Swagger

✅ Dockerized for easy deployment

✅ Deployed on Render for public access

🗂 File Structure
graphql
Copy
Edit
├── main.py             # FastAPI app with endpoints
├── utils.py            # Functions for scraping & sentiment
├── models.py           # SQLAlchemy DB models
├── database.py         # SQLite DB setup
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker instructions
└── README.md           # You're here!
📜 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Built by Umang Agarwal for the Diversifi backend assignment 🚀

yaml
Copy
Edit

---

### ✅ After pasting this:

1. Save it as `README.md` in your project root.
2. Run:
```bash
git add README.md
git commit -m "Added polished README with setup, tools, AI explanation"
git push origin main
