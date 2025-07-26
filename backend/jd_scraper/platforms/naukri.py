import requests
from bs4 import BeautifulSoup

def scrape(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        desc_div = soup.find("div", class_="jd-container") or soup.find("section")
        return desc_div.get_text(strip=True) if desc_div else "❌ Job description not found."
    except Exception as e:
        return f"❌ Failed to scrape Naukri: {e}"

