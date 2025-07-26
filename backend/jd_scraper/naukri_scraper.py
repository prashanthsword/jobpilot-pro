# backend/jd_scraper/naukri_scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_naukri(url: str) -> str:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        jd_div = soup.find("div", class_="dang-inner-html")
        return jd_div.get_text(strip=True) if jd_div else "⚠️ Could not find job description on Naukri."
    except Exception as e:
        return f"❌ Error fetching from Naukri: {e}"
