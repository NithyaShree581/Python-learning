from flask import Flask
fla=Flask(__name__)
@fla.route('/')
def something():
    return "<h1>Nithyasree<h1>"
if __name__=="__main__":
    fla.run(debug=True)
    