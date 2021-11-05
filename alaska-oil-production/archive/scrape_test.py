# scraping information from websites using pandas and gazpacho https://pypi.org/project/gazpacho/

# finding date (in month and years) options for our data to use in custom url (will need to loop through pages to extract all available data, tbd...)

from gazpacho import get, Soup
url = "https://tax.alaska.gov/programs/oil/production/ans.aspx?"
html = get(url)
soup = Soup(html)
# soup

date_list = soup.find('option')[1:]
type(date_list)
len(date_list)

date_list[0]
date_list[0].find('option')
date_list[0].find('option').attrs
date_list[0].find('option').attrs['value']

date_list = date_list[0:]
# date_list

count = len(date_list)
count
count = count - 1
print(count)

date_list[count].attrs['value']
oldest = date_list[count].attrs['value']
oldest

date_list[0].find('option').attrs['value']
newest = date_list[0].find('option').attrs['value']
newest
newest = str(newest)
newest

url = 'https://tax.alaska.gov/programs/oil/production/ans.aspx?'
url + newest

# insert a loop for the the urls in scrape_urls.py


# using the url combo found above, setting the pd.read_html(url) to extract the table data below
import pandas as pd

url = url + newest
url
type(url)

# start for loop here: 'for url in urls:' then indent below to END
tables = pd.read_html(url)
type(tables)
tables[6]
df = tables[6]
df = df.loc[2:]
df = df.reset_index(drop=True)

# delete extra columns
del df[8]
del df[9]
del df[10]
del df[11]
del df[12]

# rename columns (for Alaska North Slope oil field names)
df = df.rename(columns = {0:'date', 1:'prudhoe', 2:'kaparuk', 3:'endicott', 4:'lisburne', 5:'alpine', 6:'ans', 7:'inventories'})
df.columns

# convert strings of html data to numeric (float)
df['prudhoe'] = pd.to_numeric(df['prudhoe'],errors='coerce')
df['kaparuk'] = pd.to_numeric(df['kaparuk'],errors='coerce')
df['endicott'] = pd.to_numeric(df['endicott'],errors='coerce')
df['lisburne'] = pd.to_numeric(df['lisburne'],errors='coerce')
df['alpine'] = pd.to_numeric(df['alpine'],errors='coerce')
df['ans'] = pd.to_numeric(df['ans'],errors='coerce')
df['inventories'] = pd.to_numeric(df['inventories'],errors='coerce')

# drop any rows with NaN
df = df.dropna(how='any')
# END
df
# scraping information from websites using pandas and gazpacho https://pypi.org/project/gazpacho/

# finding date (in month and years) options for our data to use in custom url (will need to loop through pages to extract all available data, tbd...)

from gazpacho import get, Soup
url = "https://tax.alaska.gov/programs/oil/production/ans.aspx?"
html = get(url)
soup = Soup(html)
# soup

date_list = soup.find('option')[1:]
type(date_list)
len(date_list)

date_list[0]
date_list[0].find('option')
date_list[0].find('option').attrs
date_list[0].find('option').attrs['value']

date_list = date_list[0:]
# date_list

count = len(date_list)
count
count = count - 1
print(count)

date_list[count].attrs['value']
oldest = date_list[count].attrs['value']
oldest

date_list[0].find('option').attrs['value']
newest = date_list[0].find('option').attrs['value']
newest
newest = str(newest)
newest

url = 'https://tax.alaska.gov/programs/oil/production/ans.aspx?'
url + newest

# insert a loop for the the urls in scrape_urls.py


# using the url combo found above, setting the pd.read_html(url) to extract the table data below
import pandas as pd

url = url + newest
url
type(url)

tables = pd.read_html(url)
type(tables)
tables[6]
df = tables[6]
df = df.loc[2:]
df = df.reset_index(drop=True)

# delete extra columns
del df[8]
del df[9]
del df[10]
del df[11]
del df[12]

# rename columns (for Alaska North Slope oil field names)
df = df.rename(columns = {0:'date', 1:'prudhoe', 2:'kaparuk', 3:'endicott', 4:'lisburne', 5:'alpine', 6:'ans', 7:'inventories'})
df.columns

# convert strings of html data to numeric (float)
df['prudhoe'] = pd.to_numeric(df['prudhoe'],errors='coerce')
df['kaparuk'] = pd.to_numeric(df['kaparuk'],errors='coerce')
df['endicott'] = pd.to_numeric(df['endicott'],errors='coerce')
df['lisburne'] = pd.to_numeric(df['lisburne'],errors='coerce')
df['alpine'] = pd.to_numeric(df['alpine'],errors='coerce')
df['ans'] = pd.to_numeric(df['ans'],errors='coerce')
df['inventories'] = pd.to_numeric(df['inventories'],errors='coerce')

# drop any rows with NaN
df = df.dropna(how='any')
df
