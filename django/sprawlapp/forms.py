from django import forms

CITY_CHOICES = [
    ('Warsaw','Warsaw'),
    ('Vilnius','Vilnius'),
]

YEAR_CHOICES = [
    ('2018','2018'),
    ('2019','2019'),
    ('2020','2020'),
    ('2021','2021'),
    ('2022','2022'),
    ('2023','2023'),
]

class FindSprawlForm(forms.Form):
    city = forms.CharField(label='Choose a city', widget=forms.Select(choices=CITY_CHOICES))
    start = forms.CharField(label='Choose a start year', widget=forms.Select(choices=YEAR_CHOICES))
    end = forms.CharField(label='Choose an end year', widget=forms.Select(choices=YEAR_CHOICES))

