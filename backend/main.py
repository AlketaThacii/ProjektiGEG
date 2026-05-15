from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from scheduler_ui import scheduler, status_messages

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home route
@app.get("/")
def home():
    return {"message": "Intelligent News API Running"}


# Raw news
@app.get("/raw-news")
def raw_news():
    try:
        df = pd.read_csv("data/raw_news.csv")
        return df.to_dict(orient="records")
    except:
        return []


# Processed news
@app.get("/processed-news")
def processed_news():
    try:
        df = pd.read_csv("data/processed_news.csv")
        return df.to_dict(orient="records")
    except:
        return []


# Status notifications
@app.get("/status")
def get_status():
    return status_messages