# This project aims to leverage web scraping techniques to autonomously retrieve prices and other pertinent information from Zillow. 
# I will apply my knowledge of Selenium and BeautifulSoup to accomplish this task effectively.

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfVLwzXMmKTAM4pfwGL0PM_4E1o6jGXke3s0jJnC-iHbdV2zQ/viewform?usp=sf_link"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

#Using BeautifulSoup/Request to scrape all listings from Zillow-Clone
response = requests.get(ZILLOW_URL)
website_html = response.text
soup = BeautifulSoup(website_html, "lxml")

#Creating lists to store each text properly
listings = []
prices = []
addresses = []

#Housing links
housing_listing =  soup.find_all("a",{"class":"StyledPropertyCardDataArea-anchor"})
for link in housing_listing:
    listings.append(link.get('href').strip())

#Housing Prices
housing_prices = soup.find_all("span",{"class": "PropertyCardWrapper__StyledPriceLine"})
for price in housing_prices:
    formatted_price = price.get_text().strip() 
    price_without_plus = formatted_price.split('+')[0].strip()
    clean_price = price_without_plus.split('/')[0].strip()
    prices.append(clean_price)

#Housing Address
housing_address = soup.find_all("a",{"class":"StyledPropertyCardDataArea-anchor"})
for address in housing_address:
    h_address = address.get_text().strip()
    clean_address= h_address.split("|")[0].strip()
    addresses.append(clean_address)



#Using Selenium to automatically fill this google form with data achieved from houses
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#Input each box with proper item and submit the page
for i in range(len(listings)):
    driver.get(GOOGLE_FORM)

    time.sleep(2)

    address_input = driver.find_element(by=By.XPATH, 
                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(by=By.XPATH, 
                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    listing_input = driver.find_element(by=By.XPATH, 
                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    
    address_input.send_keys(addresses[i])
    price_input.send_keys(prices[i])
    listing_input.send_keys(listings[i])
    submit_button.click()