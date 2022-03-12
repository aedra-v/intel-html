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
import pandas as pd
from beautifulsoup4 import BeautifulSoup

def parse_throne(event, context):
    resource_string = context.resource
    trigger_docid = resource_string.split('/')[-1]
    print(f"Function triggered by change to: {resource_string}.")
    print(str(event))

    importhtml = event['value']['fields']['importhtml']['stringValue']
    print(importhtml)

    inteltable = pd.read_html(importhtml)
    testvalue = inteltable[0][0].iloc[1]
    print('pre-testvalue')
    print(testvalue)

    soup = BeautifulSoup(importhtml, 'html.parser')
    testvalue2 = soup.find_all('h2')[2].br.next_element.split('(')[0].strip()
    print('pre-testvalue2')
    print(testvalue2)

    return f'Success'
