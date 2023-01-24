from flask import Flask
import requests
import json
from datetime import datetime
from classes import card

app = Flask(__name__)


@app.route('/')
def index():
    print(datetime.now().strftime("%H:%M:%S"))
    url = "https://digimoncard.io/api-public/search.php"

    params = {
        "pack": "BT01-03: Release Special Booster Ver.1.0",
        "sortdirection": "desc",
        "series": "Digimon Card Game"
    }
    headers = {}

    response = requests.get(url, params=params)
    print(response)
    print(datetime.now().strftime("%H:%M:%S"))
    cardList = json.loads(response.text)
    print(len(cardList))
    while(len(cardList) != 0):
        singleCard = card.Card(cardList.pop())
        # print(f'{singleCard}\n\n')
    return "cardList"


app.run(host='0.0.0.0', port=81)
