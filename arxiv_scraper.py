import arxiv
from datetime import datetime, timedelta, timezone
from typing import List

# Default query components
BASE_QUERY = "(battery OR lithium-ion) AND (learning OR model OR forecasting OR physics)"
RESULTS_LIMIT = 7  

def build_query(custom_keywords: List[str]) -> str:
    """
    Combine base query with custom keywords to build a flexible search query.
    """
    if custom_keywords:
        keyword_query = " OR ".join(custom_keywords)
        full_query = f"({BASE_QUERY}) AND ({keyword_query})"
    else:
        full_query = BASE_QUERY
    return full_query

def fetch_arxiv_papers(custom_keywords: List[str] = [], days_back: int = 7):
    query = build_query(custom_keywords)
    date_threshold = datetime.now(timezone.utc) - timedelta(days=days_back)  # FIXED

    search = arxiv.Search(
        query=query,
        max_results=RESULTS_LIMIT,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    papers = []
    for result in search.results():
        if result.published >= date_threshold:
            papers.append({
                "title": result.title,
                "authors": [author.name for author in result.authors],
                "published": result.published.strftime("%Y-%m-%d"),
                "summary": result.summary,
                "link": result.entry_id
            })

    return papers

# Example usage
if __name__ == "__main__":
    keywords = ["fast charging", "plating"]
    days = 7  # only fetch papers published in the last 7 days
    papers = fetch_arxiv_papers(custom_keywords=keywords, days_back=days)

    for p in papers:
        print(f"{p['title']}\n{p['published']}\n{p['link']}\n")
