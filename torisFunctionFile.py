from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import sys

# Client credentials (preserve existing tokens to avoid extra requests)
client_id = '<Insert your secret here>'
client_secret = '<insert your secret here>'

# Create a session
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)

cities = {"Warsaw" : [20.775113, 52.391717, 21.375827, 52.086301], "Vilnius" : [24.939876, 54.872075, 25.599055, 54.555552]}

def getPicture(city, start, end):
    print(cities['Vilnius'])
    return cities['Vilnius']
    
def main():
    print(cities['Vilnius'])