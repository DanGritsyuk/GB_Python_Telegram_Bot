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
    if messageText.lower() == 'игра' and game.over:
        game.NewGame(message.from_user.id)
        bot.reply_to(message, 'Ок, угадай число! от 1 до 1000')
    elif not game.over and message.from_user.id == game.userId:
        if messageText.isnumeric():
            answer = game.Check(int(messageText))
            bot.reply_to(message, answer)
        elif messageText.lower() == 'сдаюсь':
            game.over = True
            bot.reply_to(message, f'Ну, ок... Число было: {game.number}, ты сдался на {game.attemptsCount} попытке.')
        else:
            bot.reply_to(message, 'Эй, это не число!')
    else:
        SaveloadFile.JsonSaveToFile(f'Data/questions.txt', {message.from_user.id : messageText})
        bot.send_message(message.from_user.id, 'Обращение принято! Оператор ответит в ближайшее время.')



game = Game()
bot.polling()