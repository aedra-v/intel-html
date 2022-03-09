from flask import Flask
from flask import request
from flask import jsonify
from google.cloud import storage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
import json
import sys
import timeit
from datetime import datetime
import pandas

firebase_admin.initialize_app()

def firestore_delta(event, context):
     resource_string = 'projects/artaeum-py/databases/(default)/documents/intel-dump/ESeAD6qvs5u3iS9IoxLY'
     inteldumpUID = resource_string.split('/')[-1]
     event.update({"inteldump UID": inteldumpUID})

     importurlstring = event['value']['fields']['url']['stringValue']
     importurlUID = importurlstring[33:]
     event.update({"Intel Type": importurlUID})
     
     event.pop('oldValue')
     event.pop('updateMask')

     importintel = firestore.client().collection('d-prov')
     intelligence = importintel.document()
     intelligence.set(event)

     return f'Success'
