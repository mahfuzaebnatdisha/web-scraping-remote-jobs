from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://remoteok.com/")
time.sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")
jobs = soup.find_all("tr", class_="job")

junk_titles = ["job title", "classic", "your job description here"]

all_jobs = []

for job in jobs:
    script_tag = job.find("script", type="application/ld+json")
    if script_tag:
        try:
            data = json.loads(script_tag.string)
            title = data.get("title", "").strip()
            company = data.get("hiringOrganization", {}).get("name", "").strip()
            date_posted = data.get("datePosted", "")
            
            if (title and company and len(title) > 5 
                and title.lower() not in junk_titles
                and "your job" not in title.lower()):
                all_jobs.append({
                    "Title": title,
                    "Company": company,
                    "Date Posted": date_posted
                })
        except:
            pass

driver.quit()

df = pd.DataFrame(all_jobs)
df.to_csv("remote_jobs.csv", index=False)
print(f"{len(df)}টা job CSV-তে সেভ হয়েছে")
print(df.head())