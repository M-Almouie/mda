#So, it returns 404 whenever *.cgi is not suffixed with '/'
# e.g: http://cgi.cse.unsw.edu.au/~z5114185/mda/mdalmouiee.cgi
# the correct url is http://cgi.cse.unsw.edu.au/~z5114185/mda/mdalmouiee.cgi/
# when first accessing the link


from flask import Flask, session, render_template, request, redirect
import os, datetime

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def begin():
    return render_template('/homepage.html')

@app.route('/blg', methods=['GET','POST'])
def blogs():
    return render_template('/blog.html')

@app.route('/sum', methods=['GET','POST'])
def summ():
    return render_template('/sum.html')

@app.route('/skills', methods=['GET','POST'])
def skills():
    return render_template('/skills.html')
    
@app.route('/high', methods=['GET','POST'])
def high():
    return render_template('/high.html')

@app.route('/exp', methods=['GET','POST'])
def exp():
    return render_template('/exp.html')
    
@app.route('/edu', methods=['GET','POST'])
def edu():
    return render_template('/edu.html')


# Blogs...
@app.route('/ml', methods=['GET','POST'])
def ml():
    return render_template('/blogs/ML.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
