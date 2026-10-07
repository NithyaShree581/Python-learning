from flask import Flask, request

app = Flask(__name__)
users = [{"id": i, "name": f"User{i}"} for i in range(1, 51)]

@app.route("/users")
def get_users():
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 10, type=int)

    start = (page - 1) * limit
    end = start + limit

    
    result = users[start:end]
    total = len(users)
    total_pages = (total + limit - 1) // limit  
    return {
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": total_pages,
        "users": result
    }

if __name__ == "__main__":
    app.run(port=3000,debug=True)
