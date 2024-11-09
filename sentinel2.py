from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import os

evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["B02", "B03", "B04"],
    output: {
      bands: 3,
      sampleType: "AUTO", // scales to [0,255]
    },
  }
}

function evaluatePixel(sample) {
  return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02];
}
"""
import os

# Ensure the 'images' folder exists
os.makedirs('images', exist_ok=True)

def generateImage(city, coordinates, year, oauth):

# Define the request payload
    request = {
        "input": {
            "bounds": {
                "properties": {"crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"},
                "bbox": coordinates,

            },
            "data": [
                {
                    "type": "sentinel-2-l1c",
                    "dataFilter": {
                        "timeRange": {
                            "from": f"{year}-01-01T00:00:00Z",
                            "to": f"{year}-12-31T23:59:59Z",
                        },
                        "maxCloudCoverage": 0  # Optional: Use a low cloud coverage percentage
                    },
                }
            ],
        },
        "output": {
            "width": 2048,
            "height": 2048,
        },
        "evalscript": evalscript,
    }

    # Send the request
    url = "https://sh.dataspace.copernicus.eu/api/v1/process"
    response = oauth.post(url, json=request)

    # Process the response
    print("Headers:", response.headers)
    filetype = response.headers['content-type'].split('/')[1]
    if response.status_code == 200:
        with open(f'images/{city}_image_{year}.' + filetype, mode='wb') as fp:
            fp.write(response.content)
        print(f"Image saved as {city}_image_{year}." + filetype)
    else:
        print("Error:", response.status_code, response.text)
            