# 
# scripts/test_jd_scraper.py
from backend.jd_scraper.scraper import get_job_description

url = "https://www.naukri.com/job-listings-data-analyst-abc-tech-delhi-123456789"
jd = get_job_description(url)

print("\n📄 Job Description:\n")
print(jd)
