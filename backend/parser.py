from datetime import datetime


def parse_news(data):
    articles = []

    if not data:
        return articles

    for index, article in enumerate(data.get("articles", []), start=1):
        articles.append({
            "ID": index,
            "Title": article.get("title"),
            "Description": article.get("description"),
            "Website Link": article.get("source", {}).get("name"),
            "Article Link": article.get("url"),
            "Photo Link": article.get("urlToImage"),
            "CreatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    return articles