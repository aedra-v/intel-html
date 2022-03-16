from bs4 import BeautifulSoup
import pandas as pd
import firebase_admin
from google.cloud import storage
from firebase_admin import credentials
from firebase_admin import firestore

firebase_admin.initialize_app()
db = firestore.client().collection('intel').document('kdsync').collection('prov')

def parse_wizards(event, context):
    resource_string = context.resource
    triggerdocid = resource_string.split('/')[-1]
    sourceurl = event['value']['fields']['sourceurl']['stringValue']

    importhtml = event['value']['fields']['importhtml']['stringValue']
    soup = BeautifulSoup(importhtml, 'html.parser')
    inteltable = pd.read_html(importhtml)

    importdict = {
      'sourcedoc': triggerdocid,
      'sourceurl': sourceurl,
      inteltable[0][0].iloc[0]: inteltable[0][1].iloc[0],
      inteltable[0][0].iloc[1]: inteltable[0][1].iloc[1],
      inteltable[0][2].iloc[0]: inteltable[0][3].iloc[0].split(' ')[0],
      'wpa': inteltable[0][3].iloc[0].split(' ')[1][1:]
    }
    
    print(importdict)
    
    importintel = db.document('aedra')
    intelligence.update(importdict)

    return f'Success'
