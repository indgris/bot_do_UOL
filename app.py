#Importando as bibliotecas e objetos necessários

import os

import requests
from flask import Flask, request
from bs4 import BeautifulSoup
from datetime import datetime

TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID"]

# Estrutura do site onde o trabalho será apresentado
app = Flask(__name__)

menu = """

<a href="/">Página inicial</a> | <a href="/sobre">Sobre</a> | <a href="/saibamais">Saiba mais</a>

"""

@app.route("/")
def hello_world():
    return menu + "<p></p><p>Hello, world! O bot do UOL está hospedado aqui :) com ele você recebe as matérias mais lidas do UOL neste momento. Acesse: t.me/universo_online_bot</p>"


@app.route("/sobre")
def sobre():
  return menu + "<p></p><p>Este projeto é um bot do Telegram que fornece as notícias mais lidas do site UOL. O bot realiza a raspagem das notícias mais lidas e as envia para os usuários por meio de comandos específicos.</p>"

@app.route("/saibamais")
def contato():
  return menu + "<p></p><p>Este é um projeto de conclusão da disciplina Algoritmos de Automação, ministrada por Álvaro Justen, no Master em Jornalismo de dados, automação e data storytelling do Insper.</p>"


#Bot do Telegram
ultima_mensagem_recebida_id = None

@app.route("/telegram-bot", methods=["POST"])
def telegram_bot():
    global ultima_mensagem_recebida_id # indica que é uma variável global
    if request.method == "POST":
        update = request.get_json()
        if "message" in update:
            message_id = update["message"]["message_id"]
            if message_id == ultima_mensagem_recebida_id:
                # Ignora a mensagem duplicada
                return "ok"
            ultima_mensagem_recebida_id = message_id
            
            text = update["message"]["text"]
            chat_id = update["message"]["chat"]["id"]
            datahora = str(datetime.fromtimestamp(update["message"]["date"]))
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
           

            # Tratamento da mensagem final que será enviada pelo bot
            mensagem_final = " "
            for item in mais_lidas_uol:
                mensagem_final = mensagem_final + f"{item[0]} | Leia agora! {item[1]}\n"

            return mensagem_final

        mensagem_final = mensagem_com_noticias_mais_lidas()

        #Emojis
        
        
        # Configuração da troca de mensagem
        if text == "/start":
            texto_resposta = "Oi! Este é o bot do UOL. Você quer receber as notícias mais lidas no site do UOL agora? /sim /não"
        
        elif text.lower().strip() in ["/SIM", "\sim", "/dim", "\sin", "sim"]:
            mensagem_final = mensagem_com_noticias_mais_lidas()
            texto_resposta = "Essas são as matérias mais lidas no UOL agora: \n"
            for item in mensagem_final.split('\n')[:-1]:
                texto_resposta += f"{item}\n"
         
        elif text.lower().strip() in ["/NÃO", "nao", "noa, "não", "/não", "\não", "/nao", "náo", "nã0", "/náo", "\nao", "nào", "naõ", "nâo", "/nâo", "\nâo"]:
            mensagem_final = mensagem_com_noticias_mais_lidas()
            texto_resposta = "Sem problemas. Se quiser saber o que está acontecendo mais tarde, escreva: receber notícias."
            for item in mensagem_final.split('\n')[:-1]:
                texto_resposta += f"{item}\n"
        
        elif text.lower().strip() in ["receber notícias", "receber notícias", "recber notícias", "receer notícias", "recebr notícias", "receber notcías", "receber notícias", "receber notíias", "receber notícas", "reecber notícias", "receber notíciás", "recebr notícas", "notícias, "receber"]:
            mensagem_final = mensagem_com_noticias_mais_lidas()
            texto_resposta = "Essas são as matérias mais lidas no UOL agora: \n"
            for item in mensagem_final.split('\n')[:-1]:
                texto_resposta += f"{item}\n"
                                      
        elif text.lower().strip() in ["obrigado", "obrigada", "grato", "grata", "gratidão", "valeu", "valeu, véinho", "tchau"]:
            texto_resposta_despedida = "Se quiser ler mais notícias, é chamar!"
           

                
        else:
            texto_resposta = "Não entendi o que você quis dizer! Eu ainda estou aprendendo :) Enquanto isso, visite o www.uol.com.br e fique por dentro do que está acontecendo no Brasil e no mundo."

        nova_mensagem = {"chat_id": chat_id, "text": texto_resposta}
        
        # Requisita que a API do Telegram mande a mensagem
        resposta = requests.post(f"https://api.telegram.org./bot{TELEGRAM_API_KEY}/sendMessage", data=nova_mensagem)
        print(resposta.text)
        return "ok"
