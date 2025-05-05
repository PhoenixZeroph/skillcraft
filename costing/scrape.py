"""Scraper GitHub issues + JIRA dataset (run local)."""
import json, requests, time, os
from pathlib import Path
from bs4 import BeautifulSoup as BS

RAW = Path("data/raw"); RAW.mkdir(parents=True, exist_ok=True)

GITHUB_API = "https://api.github.com/search/issues"
HEADERS = {"Accept": "application/vnd.github+json"}


def scrape_github(max_pages=30):
    all_items = []
    for page in range(1, max_pages + 1):
        q = "label:\"good first issue\" state:open language:python"
        url = f"{GITHUB_API}?q={q}&per_page=100&page={page}"
        r = requests.get(url, headers=HEADERS)
        data = r.json().get("items", [])
        if not data:
            break
        for it in data:
            all_items.append({
                "source": "github",
                "id": it["id"],
                "title": it["title"],
                "body": it["body"],
                "labels": [l["name"] for l in it["labels"]],
                "created": it["created_at"]
            })
        time.sleep(1)
    Path("data/raw/github_issues.jsonl").write_text("\n".join(json.dumps(x) for x in all_items))

if __name__ == "__main__":
    scrape_github()
