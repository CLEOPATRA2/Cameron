
from flask import Flask, render_template, request
from flask import jsonify
import Cameron.Cameron.execute as exec

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/chat')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def reply ():
    msg = request.form['msg']
    return jsonify( { 'text': exec.predict(msg) } )


if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)