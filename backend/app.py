from flask import Flask, jsonify
from flask_cors import CORS
from database import db

app = Flask(__name__)
CORS(app)

# localhost:5000
@app.route("/")
def get_all_customers():
    return jsonify(db)

# localhost:5000/add-realtor/<name>
@app.route("/add-realtor/<name>")
def add(name):
    db['realtors'].append(name)
    return ""

@app.route("/get-random-realtors")
def get_random_realtors():
    return realtors[::]


def calculate_realtor_score(client, realtor):
    pass
    

if __name__ == '__main__':
    app.run()