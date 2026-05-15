import pandas as pd
import os

RAW_FILE = "data/raw_news.csv"
PROCESSED_FILE = "data/processed_news.csv"


def save_raw_news(news):
    df = pd.DataFrame(news)

    try:
        if os.path.exists(RAW_FILE) and os.path.getsize(RAW_FILE) > 0:
            existing = pd.read_csv(RAW_FILE)
            df = pd.concat([existing, df], ignore_index=True)

    except Exception as e:
        print("Raw CSV Error:", e)

    df.to_csv(RAW_FILE, index=False)


def save_processed_news(news):
    df = pd.DataFrame(news)

    try:
        if (
            os.path.exists(PROCESSED_FILE)
            and os.path.getsize(PROCESSED_FILE) > 0
        ):
            existing = pd.read_csv(PROCESSED_FILE)
            df = pd.concat([existing, df], ignore_index=True)

    except Exception as e:
        print("Processed CSV Error:", e)

    df.to_csv(PROCESSED_FILE, index=False)