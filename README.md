# Remote Jobs Web Scraper

A Python + Selenium scraper that extracts remote job listings (title, company, 
date posted) from a job board — demonstrating structured data extraction via 
JSON-LD, plus real-world data cleaning to filter out incomplete or placeholder 
listings.

## Features
- Scrapes job listings using Selenium for dynamic content
- Extracts clean structured data from embedded JSON-LD (schema.org) markup
- Filters out incomplete/junk entries for reliable output
- Clean CSV export with Pandas

## Tech Stack
Python, Selenium, BeautifulSoup, JSON, Pandas

## Output
Delivers a clean CSV file with job title, company, and posting date.
