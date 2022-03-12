from google.cloud import storage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd

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
          'epoch': event['value']['fields']['epoch']['doubleValue'],
          'inteltype': event['value']['fields']['inteltype']['stringValue'],
          'importhtml': event['value']['fields']['data_html']['stringValue']
     }

     importintel = firestore.client().collection(routedcollection)
     intelligence = importintel.document()
     intelligence.set(intelfields)

     return f'Success'
