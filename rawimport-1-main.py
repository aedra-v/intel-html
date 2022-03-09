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
import time

headers = {
	'Access-Control-Allow-Origin': '*',
	'Access-Control-Allow-Methods': 'POST',
	'Access-Control-Max-Age': '1000'
}

firebase_admin.initialize_app()

def incominghttp(request):
	fields = {}
	data = request.form.to_dict()
	for field in data:
		fields[field] = data[field]
		print('Processed field: %s' % field)
		
	importepoch = time.time()
	fields.update({'epoch': importepoch})
	
	importurlstring = fields['url']
	inteltype = importurlstring[33:]
	event.update({"intel-type": inteltype})

	packagejson = json.dumps(fields, indent = 4)
	json_object = json.loads(packagejson)

	importintel = firestore.client().collection('intel-dump')
	intelligence = importintel.document()
	intelligence.set(json_object)

	return (jsonify(success='true',), 200, headers)
