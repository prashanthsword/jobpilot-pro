from backend.jd_scraper.linkedin_scraper import scrape_linkedin
from backend.jd_scraper.foundit_scraper import scrape_foundit
from backend.jd_scraper.reddit_scraper import scrape_reddit
from backend.jd_scraper.naukri_scraper import scrape_naukri

def get_job_description(url: str) -> str:
    try:
        if "linkedin.com" in url:
            return scrape_linkedin(url)
        elif "foundit.in" in url or "monsterindia.com" in url:
            return scrape_foundit(url)
        elif "reddit.com" in url:
            return scrape_reddit(url)
        elif "naukri.com" in url:
            return scrape_naukri(url)
        else:
            return "❌ Unsupported platform or scraping blocked. Please paste the JD manually."
    except Exception as e:
        return f"❌ Failed to fetch job description: {str(e)}"
