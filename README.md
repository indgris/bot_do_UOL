# Bot de Notícias UOL: As Mais Lidas no Telegram

Este é um projeto de bot do Telegram que fornece as notícias mais lidas e destaques das categorias esportes, economia, política e entretenimento do site UOL. O bot realiza a raspagem das notícias e as envia para os usuários por meio de comandos específicos.

## Funcionalidades

- Raspagem das notícias mais lidas no site UOL
- Raspagem dos destaques de esportes
- Raspagem dos destaques de economia
- Raspagem dos destaques de notícias
- Raspagem dos destaques de Splash
- Envio das notícias mais lidas para os usuários do Telegram
- Comandos simples para interação com o bot
- Resumo de informações sobre o serviço na página: https://universo-online-bot.onrender.com/

## Requisitos

- Python 3.11.3
- Flask
- Beautiful Soup
- requests
- datetime

## Uso

1. Envie uma mensagem para o bot no Telegram. Você pode encontrá-lo em https://t.me/universo_online_bot.

2. Use os seguintes comandos:

   - `/start`: Inicia a interação com o bot.
   - `/sim`: Permite escolher sobre quais notícias o usuário poderá ler.
   - `/nao`: Cancela o recebimento das notícias.
   - `/esportes`: Receber os destaques de esportes.
   - `/economia`: Receber os destaques de economia.
   - `/noticias`: Receber as principais notícias do UOL.
   - `/entretenimento`: Receber os destaques de entretenimento.
   - `/populares`: Receber as notícias mais lidas no UOL.
   - `receber notícias`: Solicita as notícias.
   - `obrigado`, `obrigada`, `grato`, `grata`, `gratidão`, `valeu`, `valeu, véinho`, `tchau`: Agradece ao bot e encerra a interação.

3. Caso o bot não compreenda sua mensagem, ele responderá com uma mensagem padrão sugerindo que você visite o site do UOL.

## Mais informações
Este é um projeto de conclusão da disciplina Algoritmos de Automação, ministrada por Álvaro Justen, no Master em Jornalismo de dados, automação e data storytelling do Insper.
