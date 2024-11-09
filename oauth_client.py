from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

# Your client credentials 
# DO NOT CHANGE, it has like 29k requests. Do not waste.
client_id = '<Your id here>'
client_secret = '<Your secret here>'

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
    input: ["B02", "B03", "B04"],
    output: {
      bands: 3,
      sampleType: "AUTO", // default value - scales the output values from [0,1] to [0,255].
    },
  }
}

function evaluatePixel(sample) {
  return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02]
}
"""

request = {
    "input": {
        "bounds": {
            "properties": {"crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"},
            "bbox": [
                60.31358333, 24.47819444, #helsinki metropolitan area bounding box
                60.15502778, 25.28138889,
            ],
        },
        "data": [
            {
                "type": "sentinel-2-l1c",
                "dataFilter": {
                    "timeRange": {
                        "from": "2023-11-01T00:00:00Z", #mess with these dates.
                        "to": "2023-11-20T00:00:00Z",
                    }
                },
            }
        ],
    },
    "output": {
        "width": 1024,
        "height": 1024,
    },
    "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/api/v1/process"
response = oauth.post(url, json=request)
print("Headers:", response.headers)
# print("Content:", response.content)
filetype = response.headers['content-type'].split('/')[1]
if response.status_code==200:
    img = response.raw.read()
    with open("image."+filetype, mode='wb') as fp:
        fp.write(response.content)
