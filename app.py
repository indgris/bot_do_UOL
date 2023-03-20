from flask import Flask

app = Flask(__name__)

menu = """

<a href="/">Página inicial</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a> |  <a href="/portfolio">Portfólio</a>
<br>
"""

@app.route("/")
def hello_world():
  return "Olá, mundo! Este é o saite da indgri"

@app.route("/sobre")
def sobre():
  return "Sobre: ser ou não ser?"

@app.route("/contato")
def contato():
  return "algum-email-ficticio@gmail.com"

@app.route("/portfolio")
def contato():
  return "https://www.behance.net/indgri"
