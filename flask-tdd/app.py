from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def get_random_number():
    return jsonify({"number": random.randint(1, 100)})

@app.route('/even-odd/<int:number>', methods=['GET'])
def check_even_odd(number):
    result = "even" if number % 2 == 0 else "odd"
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)