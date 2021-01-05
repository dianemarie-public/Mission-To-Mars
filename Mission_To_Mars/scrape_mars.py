from bs4 import BeautifulSoup as bs
from splinter import Browser
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'C:/Users/diane/.wdm/drivers/chromedriver/win32/87.0.4280.88/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    mars = {}
    
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    slides = soup.find('li', class_='slide')

    news_date = slides.find_all('div', class_='list_date')[0].get_text()

    news_title = slides.find_all('h3')[0].get_text()
    
    news_p = slides.find_all('div', class_='rollover_description_inner')[0].get_text()

    # Store data in a dictionary
    news_data = {
        "news_date": news_date,
        "news_title": news_title,
        "news_p": news_p
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return news_data
    
