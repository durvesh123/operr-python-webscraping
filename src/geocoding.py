import requests
import pandas as pd


def getnycdata():
    url = 'https://data.cityofnewyork.us/resource/9wgk-ev5c.json'
    collisions = pd.read_json(url).fillna(" ")
    collisions["address"] = collisions["house_number"].map(str) + collisions["intersecting_street"].map(str) + collisions["street_name"].map(str)
    address = []
    address.append(collisions['address'].tolist())
    return address

def getgeocoding():

    KEY = ""
    GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json&key={}'.format(KEY)

    address = getnycdata()
    for i in address:
        PARAMS={
            'address': i
        }
        r = requests.get(url=GOOGLE_MAPS_API_URL, params=PARAMS)
        data = r.json()
        latitude = data['results'][0]['geometry']['location']['lat']
        longitude = data['results'][0]['geometry']['location']['lng']
        formatted_address = data['results'][0]['formatted_address']
        print("{} {} {}".format(latitude,longitude,formatted_address))




getgeocoding()