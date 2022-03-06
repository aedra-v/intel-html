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
	packagestring = json.dumps(fields, indent = 4)
	json_indentedpackage = json.loads(packagestring)
		aion = datetime.now()
		aionlist = {'utodatetest':aion}
		aionjson = json.dumps(aionlist, indent = 4)
		packagejson_aionjson = {key: value for (key, value) in (json_indentedpackage.items() aionjson.items())}.
		json_full_object = json.loads(packagejson_aionjson)

	importintel = firestore.client().collection('intel-dump')
	intelligence = importintel.document()
	intelligence.set(json_object)

	return (jsonify(success='true',), 200, headers)
