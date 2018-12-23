from flask import Flask
from server.controller.fizzbuzz import get as get_fizzbuzz


apis = [
    get_fizzbuzz.app,
]

app = Flask(__name__)

# Blueprint の登録
for api in apis:
    app.register_blueprint(api, url_prefix="/v1")
