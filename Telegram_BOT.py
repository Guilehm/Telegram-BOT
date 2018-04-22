import telepot
from Chatbot import Chatbot
from key import botkey

telebot = telepot.Bot(botkey)
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
