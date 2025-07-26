# backend/jd_scraper/reddit_scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_reddit(url: str) -> str:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        post_content = soup.find("div", class_="_1qeIAgB0cPwnLhDF9XSiJM")
        return post_content.get_text(strip=True) if post_content else "⚠️ Could not find job post content on Reddit."
    except Exception as e:
        return f"❌ Error fetching from Reddit: {e}"
