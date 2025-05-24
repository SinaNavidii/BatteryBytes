from arxiv_scraper import fetch_arxiv_papers
from github_scraper import fetch_trending_github_repos
from news_scraper import fetch_battery_news
from config import load_user_config
from emailer import send_digest_email
from jinja2 import Environment, FileSystemLoader
import os

def generate_and_send_digest():
    config = load_user_config()
    arxiv_keywords = config["topics"]
    github_keywords = config["topics"]
    user_email = config["email"]

    DAYS_BACK = 7
    GITHUB_LOOKBACK_DAYS = 30
    RESULT_LIMIT = 5

    print("🔍 Fetching arXiv papers...")
    arxiv_papers = fetch_arxiv_papers(custom_keywords=arxiv_keywords, days_back=DAYS_BACK)

    print("📦 Fetching GitHub repos...")
    github_repos = fetch_trending_github_repos(keywords=github_keywords, max_results=RESULT_LIMIT, days_back=GITHUB_LOOKBACK_DAYS)

    print("📰 Fetching battery news...")
    NEWS_FEEDS = [
        "https://www.sciencedaily.com/rss/matter_energy/batteries.xml",
        "https://electrek.co/feed/",
        "https://phys.org/rss-feed/technology-news/energy-tech/"
    ]
    news_items = fetch_battery_news(rss_urls=NEWS_FEEDS, max_items=RESULT_LIMIT)

    # Load template and render
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template("digest_template.html")

    output_html = template.render(
        arxiv_papers=arxiv_papers,
        github_repos=github_repos,
        news_items=news_items,
        week_range=f"Last {DAYS_BACK} Days"
    )

    digest_path = os.path.join(os.getcwd(), "batterybytes_digest.html")
    with open(digest_path, "w", encoding="utf-8") as f:
        f.write(output_html)

    print("✅ Digest saved as batterybytes_digest.html")

    # Send the digest via email
    send_digest_email(to_email=user_email)