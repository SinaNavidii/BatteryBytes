from arxiv_scraper import fetch_arxiv_papers
from github_scraper import fetch_trending_github_repos
from jinja2 import Environment, FileSystemLoader

# ----------------------------
# Parameters
# ----------------------------
ARXIV_KEYWORDS = ["fast charging", "SEI"]
GITHUB_KEYWORDS = ["battery", "degradation", "lithium-ion"]
DAYS_BACK = 7
RESULT_LIMIT = 7

# ----------------------------
# Fetch Data
# ----------------------------
arxiv_papers = fetch_arxiv_papers(custom_keywords=ARXIV_KEYWORDS, days_back=DAYS_BACK)
github_repos = fetch_trending_github_repos(keywords=GITHUB_KEYWORDS, max_results=RESULT_LIMIT)

# ----------------------------
# Render Digest Template
# ----------------------------
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template("digest_template.html")

output_html = template.render(
    arxiv_papers=arxiv_papers,
    github_repos=github_repos,
    week_range=f"Last {DAYS_BACK} Days"
)

# Save output
with open("batterybytes_digest.html", "w", encoding="utf-8") as f:
    f.write(output_html)

print("Digest saved as batterybytes_digest.html")
