from flask import Flask,render_template,send_from_directory,request,jsonify
import os
from flaskErrorHandler import SafeRun
app = Flask(__name__)

BASE_URL = os.path.abspath(os.path.dirname(__file__))


APP_FOLDER = os.path.join(BASE_URL, "static")

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/index1')
def index1():

    return render_template('index1.html')


@app.route('/index2')
def index2():

    return render_template('index2.html')



@app.route('/get_title')
def get_title():
    print("in function")
    return 'Telsa Azad'



@app.route('/invoke_error')
def invoke_error():
    a = 1
    b = 0
    c = 1/0

    return jsonify({'result':'success'})

@app.route('/client-app/<path:filename>')
def client_app_folder(filename):
    return send_from_directory(APP_FOLDER, filename)

SafeRun(app,{'from_addr':'','to_addr':'','password':''})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
