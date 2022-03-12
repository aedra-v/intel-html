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

def parse_throne(event, context):
    resource_string = context.resource
    trigger_docid = resource_string.split('/')[-1]
    print(f"Function triggered by change to: {resource_string}.")
    print(str(event))

    importhtml = event['value']['fields']['importhtml']['stringValue']
    print(str(importhtml))

    inteltable = pd.read_html(importhtml)
    print(str(inteltable))

    soup = BeautifulSoup(importhtml, 'html.parser')
    print(soup)

    return f'Success'
