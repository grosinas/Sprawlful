#### MyFutureCity
MyFutureCity is the future city planning app which uses satellite images and radar data to track (and in the future - predict) urban sprawl.

### Generating Sentinel Tokens uwu
I bet you really want to try our very cool tool!!! 
Well... you can!!!! (ish)

To play around with satellite image generation you can use our web app, follow the instructions below.



### Python virtual environments
Use a virtual environment (venv) or you will break your python install at some point.
>`pip install virtualenv`

>`python -m venv env`

>`source env/bin/activate` for *sh on Linux (and Mac, I guess)
>`./env/Scripts/Activate.ps1` for Powershell on Windows
>`./env/Scripts/activate.bat` for CMD on Windows

>`pip install -r requirements.txt`

Use `pip freeze > requirements.txt` to generate a new `requirements.txt` file if you add more dependencies and decide to commit them for others.

>Run `deactivate` to exit the venv.

<br><hr><br>

### Running Django
Pretty straightforward, run this command in the django directory. If it dosen't work talk to me:
```
python manage.py runserver
```

### API Key
The oauth client contains an API key. Do not change it, it gives you access to all the APIs on https://dataspace.copernicus.eu.
Limit is about 29k ish requests. Do not do stupid loops with requests in it.

Set the client-id and secret into the client-id and secret variables in django/sprawlapp/pictures.py (or in any other file where you find the fields ;) let's call them easter eggs...)