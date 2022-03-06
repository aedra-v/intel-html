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

def firestore_delta(event, context):
    """Triggered by a change to a Firestore document.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    resource_string = context.resource
    json_object = json.dumps(event["value"])
    # print out the resource string that triggered the function
    print(f"Function triggered by change to: {json_object}.")
    # now print out the entire event object
    print(str(event))
