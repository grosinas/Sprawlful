from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from coordinating import coordinating 
import os

def getRadar(city, coordinates, year, oauth): 
    """
        Get radar images from Sentinel 1 GRD. Coordinates are passed to appropriate format. 
    """
    os.makedirs('radars', exist_ok=True)

    evalscript = """
    //VERSION=3
    function setup() {
    return {
        input: ["VV", "VH", "dataMask"],
        output: { id: "default", bands: 4 },
    }
    }

    function evaluatePixel(samples) {
    return [5.5 * samples.VH > 0.5, samples.VV, samples.VH *8, samples.dataMask]
    }
    """
    bbox = [0, 0, 0, 0]
    bbox[0], bbox[1] = coordinating([coordinates[0], coordinates[1]])
    bbox[2], bbox[3] = coordinating([coordinates[2], coordinates[3]])

    request = {
        "input": {
            "bounds": {
                "bbox": bbox,
                "properties": {"crs": "http://www.opengis.net/def/crs/EPSG/0/3857"},
            },
            "data": [
                {
                    "type": "sentinel-1-grd",
                    "dataFilter": {
                        "timeRange": {
                            "from": f"{year}-01-01T00:00:00Z",
                            "to": f"{year}-12-31T23:59:59Z",
                        }
                    },
                    "processing": {"orthorectify": "true"},
                }
            ],
        },
        "output": {
            "width": 1024,
            "height": 1024,
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
    if response.status_code==200:
        img = response.raw.read()
        with open(f"radars/{city}_radar_{year}."+filetype, mode='wb') as fp:
            fp.write(response.content)