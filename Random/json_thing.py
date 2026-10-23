"""here we are trying to learn about the json requests,exceptions and logging stuf"""

from flask import Flask,jsonify,request
import logging
app=Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
@app.get("/customers")
def create_customer():
    data=request.get_json(silent=True)
    if not isinstance(data,dict):
        return jsonify({"error": "Expected a json object"}),400
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return jsonify({
            "error": "Name and email are required"
        }), 400
    try:
        logger.info("customer creation is succcessful")
        return jsonify({
            "message": "Customer data validated",
            "name": name,
            "email": email
        }), 201
    except:
        logger.exception("unexpected errror")
        return jsonify({"error":"internal server error"}),500
if __name__ == "__main__":
    app.run(debug=True)

    



