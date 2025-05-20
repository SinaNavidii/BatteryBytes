from arxiv_scraper import fetch_arxiv_papers
from github_scraper import fetch_trending_github_repos
from news_scraper import fetch_battery_news
from jinja2 import Environment, FileSystemLoader
import sys
sys.stdout.reconfigure(encoding='utf-8')

# ----------------------------
# Config
# ----------------------------
ARXIV_KEYWORDS = ["fast charging", "SEI", "solid-state"]
GITHUB_KEYWORDS = ["battery", "degradation", "lithium"]
NEWS_FEEDS = [
    "https://www.sciencedaily.com/rss/matter_energy/batteries.xml",
    "https://electrek.co/feed/",
    "https://phys.org/rss-feed/technology-news/energy-tech/"
]

DAYS_BACK = 7
RESULT_LIMIT = 7
GITHUB_LOOKBACK_DAYS = 7

# ----------------------------
# Fetch Content
# ----------------------------
print("🔍 Fetching arXiv papers...")
arxiv_papers = fetch_arxiv_papers(custom_keywords=ARXIV_KEYWORDS, days_back=DAYS_BACK)

print("📦 Fetching GitHub repos...")
github_repos = fetch_trending_github_repos(keywords=GITHUB_KEYWORDS, max_results=RESULT_LIMIT, days_back=GITHUB_LOOKBACK_DAYS)

print("📰 Fetching battery news...")
news_items = fetch_battery_news(rss_urls=NEWS_FEEDS, max_items=RESULT_LIMIT)

# ----------------------------
# Render HTML Template
# ----------------------------
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template("digest_template.html")

output_html = template.render(
    arxiv_papers=arxiv_papers,
    github_repos=github_repos,
    news_items=news_items,
    week_range=f"Last {DAYS_BACK} Days"
)

with open("batterybytes_digest.html", "w", encoding="utf-8") as f:
    f.write(output_html)

print("✅ Digest saved as batterybytes_digest.html")
