from flask import Flask, jsonify, request
from flask_cors import CORS
from vegetables import VEGETABLES
from config import trefle_apikey
import requests
import json

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

# sanity route check
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# route to get all vegetables from vegetables.py file
@app.route('/vegetables', methods=['GET'])
def vegetables():
    return jsonify({
        'vegetables': VEGETABLES
    })


@app.route('/getplantinfo', methods=['GET'])
def get_plant_info():
    plant_id = request.args.get('plantid')
    url_detail = "https://trefle.io/api/plants/{}?token={}".format(plant_id, trefle_apikey)
    request_detail = requests.get(url_detail)
    return jsonify(json.loads(request_detail.content))


@app.route('/getplant', methods=['GET'])
def getplantid():
    plant_name = request.args.get('name')
    url = "https://trefle.io/api/plants?q={}&token={}".format(plant_name, trefle_apikey)
    r = requests.get(url)
    plants = json.loads(r.content)
    for plant in plants:
        if plant["common_name"] == plant_name:
            plant_id = plant["id"]
            print('inside if {}'.format(plant_id))
            break
    try:
        plant_id
    except NameError:
        plant_id = plants[0]["id"]
    url_detail = "https://trefle.io/api/plants/{}?token={}".format(plant_id, trefle_apikey)
    request_detail = requests.get(url_detail)
    return jsonify(json.loads(request_detail.content))


if __name__ == '__main__':
    app.run()
