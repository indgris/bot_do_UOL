from flask import Flask
from tchan import ChannelScraper

app = Flask(__name__)

menu = """

<a href="/">Página inicial</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a> |  <a href="/portfolio">Portfólio</a> | <a href="/promocoes">Promoções</a>
<br>
"""

@app.route("/")
def hello_world():
  return menu + "Olá, mundo! Este é o saite da indgri"

@app.route("/sobre")
def sobre():
  return menu + "Sobre: ser ou não ser?"

@app.route("/contato")
def contato():
  return menu + "algum-email-ficticio@gmail.com"

@app.route("/portfolio")
def portfolio():
  return menu + "https://www.behance.net/indgri"

@app.route("/promocoes")
def promocoes():
  conteudo = menu + """
  Encontrei as seguintes promoções no <a href="https://t.me/promocoeseachadinhos">@promocoeseachadinhos</a>:
  <br>
  <ul>
  """
  scraper = ChannelScraper()
  contador = 0
  for message in scraper.messages("promocoeseachadinhos"):
    contador += 1
    texto = message.text.strip().splitlines()[0]
    conteudo += f"<li>{message.created_at} {texto}</li>"
    if contador == 10:
      break
  return conteudo + "</ul>"
