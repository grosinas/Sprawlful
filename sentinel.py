from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

# Your client credentials 
# DO NOT CHANGE, it has like 29k requests. Do not waste.
client_id = '0e34822b-7026-4e20-b9eb-b520345c45d1'
client_secret = 'LcWLJDaUnnVfy8aJNT91EeMmfCAhd8KU'

# Create a session
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)

# Get token for the session
token = oauth.fetch_token(token_url='https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token',
                          client_secret=client_secret, include_client_id=True)



#==============================================CHANGES BELOW THIS
evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["VV"],
    output: {
      bands: 1,
      sampleType: "AUTO", // default value - scales the output values from [0,1] to [0,255].
    },
  }
}

function evaluatePixel(sample) {
  return [2 * sample.VV]
}
"""

request = {
    "input": {
        "bounds": {
            "properties": {"crs": "http://www.opengis.net/def/crs/EPSG/0/32633" },
            "bbox": [ 
                20.775113, 
                52.391717,  
                21.375827, 
                52.086301, 
            ],
        },
        "data": [{
                "type": "sentinel-1-grd",
                "dataFilter": {
                    "timeRange": {
                        "from": "2022-11-01T00:00:00Z", #mess with these dates.
                        "to": "2022-11-20T00:00:00Z",
                    },
                    "resolution": "HIGH",
                    "acquisitionMode": "IW"
            },
            "processing": {
                "orthorectify": "true",
                "demInstance": "COPERNICUS_30"
            },
        }
],
    },
    "output": {
        "resx": 10,
        "resy": 10,
        "responses": [{
            "identifier": "default",
            "format": {
                "type": "image/png"
            }
        }]
    },
    "evalscript": evalscript,
}

url = "https://services.sentinel-hub.com/api/v1/process"
response = oauth.post(url, json=request)
print("Headers:", response.headers)
# print("Content:", response.content)
filetype = response.headers['content-type'].split('/')[1]
print(response.status_code)
if response.status_code==200:
    img = response.raw.read()
    with open("image1."+filetype, mode='wb') as fp:
        fp.write(response.content)