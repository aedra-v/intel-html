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
    
    #datalist = data.json()
    
    datalist = ---
    
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def py_test(request):
    #Manual simulation of data
    datalist = ['2022-03-12 19:48:02.428472', {'count': 1, 'loc': '1:1', 'provinces': [{'loc': '1:1', 'land': 1700, 'name': 'DavidC', 'protected': True, 'race': 'Bocan', 'honor': 'Baron', 'nw': 233894}], 'land': 1700, 'name': 'Game Administration', 'stance': 'Normal', 'wars': [0, 0], 'honor': 2500, 'nw': 233894}, {'count': 5, 'loc': '1:3', 'provinces': [{'loc': '1:3', 'land': 1504, 'name': 'Deeznutz', 'protected': False, 'race': 'Bocan', 'honor': 'Baron', 'nw': 239505}, {'loc': '1:3', 'land': 3638, 'name': 'Meepos', 'protected': False, 'race': 'Elf', 'honor': 'King', 'nw': 1016604}, {'loc': '1:3', 'land': 2953, 'name': 'My OFF so HARD', 'protected': False, 'race': 'Dwarf', 'honor': 'Lord', 'nw': 904145}, {'loc': '1:3', 'land': 3420, 'name': 'TNT ka tropa', 'protected': False, 'race': 'Bocan', 'honor': 'Baron', 'nw': 935384}, {'loc': '1:3', 'land': 3269, 'name': 'X01', 'protected': False, 'race': 'Bocan', 'honor': 'Baron', 'nw': 956726}], 'land': 14784, 'name': 'Psych Ward', 'stance': 'Normal', 'wars': [1, 2], 'honor': 11727, 'nw': 4052364}, {'count': 6, 'loc': '1:2', 'provinces': [{'loc': '1:2', 'land': 5558, 'name': 'Zanarkand', 'protected': False, 'race': 'Bocan', 'honor': 'Queen', 'nw': 2132582}, {'loc': '1:2', 'land': 5031, 'name': 'big titty girlfriend', 'protected': False, 'race': 'Bocan', 'honor': 'Marchioness', 'nw': 2061274}, {'loc': '1:2', 'land': 5112, 'name': 'Lonely Mountain', 'protected': False, 'race': 'Dwarf', 'honor': 'Viscount', 'nw': 1822137}, {'loc': '1:2', 'land': 4781, 'name': 'Bambino', 'protected': False, 'race': 'Bocan', 'honor': 'Marquis', 'nw': 2074654}, {'loc': '1:2', 'land': 6063, 'name': 'Fae', 'protected': False, 'race': 'Dwarf', 'honor': 'Countess', 'nw': 2298014}, {'loc': '1:2', 'land': 5290, 'name': 'Queso', 'protected': False, 'race': 'Dwarf', 'honor': 'Count', 'nw': 2011299}], 'land': 31835, 'name': 'Kingdom Name', 'stance': 'Normal', 'wars': [3, 4], 'honor': 26101, 'nw': 12399960}, {'count': 6, 'loc': '2:1', 'provinces': [{'loc': '2:1', 'land': 5527, 'name': 'Mas Langosta Por Favor', 'protected': False, 'race': 'Human', 'honor': 'King', 'nw': 1661386}, {'loc': '2:1', 'land': 5355, 'name': 'Black Star Fish', 'protected': False, 'race': 'Bocan', 'honor': 'Marquis', 'nw': 2096985}, {'loc': '2:1', 'land': 5050, 'name': 'Erica', 'protected': False, 'race': 'Bocan', 'honor': 'Countess', 'nw': 1890951}, {'loc': '2:1', 'land': 5622, 'name': 'Marshlands', 'protected': False, 'race': 'Human', 'honor': 'Viscount', 'nw': 1789961}, {'loc': '2:1', 'land': 5356, 'name': 'Pain', 'protected': False, 'race': 'Elf', 'honor': 'Baron', 'nw': 2029275}, {'loc': '2:1', 'land': 5785, 'name': 'I O R I', 'protected': False, 'race': 'Human', 'honor': 'Viscount', 'nw': 2106628}], 'land': 32695, 'name': 'Agreed war 6 3', 'stance': ['war', '6:3'], 'wars': [2, 3], 'honor': 20005, 'nw': 11575186}, {'count': 5, 'loc': '2:3', 'provinces': [{'loc': '2:3', 'land': 3413, 'name': 'Apt 2B', 'protected': False, 'race': 'Dryad', 'honor': 'Baron', 'nw': 1055072}, {'loc': '2:3', 'land': 3711, 'name': 'Culdeo', 'protected': False, 'race': 'Bocan', 'honor': 'King', 'nw': 1419522}, {'loc': '2:3', 'land': 4092, 'name': 'Changying', 'protected': False, 'race': 'Bocan', 'honor': 'Noble Lady', 'nw': 1349182}, {'loc': '2:3', 'land': 2137, 'name': 'effit', 'protected': False, 'race': 'Dwarf', 'honor': 'Baron', 'nw': 330044}, {'loc': '2:3', 'land': 7665, 'name': 'Dalaran', 'protected': False, 'race': 'Bocan', 'honor': 'Marquis', 'nw': 3318879}], 'land': 21018, 'name': 'Looking for war pm dal', 'stance': 'Normal', 'wars': [2, 4], 'honor': 15679, 'nw': 7472699}, {'count': 6, 'loc': '2:2', 'provinces': [{'loc': '2:2', 'land': 2659, 'name': 'Xendell', 'protected': False, 'race': 'Dwarf', 'honor': 'Lord', 'nw': 952637}, {'loc': '2:2', 'land': 2913, 'name': 'MRG', 'protected': False, 'race': 'Bocan', 'honor': 'King', 'nw': 889153}, {'loc': '2:2', 'land': 2297, 'name': 'Rancank', 'protected': False, 'race': 'Gnome', 'honor': 'Baron', 'nw': 653883}, {'loc': '2:2', 'land': 3216, 'name': 'Dungeon Druid', 'protected': False, 'race': 'Human', 'honor': 'Lord', 'nw': 937938}, {'loc': '2:2', 'land': 3230, 'name': 'Dj langemand', 'protected': False, 'race': 'Human', 'honor': 'Lord', 'nw': 971698}, {'loc': '2:2', 'land': 2963, 'name': 'rip', 'protected': False, 'race': 'Human', 'honor': 'Baron', 'nw': 874609}], 'land': 17278, 'name': 'Run it Back', 'stance': 'Normal', 'wars': [1, 4], 'honor': 13633, 'nw': 5279918}, '2022-03-12 19:48:02.485025']
    print(datalist)
    
    
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
