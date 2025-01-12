import json
import urllib.request

def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')

    print(requestJson)

    response = json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

def clean_text(text):
    if isinstance(text, list):
        return ' '.join(text)

def get_deck_id(deck_name):
    decks = invoke('deckNamesAndIds')
    return decks.get(deck_name)

deck_name = 'Nome do Deck'
invoke('createDeck', deck=deck_name)

id_deck = get_deck_id(deck_name)

invoke('saveDeckConfig', config={
            "lapse": {
                "leechFails": 8,
                "delays": [10],
                "minInt": 1,
                "leechAction": 0,
                "mult": 0
            },
            "dyn": False,
            "autoplay": False,
            "mod": 1502970872,
            "id": id_deck,
            "maxTaken": 60,
            "new": {
                "bury": True,
                "order": 1,
                "initialFactor": 2500,
                "perDay": 100,
                "delays": [1, 10],
                "separate": True,
                "ints": [1, 4, 7]
            },
            "name": deck_name,
            "rev": {
                "bury": True,
                "ivlFct": 1,
                "ease4": 1.3,
                "maxIvl": 36500,
                "perDay": 100,
                "minSpace": 1,
                "fuzz": 0.05
            },
            "timer": 0,
            "replayq": True,
            "usn": -1
        })

with open('arquivo.json', 'r') as file:
    reader = json.load(file)
    
    for row in reader:

        front = clean_text(row["front"])
        back = clean_text(row["back"])
        
        invoke('addNote', note={
            "deckName": deck_name,
            "modelName": "Basic",
            "fields": {
                "Front": front,
                "Back": back
            },
            "tags": ["english"],
            "options": {
                "allowDuplicate": True
            }
        })

    
