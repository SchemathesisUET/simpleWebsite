from flask import Flask, jsonify, request

app = Flask(__name__)

# API hello to greet the user. The user name only accepts string that consists of alphabets only and have at least 1 alphabets. If not then it will return an error message.
@app.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name")
    if name.isalpha() and len(name) > 0:
        return jsonify({"message": f"Hello, {name}!"})
    else:
        return jsonify({"message": "Name should be a string that consists of alphabets only and have at least 1 alphabet."}), 400

# API to add two numbers. The numbers should be positive integers. If not then it will return an error message.
@app.route("/add", methods=["GET"])
def add():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    if num1.isdigit() and num2.isdigit():
        return jsonify({"result": int(num1) + int(num2)})
    else:
        return jsonify({"message": "Both numbers should be integers."}), 400

# API with 3 request bodies: name, age and address. The name only accepts string that consists of alphabets only and have at least 1 alphabets. If not then it will return an error message. The age should be a positive integer. If not then it will return an error message. The address should be a string. If not then it will return an error message.
#  If object have no attribute name, age or address, it will return an error message.
@app.route("/details", methods=["POST"])
def details():
    data = request.get_json()
    if "name" in data and "age" in data and "address" in data:
        name = data["name"]
        age = data["age"]
        address = data["address"]
        if name.isalpha() and len(name) > 0:
            if age.isdigit() and int(age) > 0:
                return jsonify({"name": name, "age": int(age), "address": address})
            else:
                return jsonify({"message": "Age should be a positive integer."}), 400
        else:
            return jsonify({"message": "Name should be a string that consists of alphabets only and have at least 1 alphabet."}), 400
    else:
        return jsonify({"message": "Object should have name, age and address attributes."}), 400

    
# API to calculate sum from x to y using a for-loop. The x and y should be positive integers. If not then it will return an error message.
@app.route("/sum", methods=["GET"])
def sum():
    x = request.args.get("x")
    y = request.args.get("y")
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        if x > 0 and y > 0:
            sum = 0
            for i in range(x, y+1):
                sum += i
            return jsonify({"result": sum})
        else:
            return jsonify({"message": "Both numbers should be positive integers."}), 400
    else:
        return jsonify({"message": "Both numbers should be integers."}), 400
    
if __name__ == "__main__":
    app.run(debug=True)