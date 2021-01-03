from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import time

# Test GitHub Push
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'C:/Users/diane/.wdm/drivers/chromedriver/win32/87.0.4280.88/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

# Initiate browser
def scrape_info():
    browser = init_browser()
    
    # Visit the website
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    # ?
    time.sleep(1)
    
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the slides
    slides = soup.find('li', class_='slide')

    # Get the news date
    news_date = slides.find_all('div', class_='list_date')[0].text
    
    # Get the news title
    news_title = slides.find_all('h3')[0].text
    
    # Get the news paragraph
    news_p = slides.find_all('div', class_='rollover_description_inner')[0].text

    # Store data in dictionary
    news_data = {
        "date": news_date,
        "title": news_title,
        "paragraph": news_p
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return news_data
    
