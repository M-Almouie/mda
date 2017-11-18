from flask import Flask, session, render_template, request, redirect
import os, datetime

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route('/homepage', methods=['GET','POST'])
def begin():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
