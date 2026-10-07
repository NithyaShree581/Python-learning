from flask import Flask, request, render_template_string

app = Flask(__name__)
users = []
form_html = """
<!doctype html>
<html>
    <head>
        <title>User Form</title>
    </head>
    <body>
        <h2>Add a User</h2>
        <form action="/users" method="post">
            <label>Name:</label>
            <input type="text" name="name" required><br><br>
            <label>Age:</label>
            <input type="number" name="age" required><br><br>
            <button type="submit">Submit</button>
        </form>
    </body>
</html>
"""
@app.route("/")
def home():
    return render_template_string(form_html, users=users)

@app.route("/users", methods=["GET"])
def get_users():
    return users

@app.route("/users", methods=["POST"])
def create_user():
    # Get data from form
    name = request.form["name"]
    age = request.form["age"]
    new_user = {"name": name, "age": int(age)}
    users.append(new_user)
    return render_template_string(form_html, users=users), 201

if __name__ == "__main__":
    app.run(port=3000,debug=True)
