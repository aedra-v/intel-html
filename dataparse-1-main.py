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
     resource_string = context.resource
     
     a1 = str(event()[5])
     a2 = a1.split("/")
     v1 = a2[-1]
     print(v1)
     
     json_object = json.dumps(event["value"], indent = 4)
     json_string = json.loads(json_object)
     importintel = firestore.client().collection('d-prov')
     intelligence = importintel.document()
     intelligence.set(json_string)

     return f'Success'
