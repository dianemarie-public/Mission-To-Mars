#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
# Define the 'classDB' database in Mongo
db = client.classDB


# In[3]:


# Setup splinter
executable_path = {'executable_path': 'C:/Users/diane/.wdm/drivers/chromedriver/win32/87.0.4280.88/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


# Scrape for Mars News text


# In[5]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[6]:


html = browser.html
soup = bs(html, 'html.parser')
slides = soup.find('li', class_='slide')
news_date = slides.find_all('div', class_='list_date')[0].text
news_title = slides.find_all('h3')[0].text
news_p = slides.find_all('div', class_='rollover_description_inner')[0].text
print(news_date)
print(news_title)
print(news_p)


# In[7]:


# Scrape for Mars featured image url


# In[8]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[9]:


html = browser.html
soup = bs(html, 'html.parser')
carousel = soup.find('article', class_='carousel_item')
featured_image_url = carousel.find('a').get('data-fancybox-href')
featured_image_url = 'https://www.jpl.nasa.gov/' + featured_image_url
print(featured_image_url)


# In[10]:


# Scrape for Mars facts table


# In[11]:


url = 'https://space-facts.com/mars/'


# In[12]:


tables = pd.read_html(url)
df = tables[0]
df.index.name = None
html_table = df.to_html()
df.to_html('static/mars_facts_table.html')
print(df)


# In[13]:


# Mars Hemisphere Images


# In[14]:


hemisphere_image_urls = []


# In[15]:


url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'


# In[16]:


browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')
title = soup.find('h2', class_='title').text
hemisphere_image_urls.append(title)
ul = soup.find('ul')
img_url = ul.find('a')['href']
hemisphere_image_urls.append(img_url)
print(hemisphere_image_urls)


# In[17]:


url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'


# In[18]:


browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')
title = soup.find('h2', class_='title').text
hemisphere_image_urls.append(title)
ul = soup.find('ul')
img_url = ul.find('a')['href']
hemisphere_image_urls.append(img_url)
print(hemisphere_image_urls)


# In[19]:


url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'


# In[20]:


browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')
title = soup.find('h2', class_='title').text
hemisphere_image_urls.append(title)
ul = soup.find('ul')
img_url = ul.find('a')['href']
hemisphere_image_urls.append(img_url)
print(hemisphere_image_urls)


# In[21]:


url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'


# In[22]:


browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')
title = soup.find('h2', class_='title').text
hemisphere_image_urls.append(title)
ul = soup.find('ul')
img_url = ul.find('a')['href']
hemisphere_image_urls.append(img_url)
print(hemisphere_image_urls)


# In[23]:


# Define a function to convert the list to a dictionary
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
         
# Driver code
print(Convert(hemisphere_image_urls))

