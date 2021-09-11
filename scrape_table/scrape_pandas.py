import pandas as pd

# found earliest data available (should scrape from dropdown menu link below)
url = 'https://tax.alaska.gov/programs/oil/production.aspx?'
month = '1'
month
year = '2002'
year
day = '1'
start_url = url + str(month) + '/' + str(day) + '/' + str(year)
start_url

# -----------------------------
# set the url for the most recent page update
end_url = "https://tax.alaska.gov/programs/oil/production/ans.aspx?9/1/2021"
tables = pd.read_html(end_url)
type(tables)
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

# Next steps: write a loop to loop through all the webpages by month and year, then we can scrape and append each into a dataframe and export it
