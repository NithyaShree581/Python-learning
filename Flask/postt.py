#23/09/2026
from flask import Flask, request

app = Flask(__name__)

users = []
data = {"name": "Nithyasree", "age": 21}

@app.route("/users", methods=["GET"])
def get_users():
    return users

@app.route("/users", methods=["POST"])
def create_user():
    users.append(data)
    return users, 201

@app.route("/users", methods=["PUT"])
def update_user():
   
    if users:  
        users[0]["university"] = "RNS Institute of Technology"
        return users, 200
    else:
        return {"error": "No users to update"}, 404

if __name__ == "__main__":
    app.run(debug=True)
