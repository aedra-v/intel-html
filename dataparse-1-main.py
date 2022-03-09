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
     print(event)
     routedcollection = event['value']['fields']['inteltype']['stringValue'].replace("_", "")
     print(routedcollection)
     importintel = firestore.client().collection(routedcollection)
     intelligence = importintel.document()
     intelligence.set(event)

     return f'Success'
