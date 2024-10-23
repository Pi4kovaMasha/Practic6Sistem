from flask import Flask, request, jsonify
from users import *

app = Flask(__name__)

@app.route("/users/", methods=['GET'])
def returnUserInfo():
    id = int(request.args.get("id"))
    return jsonify(users[id])

if __name__ == "__main__":
    app.run(debug=True)