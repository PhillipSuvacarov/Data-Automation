# Overview
This project leverages web scraping techniques to autonomously retrieve housing prices, addresses, and listing links from Zillow. The extracted data is then automatically submitted to a Google Form. The project uses BeautifulSoup and Selenium to achieve this functionality.

# Features
Scrapes housing listings from Zillow-Clone using BeautifulSoup

Extracts housing prices, addresses, and links

Uses Selenium to automate data entry into a Google Form

Runs in an automated loop to process multiple listings
# Technologies Used
Python

BeautifulSoup for parsing HTML

Requests for fetching webpage content

Selenium for browser automation (Google Form submission)

Chrome WebDriver for Selenium automation
# Installation
Prerequisites
Python 3.x installed

Google Chrome browser installed

Chrome WebDriver installed (matching your Chrome version)

Install dependencies using:

pip install requests beautifulsoup4 selenium lxml

# Usage
Clone the repository:

git clone https://github.com/yourusername/Data-Automation.git

cd your-repo

Update the GOOGLE_FORM and ZILLOW_URL if needed

Run the script:

python script_name.py



