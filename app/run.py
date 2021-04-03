import  concurrent.futures
import subprocess
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()

def runCode(language, code):
    if language == "python":
        with open('file.py', "w") as outfile:
            outfile.write(code)
        res = subprocess.getoutput(["python file.py"])


        return res

    elif language == "C":
        with open('file.c', "w") as outfile:
            outfile.write(code)
        
        res = subprocess.getoutput(["gcc file.c -o out;./out"])
        
        return res

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    code = request.form['text']
    print(code)
    return redirect('/submit')

@app.route('/exec', methods=['POST'])
def exec():
    data = request.get_json(force=True)
    language = data['lang']
    code = data['code']

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(runCode, language, code)
        output = future.result()
    
    return output

if __name__ == '__main__':

    app.run('127.0.0.1', 5000, debug=True)

