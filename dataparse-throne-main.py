from bs4 import BeautifulSoup
import pandas as pd
import firebase_admin
from google.cloud import storage
from firebase_admin import credentials
from firebase_admin import firestore

firebase_admin.initialize_app()

def parse_throne(event, context):
    resource_string = context.resource
    trigger_docid = resource_string.split('/')[-1]
    print(f"Function triggered by change to: {resource_string}.")
    print(str(event))

    importhtml = event['value']['fields']['importhtml']['stringValue']
    print('p1 pass')

    inteltable = pd.read_html(importhtml)
    inteltable[0][0] = inteltable[0][0].str.replace('\W','', regex=True)
    inteltable[0][2] = inteltable[0][2].str.replace('\W','', regex=True) 
    test2 = inteltable[0][0].iloc[1]
    print(test2)

    soup = BeautifulSoup(importhtml, 'html.parser')
    test3 = soup.find_all('h2')[2].a.get_text()
    print(test3)

    importdict = {
        'utotime': soup.find_all('h2')[2].br.next_element.split('(')[0].strip(),
        'nexttick': soup.find_all('h2')[2].br.next_element.split('(')[1].strip().split(':')[1][:-1].strip(),
        'provlabel': soup.find_all('h2')[2].next_element[16:-2],
        'loc': soup.find_all('h2')[2].a.get_text(),
        'thronecommand': soup.find('div', id = 'throne-monarch-message').p,
        inteltable[0][0].iloc[1]: inteltable[0][1].iloc[1],
        inteltable[0][0].iloc[2]: inteltable[0][1].iloc[2],
        inteltable[0][0].iloc[3]: inteltable[0][1].iloc[3],
        inteltable[0][0].iloc[4]: inteltable[0][1].iloc[4],
        inteltable[0][0].iloc[5]: inteltable[0][1].iloc[5],
        inteltable[0][0].iloc[6]: inteltable[0][1].iloc[6],
        inteltable[0][0].iloc[7]: inteltable[0][1].iloc[7],
        inteltable[0][0].iloc[8]: inteltable[0][1].iloc[8],
        inteltable[0][0].iloc[9]: inteltable[0][1].iloc[9],
        inteltable[0][2].iloc[1]: inteltable[0][1].iloc[1],
        inteltable[0][2].iloc[2]: inteltable[0][3].iloc[2],
        inteltable[0][2].iloc[3]: inteltable[0][3].iloc[3],
        inteltable[0][2].iloc[4]: inteltable[0][3].iloc[4],
        inteltable[0][2].iloc[5]: inteltable[0][3].iloc[5],
        inteltable[0][2].iloc[6]: inteltable[0][3].iloc[6],
        inteltable[0][2].iloc[7]: inteltable[0][3].iloc[7],
        inteltable[0][2].iloc[8]: inteltable[0][3].iloc[8],
        inteltable[0][2].iloc[9]: inteltable[0][3].iloc[9],
    }

    print(importdict)

    importintel = firestore.client().collection('throne').document(trigger_docid).update(importdict)
    
    return f'Success'
