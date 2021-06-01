from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/Klients')
def Klients():
  return render_template("index2.html")

@app.route('/Admins')
def Admins():
  return render_template("index3.html")


app.run(host='0.0.0.0', port=8080)