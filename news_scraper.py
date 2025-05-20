import feedparser
from typing import List

def fetch_battery_news(rss_urls: List[str], max_items: int = 5) -> List[dict]:
    news_items = []

    for url in rss_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:max_items]:
            news_items.append({
                "title": entry.title,
                "summary": entry.summary if "summary" in entry else "",
                "link": entry.link,
                "published": entry.published if "published" in entry else "N/A",
                "source": feed.feed.get("title", "Unknown Source")
            })

    return news_items
