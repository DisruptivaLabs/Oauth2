from bottle import route, run, redirect, request
import json
import requests
from config import *

@route('/oauth2/login')
def login():
    querystring = "response_type=code&client_id="+CLIENT_ID+"&redirect_uri="+REDIRECT_URI

    redirect(URL_AUTHORIZATION+querystring)

@route('/oauth2/callback')
def callback():
    acessCode = request.query.get('code')
    
    getToken(acessCode)

def getToken(code):
    payload = {
                    "grant_type":"authorization_code",
                    "client_id":CLIENT_ID,
                    "client_secret":CLIENT_SECRET,
                    "redirect_uri":REDIRECT_URI,
                    "code":code
                  }

    headers = {
                'content-type': 'application/json'
              }

    response = requests.request("POST", URL_GET_TOKEN, data=json.dumps(payload), headers=headers)

    retorno = json.loads(response.text)

    token = retorno['access_token']

    print(token)

run(host='localhost', port=8000)
