from flask import Flask,request
app=Flask(__name__)
users=[{"id":i,"name":"f:user{i}" }for i in range(1,50)]
@app.route("/users")
def getting_users():
    page=request.args.get("page",type=int)
    limit=request.args.get("limit",type=int)
    result=users[page:limit]
    return result
if __name__=="__main__":
    app.run(port=3000,debug=True)