from flask import Flask, render_template, request
from flask import jsonify



import Cameron.Cameron.execute as exec

app = Flask(__name__, static_url_path='/static')


@app.route('/message', methods=['POST'])
def reply ():
    msg = request.form['msg']
    return jsonify( { 'text': exec.predict(msg) } )

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=False)