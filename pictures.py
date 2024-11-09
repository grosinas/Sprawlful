from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import sys
from sentinel2 import generateImage

# Client credentials (preserve existing tokens to avoid extra requests)
client_id = 'sh-b203c513-8741-4360-b982-e4ac316c9f9f'
client_secret = 'Tq07v2FnohSm9PucuklZqRu2IPoBMt66'

# Create a session
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)

# Generate token for session
token = oauth.fetch_token(
    token_url='https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token',
    client_secret=client_secret,
    include_client_id=True
)

cities = {"Warsaw" : [20.775113, 52.391717, 21.375827, 52.086301], "Vilnius" : [24.939876, 54.872075, 25.599055, 54.555552]}

def getPicture(city, start, end):
    # Get coordinates for city from dictionary
    coordinates = cities[city]
    
    # for each year in the range generate image (using sentinel2 data)
    # and radar data (using sentinel1GND data)
    for year in range(start, end+1):
        generateImage(city, coordinates, year, oauth)
        
