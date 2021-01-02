# From Unit 12 Week 3 Activity 09 Ins_Scrape_And_Render file: scrape_craigslist.py

# Import module used to connect Python with MongoDb
import pymongo
# Import BeautifulSoup
from bs4 import BeautifulSoup as bs
# Import Requests module
import requests
# Import splinter
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
# Import Pandas
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/Users/diane/.wdm/drivers/chromedriver/win32/87.0.4280.88/chromedriver"}
    # C:\Users\diane\.wdm\drivers\chromedriver\win32\87.0.4280.88\chromedriver
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    news_list = {}

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    news_list["news_title"] = soup.find("h3", class_="result-title").get_text()
    news_list["news_p"] = soup.find("div", class_="rollover_description_inner").get_text()

    return news_list