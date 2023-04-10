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


################################################################ Bot do Telegram

############################################################### Set de atualizações

ultima_mensagem_recebida_id = None
@app.route("/telegram-bot", methods=["POST"])
def telegram_bot():
    global ultima_mensagem_recebida_id  # indica que é uma variável global
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

############################################################# Funcionalidade
            def mensagem_com_noticias_mais_lidas():
                # raspagem mais lidas do uol
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


            def mensagem_com_noticias_economia():
                # raspagem economia
                link = 'https://economia.uol.com.br/'
                resposta = requests.get(link)
                html = BeautifulSoup(resposta.content, 'html.parser')

                links_uol = html.findAll('div', {'class': 'float-box'})[0].findAll('a')

                mais_lidas_economia = []

                for noticia in links_uol:
                    manchete = noticia.text.strip()
                    link = noticia.get('href')
                    data = datetime.today()
                    mais_lidas_economia.append([manchete, link])

                # Tratamento da mensagem final que será enviada pelo bot
                mensagem_final_economia = " "
                for item in mais_lidas_economia:
                    mensagem_final_economia = mensagem_final + f"{item[0]} | Leia agora! {item[1]}\n \n"

                return mensagem_final_economia
            
            mensagem_final_economia = mensagem_com_noticias_economia()

            def mensagem_com_noticias_splash():
               # raspagem splash
               link = 'https://www.uol.com.br/splash/'
               resposta = requests.get(link)
               html = BeautifulSoup(resposta.content, 'html.parser')
               links_uol_splash = html.findAll('div', {'class': 'row'})[1].findAll('a')
    
               mais_lidas_uol_entrete = []
    
               for noticia in links_uol_splash:
                   manchete = noticia.text.strip()
                   link = noticia.get('href')
                   mais_lidas_uol_entrete.append([manchete, link])
    
               # Tratamento da mensagem final que será enviada pelo bot
               mensagem_final_entrete = " "
               for item in mais_lidas_uol_entrete:
                   mensagem_final_entrete = mensagem_final_entrete + f"{item[0]} | Leia agora! {item[1]}\n \n"
    
               return mensagem_final_entrete
    
            mensagem_final_entrete = mensagem_com_noticias_splash()
    
                                                      
            def  mensagem_com_noticias_geral():
                # raspagem
                link = 'https://noticias.uol.com.br/'
                resposta = requests.get(link)
                html = BeautifulSoup(resposta.content, 'html.parser')
                links_uol_noticias = html.findAll('div', {'class': 'float-box'})[0].findAll('a')
    
                destaque_uol_noticias = []
    
                for noticia in links_uol_noticias:
                manchete = noticia.text.strip()
                link = noticia.get('href')
                destaque_uol_noticias.append([manchete, link])
    
                # Tratamento da mensagem final que será enviada pelo bot
                mensagem_final_uol_noticias = " "
                for item in destaque_uol_noticias:
                    mensagem_final_uol_noticias = mensagem_final_uol_noticias + f"{item[0]} | Leia agora! {item[1]}\n \n"
    
                return mensagem_final_uol_noticias   
                                                      
            mensagem_final_uol_noticias = mensagem_com_noticias_geral()
                                                  
                                                  
            def mensagem_com_noticias_esporte():
                # raspagem
                link = 'https://www.uol.com.br/esporte/'
                resposta = requests.get(link)
                html = BeautifulSoup(resposta.content, 'html.parser')
                links_uol_esporte = html.findAll('div', {'class': 'positioning-bottom'})[0].findAll('a')

                mais_lidas_esporte = []

                for noticia in links_uol_esporte:
                    manchete = noticia.text.strip()
                    link = noticia.get('href')
                    mais_lidas_esporte.append([manchete, link])

                # Tratamento da mensagem final que será enviada pelo bot
                mensagem_final_esporte = " "
                for item in mais_lidas_esporte:
                    mensagem_final_esporte = mensagem_final_esporte + f"{item[0]} | Leia agora! {item[1]}\n \n"

                return mensagem_final_esporte

            mensagem_final_esporte = mensagem_com_noticias_esporte()                                                    

    

        ############################################################### Configuração da troca de mensagem
        if text == "/start":
            texto_resposta = "Oi! Este é o bot do UOL  ( ͡❛ ͜ʖ ͡❛) Você quer receber as notícias principais notícias do UOL agora? /sim ou /nao"
        
        elif text.lower().strip() in ["/sim", "/SIM", "\sim", "/dim", "\sin", "sim"]:
            texto_resposta = "Legal! ( ͡ᵔ ͜ʖ ͡ᵔ) Escolha uma categoria: /esportes /economia /noticias /entretenimento /mais-lidas"                           
                
        elif text.lower().strip() in ["/NÃO", "nao", "noa", "não", "/não", "\não", "/nao", "náo", "nã0", "/náo", "\nao", "nào", "naõ", "nâo", "/nâo", "\nâo"]:
            texto_resposta = "Sem problemas ¯\_( ͡❛ ͜ʖ ͡❛)_/¯ Se quiser saber o que está acontecendo mais tarde, escreva: receber notícias."
        
        elif text.lower().strip() in ["/mais-lidas", "/MAIS-LIDAS", "\mais-lidas", "mas lidas", "mais lida", "mias lidas", "mai lida"]:
            mensagem_final = mensagem_com_noticias_mais_lidas()
            texto_resposta = "Essas são as matérias mais lidas no UOL agora: \n"
            for item in mensagem_final.split('\n')[:-1]:
                texto_resposta += f"{item}\n"
                
        elif text.lower().strip() in ["\esportes", "/esportes", "/SPORT", "\esportes", "esporte", "esportes", "esprte", "esporter", "/esprtes", "sporTS", "espotes", "esprtes", "esportez", "esporrt", "esportres", "/esportez", "/SPOrt", "\esport", "espor", "esportss", "esprtte", "esporterrs"]:
            mensagem_final = mensagem_com_noticias_esporte()
            texto_resposta = "Essas são as matérias mais lidas no UOL agora: \n"
            for item in mensagem_final.split('\n')[:-1]:
                texto_resposta += f"{item}\n"
        
        elif text.lower().strip() in ["/emtretenimento", "/entretenimento", "entretenimento", "/entretinimento", "/entretenimeto", "/entertenimento", "/entertemimento", "/entretenimetno", "/entretneimento", "/entertetimento", "/entertenenimento", "/entretanimento", "/entertinimento", "/entretinmento", "/entreteniment", "/entretenmiento", "/entrretenimento"]:
             mensagem_final = mensagem_com_noticias_splash()
             texto_resposta = "Essas são as matérias mais lidas no UOL agora: \n"
             for item in mensagem_final.split('\n')[:-1]:
                 texto_resposta += f"{item}\n"
                                                  
        elif text.lower().strip() in ["\economia", "/economia", "/economi", "econo", "encon", "econimia", "\econimia", "\ecnomia", "\economai", "\econmoia", "\economla", "/econmia", "/economai", "econmoia", "/economla", "econimia", "\ecomomia", "/ecomomia", "\ecoonmia", "ecoonmia", "\economka"]:
             mensagem_final = mensagem_com_noticias_economia()
             texto_resposta = "Essas são as matérias mais lidas no UOL agora: \n"
             for item in mensagem_final.split('\n')[:-1]:
                 texto_resposta += f"{item}\n"
                
        elif text.lower().strip() in ["/noticias", "\noticias", "noticias", "\ntoicias", "notciias", "\notiicas", "notiias", "\notcias", "ntoicias", "/notciias", "/notiicas", "/notiias", "/notcias", "\noitcias", "/noitcias", "\notcias", "/notciias", "\notciaas" ]:
             mensagem_final = mensagem_com_noticias_geral()
             texto_resposta = "Essas são as matérias mais lidas no UOL agora: \n"
             for item in mensagem_final.split('\n')[:-1]:
                 texto_resposta += f"{item}\n"
                                                          
        elif text.lower().strip() in ["receber notícias", "receber notícias", "recber notícias", "receer notícias", "recebr notícias", "receber notcías", "receber notícias", "receber notíias", "receber notícas", "reecber notícias", "receber notíciás", "recebr notícas", "notícias", "receber"]:
             texto_resposta = "Oi, sobre o que você quer ler? Escolha uma categoria: /esportes /economia /noticias /entretenimento /mais-lidas"
                                                   
        elif text.lower().strip() in ["obrigado", "obrigada", "grato", "grata", "gratidão", "valeu", "valeu, véinho", "tchau"]:
            texto_resposta = "Se quiser ler mais notícias, mande um oi aqui! ( ͡ᵔ ͜ʖ ͡ᵔ)"
        
        elif text.lower().strip() in ["oi", "olá", ".", "salve", "ola", "hello", "hi", "oi, tudo bem?", "olá, td bem?", "oi, tudo bom?", "tudo bom?", "td bem?", "io"]:
            texto_resposta = "Oi! Este é o bot do UOL  ( ͡❛ ͜ʖ ͡❛) Você quer receber as notícias principais notícias do UOL agora? /sim ou /nao"
            
        else:
            texto_resposta = "Não entendi o que você quis dizer! Eu ainda estou aprendendo :) Enquanto isso, visite o www.uol.com.br e fique por dentro do que está acontecendo no Brasil e no mundo."

        nova_mensagem = {"chat_id": chat_id, "text": texto_resposta}
        
        # Requisita que a API do Telegram mande a mensagem
        resposta = requests.post(f"https://api.telegram.org./bot{TELEGRAM_API_KEY}/sendMessage", data=nova_mensagem)
        print(resposta.text)
        return "ok"
