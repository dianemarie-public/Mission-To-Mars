from gazpacho import get, Soup
url = "https://tax.alaska.gov/programs/oil/production/ans.aspx?"
html = get(url)
soup = Soup(html)

list = soup.find('option')[1:]
length = len(list)

# base_url = "https://tax.alaska.gov/programs/oil/production/ans.aspx?"
urls = []

for i in range(length):
    options = list[i].attrs['value']
    urls.append(url + options)

len(urls)

import pandas as pd

data = []

# df = df.rename(columns = {0:'date', 1:'prudhoe', 2:'kaparuk', 3:'endicott', 4:'lisburne', 5:'alpine', 6:'ans', 7:'inventories'})
# df.columns
# df.reset_index()

for url in urls:
    df = pd.read_html(url)[6]
    df = df.loc[2:]
    df[1] = pd.to_numeric(df[1],errors='coerce')
    df[2] = pd.to_numeric(df[2],errors='coerce')
    df[3] = pd.to_numeric(df[3],errors='coerce')
    df[4] = pd.to_numeric(df[4],errors='coerce')
    df[5] = pd.to_numeric(df[5],errors='coerce')
    df[6] = pd.to_numeric(df[6],errors='coerce')
    df[7] = pd.to_numeric(df[7],errors='coerce')
    del df[8]
    del df[9]
    del df[10]
    del df[11]
    del df[12]
    df = df.dropna(how='any')
    df = df[df[0] != 'Average']
    df.to_csv('pandas.csv', mode='a', header=False, index=False)
