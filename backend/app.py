from flask import Flask, jsonify, request
from flask_cors import CORS
from database import db
import google.generativeai as genai
import time


app = Flask(__name__)
CORS(app)

@app.route("/narrow-clients")
def narrow_down_clients(realtor):

    realtor = str(realtor)
    client_scores = []
    for client in db["clients"]:
        score = int(gemini_response(realtor, client))
        client_scores.append((client, score))

    # Sort the list by score in descending order
    client_scores.sort(key=lambda x: x[1], reverse=True)

    # Get the top clients
    top_clients = [client for client, _ in client_scores[:3]]

    return jsonify(top_clients)


@app.route("/narrow-realtors")
def narrow_down_realtors(client):
    
    client = str(client)
    realtor_scores = []
    for realtor in db["realtors"]:
        score = int(gemini_response(realtor, client))
        time.sleep(1)
        score = round(score)
        realtor_scores.append((realtor, score))

    # Sort the list by score in descending order
    realtor_scores.sort(key=lambda x: x[1], reverse=True)

    # Get the top realtors
    top_realtors = [realtor for realtor, _ in realtor_scores[:3]]

    return jsonify(top_realtors)


@app.route("/ai/")
def gemini_response(realtor, client):

    print("inside")
    genai.configure(api_key="AIzaSyAJ1ML4UXZ7-pOKS5CeuZN3VbHnHnb0NFc")
    model = genai.GenerativeModel("gemini-1.5-flash")
    specifications =  """
    Take the following attributes of the realtor and compare it to the attributes of the client. 
    Assign an INTEGER, WHOLE NUMBER score out of 100 based on compatibility for real estate matching. 
    

    If the client and realtor are not in the same location (city/state) or do not speak the same language, 
    automatically reduce the score below 50.

    1. City (Weight: 15)
    Same city: 15 points.
    Nearby cities (within 50 miles or the same state): 10 points.
    No match: 0 points.

    2. State (Weight: 10)
    Same state: 10 points.
    Different state: 0 points.

    3. Experience Level (Weight: 15)
    Matching or complementary experience levels (e.g., first-time buyer with an experienced realtor): 15 points.
    Partial mismatch (e.g., experienced buyer with a novice realtor): 5 points.
    Severe mismatch: 0 points.

    4. Timeline (Weight: 15)
    Both the client and realtor have the same timeline (immediate or within 3 months): 15 points.
    Minor difference in timelines: 7 points.
    No alignment in timelines: 0 points.

    5. Language (Weight: 10)
    Exact match in language: 10 points.
    No match: 0 points.

    6. Property Type (Weight: 15)
    Exact match in property types: 15 points.
    Partial match (e.g., both like single-family homes, but the client also prefers condos): 7 points.
    No match: 0 points.

    7. Lifestyle (Weight: 15)
    If the realtor specializes in or aligns with the client’s lifestyle preferences (e.g., urban vs. suburban, pet-friendly): 15 points.
    Partial match: 7 points.
    No match: 0 points.

    8. Personality (Weight: 15)
    If the personalities align well (e.g., empathetic with attentive, reserved with reserved): 15 points.
    Partial match: 7 points.
    No match: 0 points."""

    response = model.generate_content(specifications + str(client) + str(realtor))
    clarified_response = model.generate_content("Please extract the final INTEGER, NUMERICAL VALUE score out of 100 and return only. It should be between 0 and 100, and only be one integer. Nothing more, nothing less. Find that from " + response.text)
    return (clarified_response.text)

@app.route('/receive-form-data', methods=['POST'])
def receive_form_data(): 
    narrowed_data = []
    form_data = request.form.to_dict()
    print(form_data) 
    if "budget" in form_data:
        narrowed_data = narrow_down_realtors(form_data)
    elif "budget" not in form_data:
        narrowed_data = narrow_down_clients(form_data)

    print(narrowed_data)

    return jsonify(narrowed_data)

# localhost:5000
@app.route("/")
def get_all_customers():
    return jsonify(db)
   #return db

# localhost:5000/add-realtor/<name>
@app.route("/add-realtor/<name>")
def add(name):
    db['realtors'].append(name)
    return ""
    

if __name__ == '__main__':
    app.run()