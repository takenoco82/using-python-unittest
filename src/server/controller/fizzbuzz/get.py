from flask import Blueprint, jsonify

from server.logic.fizzbuzz import fizzbuzz_gen

app = Blueprint('fizzbuzz', __name__)


@app.route('/fizzbuzz/<int:n>', methods=['GET'])
def get_fizzbuzz(n: int):
    try:
        response = {'fizzbuzz': list(fizzbuzz_gen(n))}
    except (TypeError, ValueError) as e:
        response = {'error': e.args[0]}
        return jsonify(response), 400

    return jsonify(response), 200
