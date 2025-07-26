import requests
from bs4 import BeautifulSoup

def scrape(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        content = soup.find("div", attrs={"data-test-id": "post-content"})
        return content.get_text(strip=True) if content else "❌ No job post content found."
    except Exception as e:
        return f"❌ Failed to scrape Reddit: {e}"
