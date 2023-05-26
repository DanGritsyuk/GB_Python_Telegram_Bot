import telebot
import requests
import time

from SaveloadFile import SaveloadFile
from Game import Game

bot = telebot.TeleBot(SaveloadFile.LoadFromFile("bot.key"))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	

@bot.message_handler(content_types=['text'])
def text_message(message):
    messageText = str(message.text)
    SaveloadFile.SaveToFile('log.txt', f'{message.from_user.first_name} {message.from_user.last_name}: {messageText}\n')
    if messageText.lower() == 'игра':
        game.NewGame(message.from_user.id)
        bot.reply_to(message, 'Ок, угадай число! от 1 до 1000')
    elif not game.over and message.from_user.id == game.userId:
        if messageText.isnumeric():
            answer = game.Check(int(messageText))
            bot.reply_to(message, answer)
        else:
            bot.reply_to(message, 'Эй, это не число!')


game = Game()
bot.polling()