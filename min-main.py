#The Flask request object contains the data that the client (eg a browser) has sent to your app - ie the URL parameters, any POST data, etc.
from flask import request 

#The requests library is for your app to make HTTP request to other sites, usually APIs. It makes an outgoing request and returns the response from the external site.
import requests 


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
