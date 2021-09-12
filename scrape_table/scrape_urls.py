from gazpacho import get, Soup
url = "https://tax.alaska.gov/programs/oil/production/ans.aspx?"
html = get(url)
soup = Soup(html)

months = []
years = []

# interactive test code
soup.find('option')[1:]

list = soup.find('option')[1:]
length = len(list)
length

# interactive test code
list[0].attrs['value']

options = []

# iterate over the reset_index same as 'for i in range(len(list))'
for i in range(length):
    option = list[i].attrs['value']
    url = "https://tax.alaska.gov/programs/oil/production/ans.aspx?"
    options.append(url + option)
    # print(option)
    # print(list[i].attrs['value'])

options
