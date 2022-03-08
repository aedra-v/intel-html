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
     print(resource_string)

     importurl_list = (event['value']['fields']['url'])
     print(importurl_list)
     importurl_UID = (importurl_list.split("/")[-1]
     print(importurl_UID)

     importintel = firestore.client().collection('d-prov')
     intelligence = importintel.document()
     intelligence.set(event)

     return f'Success'
