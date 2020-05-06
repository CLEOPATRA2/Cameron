import sys
import json

from flask import Flask, render_template
from flask import jsonify
from setup import predicted_sentence


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def reply ():
    return jsonify( { 'text':(predicted_sentence) } )

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=False)