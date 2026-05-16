from apscheduler.schedulers.background import BackgroundScheduler
from collector import collect_news
from parser import parse_news
from storage import save_raw_news, save_processed_news
from rewriter import rewrite_text

scheduler = BackgroundScheduler()

# status global
status_messages = []


def add_status(message):
    status_messages.append(message)

    # mbaj vetëm 10 mesazhet e fundit
    if len(status_messages) > 10:
        status_messages.pop(0)

    print(message)


def run_pipeline():
    add_status("Scraping started")

    data = collect_news()

    parsed = parse_news(data)

    add_status(f"{len(parsed)} articles collected")

    save_raw_news(parsed)

    add_status("Raw CSV updated successfully")

    processed = []

    for item in parsed:
     processed.append({
        "ID": item["ID"],
        "Original Title": item["Title"],
        "Rewritten Title": rewrite_text(item["Title"]),
        "Original Description": item["Description"],
        "Rewritten Description": item["Description"],
        "Source Website": item["Website Link"],
        "Article Link": item["Article Link"],
        "CreatedAt": item["CreatedAt"]
    })

    add_status("AI rewriting completed")

    save_processed_news(processed)

    add_status("Processed CSV updated successfully")


scheduler.add_job(run_pipeline, 'interval', minutes=5)
scheduler.start()
run_pipeline()
print("AI rewriting completed")
print("Processed CSV updated successfully")