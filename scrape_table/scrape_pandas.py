import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

url = "https://tax.alaska.gov/programs/oil/production/ans.aspx?"
month = '1'
month
year = '2021'
year
day = '1'

url = url + str(month) + '/' + str(day) + '/' + str(year)
url
# -----------------------------
# set the url for the most recent page update
# url = "https://tax.alaska.gov/programs/oil/production/ans.aspx?9/1/2021"
tables = pd.read_html(url)
type(tables)
df = tables[6]
df = df.loc[2:]
df = df.reset_index(drop=True)


del df[8]
del df[9]
del df[10]
del df[11]
del df[12]

df = df.rename(columns = {0:'date', 1:'prudhoe', 2:'kaparuk', 3:'endicott', 4:'lisburne', 5:'alpine', 6:'ans', 7:'inventories'})
df.columns
# df.head()
df['prudhoe'].dtype
df['prudhoe'] = pd.to_numeric(df['prudhoe'],errors='coerce')
df['kaparuk'] = pd.to_numeric(df['kaparuk'],errors='coerce')
df['endicott'] = pd.to_numeric(df['endicott'],errors='coerce')
df['lisburne'] = pd.to_numeric(df['lisburne'],errors='coerce')
df['alpine'] = pd.to_numeric(df['alpine'],errors='coerce')
df['ans'] = pd.to_numeric(df['ans'],errors='coerce')
df['inventories'] = pd.to_numeric(df['inventories'],errors='coerce')
# df.head()
# df
df = df.dropna(how='any')
df
