from flask import Flask, render_template, session, redirect,request

app = Flask(__name__)

app.secret_key="something"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process',methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('/show.html')
    
if __name__=="__main__":
    app.run(debug=True)