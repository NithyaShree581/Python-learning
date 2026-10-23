
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Temporary storage
customers = {}
next_customer_id = 1


# 1. GET - Retrieve all customers
@app.get("/customers")
def get_customers():
    return jsonify(list(customers.values())), 200


# 2. POST - Create a customer
@app.post("/customers")
def create_customer():
    global next_customer_id

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Expected a JSON object"}), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({
            "error": "Name and email are required"
        }), 400

    customer = {
        "id": next_customer_id,
        "name": name,
        "email": email
    }

    customers[next_customer_id] = customer
    next_customer_id += 1

    logger.info("Customer created successfully")

    return jsonify(customer), 201


# 3. PUT - Replace customer details
@app.put("/customers/<int:customer_id>")
def replace_customer(customer_id):
    if customer_id not in customers:
        return jsonify({"error": "Customer not found"}), 404

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Expected a JSON object"}), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({
            "error": "Name and email are required"
        }), 400

    customers[customer_id] = {
        "id": customer_id,
        "name": name,
        "email": email
    }

    logger.info("Customer replaced successfully")

    return jsonify(customers[customer_id]), 200


# 4. PATCH - Update selected customer fields
@app.patch("/customers/<int:customer_id>")
def update_customer(customer_id):
    customer = customers.get(customer_id)

    if customer is None:
        return jsonify({"error": "Customer not found"}), 404

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Expected a JSON object"}), 400

    if "name" in data:
        if not data["name"]:
            return jsonify({"error": "Name cannot be empty"}), 400
        customer["name"] = data["name"]

    if "email" in data:
        if not data["email"]:
            return jsonify({"error": "Email cannot be empty"}), 400
        customer["email"] = data["email"]

    logger.info("Customer updated successfully")
    return jsonify(customer), 200


if __name__ == "__main__":
    app.run(debug=True)
