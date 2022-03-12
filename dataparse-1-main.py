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

def firestore_route(event, context):
     resource_string = context.resource
     trigger_docid = resource_string.split('/')[-1]
     print(trigger_docid)
     print(event)

     routedcollection = event['value']['fields']['inteltype']['stringValue'].replace("_", "")
     print(routedcollection)

     intelfields = {
          'sourcedoc': trigger_docid,
          'epoch': event['value']['fields']['epoch'],
          'inteltype': event['value']['fields']['inteltype'],
          'importhtml': event['value']['fields']['data_html']['stringValue']
     }

     importintel = firestore.client().collection(routedcollection)
     intelligence = importintel.document()
     intelligence.set(intelfields)

     return f'Success'
