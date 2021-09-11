import pandas as pd

url = "https://tax.alaska.gov/programs/oil/production/ans.aspx?9/1/2021"

tables = pd.read_html(url)
# tables
type(tables)

# tables[6]
df = tables[6]
# df.head()
df = df.loc[2:]
# df.head()
df = df.reset_index(drop=True)
# df.head()
# identify incomplete all_rows
# df.count()
del df[8]
del df[9]
del df[10]
del df[11]
del df[12]
# df.head()
# df.dtypes
# df[0]
# df.info()

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
