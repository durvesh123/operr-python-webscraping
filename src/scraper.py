import urllib.request
from bs4 import BeautifulSoup
import pandas as pd


webpage="http://www.city-data.com/accidents/acc-Cincinnati-Ohio.html"
page = urllib.request.urlopen(webpage)
soup = BeautifulSoup(page)
fatal_car_crashes = pd.DataFrame(columns = ['YEAR', 'TYPE','COUNT'])

for li in soup.find_all("li", class_="list-group-item active"):
    print(li.contents)

for b in soup.find_all("b"):
    print(b.contents)

for s in soup.find_all("span", class_="badge"):
    print(s.contents)

fatal_car_crashes.YEAR = [2016,2016,2016,2016,2016,2016,2017,2017,2017,2017,2017,2017]
fatal_car_crashes.TYPE = ['Fatal accident count',
'Vehicles involved in fatal accidents',
'Fatal accidents involving drunken persons',
'Fatalities',
'Persons involved in fatal accidents',
'Pedestrians involved in fatal accidents',
'Fatal accident count',
'Vehicles involved in fatal accidents',
'Fatal accidents involving drunken persons',
'Fatalities',
'Persons involved in fatal accidents',
'Pedestrians involved in fatal accidents']
fatal_car_crashes.COUNT=['22',
'38',
'7',
'26',
'47',
'7',
'31',
'50',
'11',
'31',
'56',
'8',
]

print(fatal_car_crashes)



