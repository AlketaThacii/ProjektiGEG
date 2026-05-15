# ProjektiGEG

## Project Description

Intelligent News Aggregator is an AI-powered news collection system that automatically collects news from the internet, stores them in CSV files, rewrites content using AI, and displays them in a user-friendly dashboard.

The system updates automatically every 5 minutes and provides request logging, notifications, and data visualization.

---

## Features

- Automatic news collection every 5 minutes
- CSV data storage
- AI rewriting for titles and descriptions
- Request logging
- Frontend dashboard
- Search functionality
- Status notifications
- Automatic frontend refresh

---

## Technologies Used

### Backend
- Python
- FastAPI
- APScheduler
- Pandas
- Requests

### Frontend
- React
- Axios
- CSS

### AI
- OpenAI API / Ollama

### Storage
- CSV Files

---

## Project Structure

```txt
intelligent-news/
│
├── backend/
│   ├── main.py
│   ├── collector.py
│   ├── parser.py
│   ├── storage.py
│   ├── rewriter.py
│   ├── scheduler_ui.py
│   ├── logs/
│   │   └── requests.log
│   ├── data/
│   │   ├── raw_news.csv
│   │   └── processed_news.csv
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   └── package.json
│
└── README.md
