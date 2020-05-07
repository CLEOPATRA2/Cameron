from flask import Flask, render_template, request
from flask import jsonify


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def reply ():
    return jsonify( { 'text': predict.predicted_sentence(request.form['msg']) } )

import tensorflow as tf
import Cameron.Cameron.execute
evaluate()
predict.prediction()
predict.predicted_sentence()


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=False)