import requests
import json

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
