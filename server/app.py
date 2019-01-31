from flask import Flask, jsonify
from flask_cors import CORS
from vegetables import VEGETABLES

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

# sanity route check
@app.route('/ping', methods=['GET'])
def ping_pong():
  return jsonify('pong!')

@app.route('/vegetables', methods=['GET'])
def vegetables():
  return jsonify({
    'vegetables': VEGETABLES
  })

if __name__ == '__main__':
  app.run()