import requests
import logging
import os

API_KEY = "782d15283ab6498092aa437fb1adb524"

URL = (
    f"https://newsapi.org/v2/top-headlines?"
    f"language=en&pageSize=10&apiKey={API_KEY}"
)

# krijohet folderi logs automatikisht
os.makedirs("logs", exist_ok=True)

# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/requests.log")
formatter = logging.Formatter(
    "%(asctime)s - %(message)s"
)

file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)


def collect_news():
    try:
        response = requests.get(URL)

        logger.info(
            f"Request Status: {response.status_code}"
        )

        print(
            f"Request Status: {response.status_code}"
        )

        if response.status_code == 200:
            return response.json()

        return None

    except Exception as e:
        logger.error(f"Request Error: {str(e)}")
        print(f"Request Error: {str(e)}")
        return None