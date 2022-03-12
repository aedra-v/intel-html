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

firebase_admin.initialize_app()

def import_kddump(request):
    data = requests.get('https://utopia-game.com/gen/game/kingdoms_dump/')
    
    datalist = data.json()

    datalistclean = data.json()
    del datalistclean[0]
    del datalistclean[-1]
    elength = len(datalistclean)

    datadict = {}
    keylist = []

    for i in range(elength):
      keylist.append(datalistclean[i]['loc'])

    datadict = dict(zip(keylist, datalistclean))

    importintel = firestore.client().collection('kd-dump')
    intelligence = importintel.document()
    intelligence.set(datadict)

    return f'Success!'
