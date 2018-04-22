import telepot
from Chatbot import Chatbot

telebot = telepot.Bot('560759619:AAEHui3g5uMsq7hIWc0VZvVIacTJK_SS0NI')
bot = Chatbot('GuilehmBot')

def recebendo_msg(msg):
    frase = bot.escuta(frase=msg['text'])
    resposta = bot.pensa(frase)
    bot.fala(resposta)
    # chatID = msg['chat']['id']
    telepot.glance(msg)
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    telebot.sendMessage(chatID, resposta)

telebot.message_loop(recebendo_msg)

while True:
    pass
