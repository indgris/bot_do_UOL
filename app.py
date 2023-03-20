from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Olá, mundo!"

@app.route("/sobre")
def sobre():
  return "Sobre"

@app.route("/contato")
def contato():
  return "contato@algum.com"
