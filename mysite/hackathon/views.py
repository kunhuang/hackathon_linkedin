from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
    url = 'https://www.linkedin.com/uas/oauth2/accessToken'
    payload = {'grant_type': 'authorization_code',
               'code': request.GET['code'],
               'redirect_uri': 'http://localhost:8000/hackathon/test',
               'scope': 'r_fullprofile',
               'client_id': '75rlqt9xns8nr4',
               'client_secret': 'U1Ogc52WYwIuTuBn'}
    r = requests.get(url, params=payload)

    url = 'https://api.linkedin.com/v1/people/url={https%3A%2F%2Fwww.linkedin.com%2Fin%2Fvyasbhairavi}:(first-name,last-name,headline,picture-url,id,skills)?format=json'
    headers = {'content-type': 'application/json'}
    payload = {'oauth2_access_token' : json.loads(r.content)['access_token']}
    r = requests.get(url, params=payload, headers=headers)

    return HttpResponse(r)