from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

# Flask app create kar rahe hain
app = Flask(__name__)

# Environment variable se MONGO_HOST le rahe hain, agar na mile to default "mongo"
mongo_host = os.getenv("MONGO_HOST", "mongo")
# MongoClient se MongoDB server se connect ho rahe hain
client = MongoClient(f"mongodb://{mongo_host}:27017/")

# "testdb" naam ka database use kar rahe hain
db = client["testdb"]

# "testcollection" naam ki collection use kar rahe hain
collection = db["testcollection"]

# Sample data ek baar hi insert karna hai agar collection empty ho toh
if collection.count_documents({}) == 0:
    collection.insert_many([
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ])

# Home route - basic endpoint jo app chal raha hai yeh confirm karta hai ya health check bhi keh sakte ho
@app.route('/')
def home():
    return jsonify({"message":"👋 Hello from Flask running inside Docker with MongoDB"})

# GET request ke liye endpoint - saari data fetch karta hai collection se
@app.route('/data', methods=['GET'])
def get_data():
    # find se data la rahe hain aur "_id" field exclude kar rahe hain
    data = list(collection.find({}, {"_id": 0}))
    # data ko JSON format mein return kar rahe hain
    return jsonify(data)

# POST request ke liye endpoint - new data insert karta hai
@app.route('/add', methods=['POST'])
def add_data():
    # request body se JSON data nikal rahe hain
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data:
        return jsonify({"error": "Invalid data. Must include 'name' and 'age'."}), 400
    
    # MongoDB mein naya document insert kar rahe hain
    collection.insert_one({"name": data["name"], "age": data["age"]})
    return jsonify({"message": "Data inserted successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
