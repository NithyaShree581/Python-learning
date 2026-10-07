from flask import Flask,request

app = Flask(__name__)

users = [
    {"Name": "Nithya", "Age": 21, "City": "Bengaluru"},
    {"Name": "Radha", "Age": 30, "City": "Hindupur"},
    {"Name": "Murali", "Age": 34, "City": "Bengaluru"}
]


@app.route("/users", methods=["GET"])
def get_info():

    input_from_user = request.args.get("city")

    if input_from_user:
        filtered = []

        for user in users:
            if user["City"].lower() == input_from_user.lower():
                filtered.append(user)

        if filtered:
            return filtered
        else:
            return "No city found"
    


if __name__ == "__main__":
    app.run(debug=True,port=3000)