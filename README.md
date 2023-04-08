# UOL Notícias Mais Lidas Telegram Bot

Este projeto é um bot do Telegram que fornece as notícias mais lidas do site UOL. O bot realiza a raspagem das notícias mais lidas e as envia para os usuários por meio de comandos específicos.

## Funcionalidades

- Raspagem das notícias mais lidas no site UOL
- Envio das notícias mais lidas para os usuários do Telegram
- Comandos simples para interação com o bot

## Requisitos

- bs4
- datetime
- flask
- gunicorn
- requests

##Quer usar o código? Não se esqueça de:

- Criar o token do seu robô no Telegram
- Configurar o setWebhook do Telegram
- Configurando o webhook do Telegram
- Execute o seguinte código:

```
import requests

token = "SEU TOKEN"
url = "https://site-teste-turicas.onrender.com/telegram-bot"
response = requests.post(f"https://api.telegram.org/bot{token}/setWebhook", data={"url": url})
print(response.text)

```

## Comandos do bot

- `/start`: Inicia a interação com o bot e apresenta uma mensagem de boas-vindas
- `/sim`: Envia as notícias mais lidas do UOL no momento

## Mais informações
Este é um projeto de conclusão da disciplina Algoritmos de Automação, ministrada por Álvaro Justen, no Master em Jornalismo de dados, automação e data storytelling do Insper.
