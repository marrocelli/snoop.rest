from flask import Flask, jsonify, render_template, request, url_for
from flask_bootstrap import Bootstrap
import random
import json

app = Flask(__name__)
Bootstrap(app)

with open('quotes.json', 'r') as f:
    all_quotes = json.load(f)


def get_quote():
    quote = random.choice(all_quotes)
    return quote


@app.route('/')
def home():
    quote = get_quote()
    return render_template('index.html', get_quote=get_quote, quote=quote, all_quotes=all_quotes)


@app.route('/get')
def api_GET():
    quote = get_quote().split('"')[1]
    return jsonify(quote=quote)


if __name__ == '__main__':
    app.run()
