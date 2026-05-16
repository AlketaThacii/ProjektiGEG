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
    df = pd.read_csv("data/raw_news.csv")
    df = df.fillna("")
    return df.to_dict(orient="records")


# Processed news
@app.get("/processed-news")
def processed_news():
    df = pd.read_csv("data/processed_news.csv")
    df = df.fillna("")
    return df.to_dict(orient="records")

# Status notifications
@app.get("/status")
def get_status():
    return status_messages