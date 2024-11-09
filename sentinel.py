from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

# Your client credentials 
# DO NOT CHANGE, it has like 29k requests. Do not waste.
client_id = '<Insert Your ID here>'
client_secret = '<insert your secret here>'

# Create a session
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)

# Get token for the session
token = oauth.fetch_token(token_url='https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token',
                          client_secret=client_secret,
                          include_client_id=True)

#==============================================CHANGES BELOW THIS
evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["VV"],
    output: { id: "default", bands: 1 },
  }
}

function evaluatePixel(samples) {
  return [2 * samples.VV]
}
"""

request = {
    "input": {
        "bounds": {
            "bbox": [
                484696.51,
                5804631.34, 
                525751.04,
                5770703.56
            ],
            "properties": {"crs": "http://www.opengis.net/def/crs/EPSG/0/3857"},
        },
        "data": [
            {
                "type": "sentinel-1-grd",
                "dataFilter": {
                    "timeRange": {
                        "from": "2020-02-02T00:00:00Z",
                        "to": "2021-04-02T23:59:59Z",
                    }
                },
                "processing": {"orthorectify": "true"},
            }
        ],
    },
    "output": {
        "width": 2048,
        "height": 2048,
        "responses": [
            {
                "identifier": "default",
                "format": {"type": "image/png"},
            }
        ],
    },
    "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/api/v1/process"
response = oauth.post(url, json=request)
print("Headers:", response.headers)
# print("Content:", response.content)
filetype = response.headers['content-type'].split('/')[1]
print(response.status_code)
if response.status_code==200:
    img = response.raw.read()
    with open("image1."+filetype, mode='wb') as fp:
        fp.write(response.content)