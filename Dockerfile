# 1. Use an official Python base image
FROM python:3.10

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy all files from your project into the container
COPY . .

# 4. Install all dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Download NLTK data (VADER)
RUN python -m nltk.downloader vader_lexicon

# 6. Command to run your FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
