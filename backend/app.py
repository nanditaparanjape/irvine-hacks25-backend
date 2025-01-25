from flask import Flask, jsonify
from flask_cors import CORS
from database import db
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)
CORS(app)

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")


def get_gemini_response(prompt):
    url = "https://generativelanguage.googleapis.com"
    headers = {
        "Authorization": f"Bearer {GEMINI_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "prompt": prompt,
        "max_tokens": 10,  # You can adjust this value
        "temperature": 0.3,
        "top_p": 0.3,
    }
    
    response = requests.post(url, json=data, headers=headers)
 
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        print("Response Body:", response.text)
        return f"Error: Unable to get response from Gemini API {response.status_code}"
 

# localhost:5000/gemini-prompt/<top 2 characters from this show>
@app.route("/gemini")
def gemini_prompt():
    print("inside")
    prompt="what is your name"
    response = get_gemini_response(prompt)
    return jsonify({"response": response})
    # return {"key":"vsjkfnd"}

# localhost:5000
@app.route("/database")
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