import requests
from bs4 import BeautifulSoup

def scrape(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        job_desc = soup.find("div", class_="description__text") or soup.find("section")
        return job_desc.get_text(strip=True) if job_desc else "❌ Job description not found."
    except Exception as e:
        return f"❌ Failed to scrape LinkedIn: {e}"
