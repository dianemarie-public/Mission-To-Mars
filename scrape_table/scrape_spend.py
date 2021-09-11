from gazpacho  import get, Soup

url = "https://scrape.world/spend"

get(url)
html = get(url)

Soup(html)
soup = Soup(html)

# soup.find('tr', {'class': "tmx"}, partial=True)
trs = soup.find('tr', {'class': "tmx"}, partial=True)
type(trs)

# trs[0]
tr = trs[0]

tr.find('td', {'data-label': "TEAM"}, partial=True).text
name = tr.find('td', {'data-label': "TEAM"}, partial=True).text
type(name)
# find text of data-label
tr.find('td', {"data-label": "TODAYS CAP HIT"}).text
# replace , with blank
tr.find('td', {"data-label": "TODAYS CAP HIT"}).text.replace(',','')
# replace $ with blank
tr.find('td', {"data-label": "TODAYS CAP HIT"}).text.replace(',','').replace('$','')
# wrap in float
float(tr.find('td', {"data-label": "TODAYS CAP HIT"}).text.replace(',','').replace('$',''))
# create a variable for the spend of the team
spend = float(tr.find('td', {"data-label": "TODAYS CAP HIT"}).text.replace(',','').replace('$',''))
type(spend)
# create a function
def parse_tr(tr):
    name = tr.find('td', {'data-label': "TEAM"}, partial=True).text
    spend = float(tr.find('td', {"data-label": "TODAYS CAP HIT"}).text.replace(',','').replace('$',''))
    return name, spend

parse_tr(tr)

[tr for tr in trs]

import pandas as pd

[parse_tr(tr) for tr in trs]
data = [parse_tr(tr) for tr in trs]
pd.DataFrame(data, columns=['team', 'salary_cap'])
