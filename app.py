import random

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def random_status():
    random_code = random.choice([200, 300, 400, 500])
    response = {"status": random_code}
    return jsonify(response), random_code


if __name__ == "__main__":
    app.run()
