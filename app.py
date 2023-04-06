import os

import requests
import gspread
from flask import Flask, request
from bs4 import BeautifulSoup
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials


GOOGLE_SHEETS_CREDENTIALS = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
with open("credenciais.json", mode="w") as arquivo:
  arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
  
conta = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json")
api = gspread.authorize(conta)
planilha = api.open_by_key("1BuTfkPK7oY3X9-dA4pz1Z-KtNiyyWIFjZUs0CICr4Qg")
sheet = planilha.worksheet("Updates")

app = Flask(__name__)

menu = """

<a href="/">Página inicial</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
"""

@app.route("/")
def hello_world():
  return menu + "Olá, mundo! Este é o saite da indgri"

@app.route("/sobre")
def sobre():
  return menu + "Sobre: ser ou não ser?"

@app.route("/contato")
def contato():
  return menu + "iruela@uolinc.com"

@app.route("/telegram-bot", methods=["POST"])
def telegram_bot():
    update = request.json
    message = update["message"]["text"]
    chat_id = update["message"]["chat"]["id"]
    datahora = str(datetime.datetime.fromtimestamp(update["message"]["date"]))
    first_name = update["message"]["from"]["first_name"]

    def mensagem_com_noticias_mais_lidas():
    # raspagem
    link = 'http://uol.com.br'
    resposta = requests.get(link)
    html = BeautifulSoup(resposta.content, 'html.parser')

    links_uol = html.findAll('ol', {'class': 'mostRead'})[0].findAll('a')

    mais_lidas_uol = []

    for noticia in links_uol:
        manchete = noticia.text.strip()
        link = noticia.get('href')
        data = datetime.today()
        mais_lidas_uol.append([manchete, link])

    #Tratamento da mensagem final que será enviada pelo bot
    mensagem_final = " "
    for item in mais_lidas_uol:
        mensagem_final = mensagem_final + f"{item[0]} | Leia agora! {item[1]}\n"

    return mensagem_final

     mensagem_final = mensagem_com_noticias_mais_lidas()
    
    # Configuração da troca de mensagem
    if message == "/start":
        texto_resposta = "Oi! Este é o bot do UOL, para receber as notícias mais lidas agora digite /sim"

    elif message == "/sim":
        texto_resposta = mensagem_final

    elif message.lower().strip() in ["/SIM", "\sim", "/dim", "\sin", "sim"]:
        mensagem_final = mensagem_com_noticias_mais_lidas()
        texto_resposta = "Essas são as matérias mais lidas no UOL agora: \n"
        for item in mensagem_final.split('\n')[:-1]:
            texto_resposta += f"{item}\n"

    else:
        texto_resposta = "Não entendi!"

    nova_mensagem = {"chat_id": chat_id, "text": texto_resposta}
    requests.post(f"https://api.telegram.org./bot{token}/sendMessage", data=nova_mensagem)
    
    # Requisita que a API do Telegram mande a mensagem
    resposta = requests.post(f"https://api.telegram.org./bot{TELEGRAM_API_KEY}/sendMessage", data=nova_mensagem)
    print(resposta.text)
    return "ok"
