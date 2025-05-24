import requests
from typing import List
from dotenv import load_dotenv
import os

# Load GitHub token from .env
load_dotenv(dotenv_path=".env")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("GitHub token not found. Check your .env file.")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

BASE_URL = "https://api.github.com/search/repositories"

from datetime import datetime, timedelta

def fetch_trending_github_repos(keywords: List[str], max_results: int = 5, sort_by: str = "stars", days_back: int = 30) -> List[dict]:
    """
    Fetches GitHub repositories created in the last `days_back` days that match the keyword query.
    """
    created_since = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
    keyword_query = " ".join(keywords)
    query_string = f"{keyword_query} language:python created:>={created_since}"

    params = {
        "q": query_string,
        "sort": sort_by,
        "order": "desc",
        "per_page": max_results
    }

    response = requests.get(BASE_URL, headers=HEADERS, params=params)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return []

    data = response.json()
    items = data.get("items", [])

    if not items:
        print("No repositories found for the given keywords and date range.")
        return []

    repos = []
    for item in items:
        repos.append({
            "name": item["full_name"],
            "description": item.get("description") or "No description provided.",
            "stars": item["stargazers_count"],
            "url": item["html_url"]
        })

    return repos


# --- Run Example ---
if __name__ == "__main__":
    keywords = ["battery", "degradation", "lithium"]
    repos = fetch_trending_github_repos(keywords)

    if repos:
        for repo in repos:
            print(f"{repo['name']} ({repo['stars']} stars)\n{repo['description']}\n{repo['url']}\n")

