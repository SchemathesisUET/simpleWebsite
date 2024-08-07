from flask import Flask, jsonify, request

app = Flask(__name__)

# API hello to greet the user. The user name only accepts string that consists of alphabets only. If not then it will return an error message.
@app.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name")
    if name.isalpha():
        return jsonify({"message": f"Hello, {name}!"})
    else:
        return jsonify({"message": "Name should only contain alphabets."}), 400

# API to add two numbers. The numbers should be integers. If not then it will return an error message.
@app.route("/add", methods=["GET"])
def add():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    if num1.isdigit() and num2.isdigit():
        return jsonify({"result": int(num1) + int(num2)})
    else:
        return jsonify({"message": "Both numbers should be integers."}), 400

if __name__ == "__main__":
    app.run(debug=True)
