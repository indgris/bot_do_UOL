import os

import requests
import gspread
from flask import Flask
from bs4 import BeautifulSoup
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from tchan import ChannelScraper


TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID"]
GOOGLE_SHEETS_CREDENTIALS = os.environ["GOOGLE_SHEETS_CREDENTIALS"]

with open ("credenciais.json", mode="w") as fobj:
  fobj.write(GOOGLE_SHEETS_CREDENTIALS)

conta = ServiceAccountCredentials.from_json()
api = gspread.authorize(conta) # sheets.new
planilha = api.open_by_key("1BuTfkPK7oY3X9-dA4pz1Z-KtNiyyWIFjZUs0CICr4Qg")
sheet = planilha.worksheet("Updates")

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

@app.route("/dedoduro")
def dedoduro():
  mensagem = {"chat_id": TELEGRAM_ADMIN_ID, "text": "Alguém acessou a página dedo duro!"}
  requests.post(f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage", data=mensagem)
  return "Tô de olho, ein!"

@app.route("/dedoduro2")
def dedoduro2():
  sheet.append_row(["Teste", "Banan", "maça"])
  return "Planilha escrita!"
