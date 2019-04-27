import bs4 as bs
import urllib.request

source = urllib.request.urlopen('http://www.city-data.com/accidents/acc-Cincinnati-Ohio.html').read()
soup = bs.BeautifulSoup(source,'lxml')
table = soup.find('table')
table_rows = table.find_all('tr')
print(table_rows)
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)


