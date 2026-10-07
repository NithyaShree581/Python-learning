from flask import Flask, request, send_file

app = Flask(__name__)


@app.route("/")
def home():
    return send_file("index.html")


@app.route("/script.js")
def javascript():
    return send_file("script.js")


@app.route("/save", methods=["POST"])
def save():
    data = request.get_json()

    print("Received data:")
    print(data)

    return {
        "message": "Data received successfully!"
    }


if __name__ == "__main__":
    app.run(debug=True)