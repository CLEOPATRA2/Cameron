import os
from BOFS.create_app import create_app

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app")
app = create_app(path, 'minimal.cfg')

from flask import Flask, render_template, request
from flask import jsonify
from .. import execute as exec

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
    app.debug = True
    app.run()
