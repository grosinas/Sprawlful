### Python virtual environments
Use a virtual environment (venv) or you will break your python install at some point.
>`pip install venv`

>`python -m venv env`

>`source env/bin/activate` for *sh on Linux (and Mac, I guess)
>`./env/Scripts/Activate.ps1` for Powershell on Windows
>`./env/Scripts/activate.bat` for CMD on Windows

>`pip install -r requirements.txt`

Use `pip freeze > requirements.txt` to generate a new `requirements.txt` file if you add more dependencies and decide to commit them for others.

>Run `deactivate` to exit the venv.

<br><hr><br>

### API Key
The oauth client contains an API key. Do not change it, it gives you access to all the APIs on https://dataspace.copernicus.eu.
Limit is about 29k ish requests. Do not do stupid loops with requests in it.

### WTF is this image

For the image, I am stll not sure what is being returned. 
I used https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Process/Examples/S2L1C.html#true-color. It is supposed to be Helsinki Metropolitan Area. The `evalscript` determines what calculations the API runs before returning data. The evaluatePixel function returns a 3 channel array of pixels (RGB i think, so you can modify colours if you need, but its unnecessary I think). 

It would be really nice if we could get the image pulling for Helsinki working, then we can say that we got something from an satellite image API, rather than screenshotting Google Maps. 

### This does not work, what are we submitting?

The metrics for the calculation of WUP (ref. Section 2 of https://www.eea.europa.eu/publications/urban-sprawl-in-europe) for ONLY HELSINKI (for now), may be obtained from web sources, and road density and the elevation metric (Relief energy) (and maybe more, ref Axel's notes, the ones with the satellite drawn next to them) can be obtained from running image processing on the map image, but for the purpose of the demo/presentation/pitch, it may be hand calculated. Table 2.2 lists the variables.

### Want to change ideas on Saturday

Feel free to switch it up as you like, I am not there so I don't get to complain about it. All the best!