from flask import Flask, render_template, request, url_for
from flask import jsonify
from .forms import LoginForm


import Cameron.Cameron.execute as exec

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'you-better-be-ready'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def reply ():
    msg = request.form['msg']
    return jsonify( { 'text': exec.predict(msg) } )


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=False)