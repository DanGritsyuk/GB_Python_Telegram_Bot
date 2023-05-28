import os
import telebot

from SaveloadFile import SaveloadFile

bot = telebot.TeleBot(SaveloadFile.LoadFromFile("bot.key"))

questions = list(SaveloadFile.JsonLoadFromFile('Data/questions.txt'))

for question in questions:
    for userId, text in question.items():
        os.system('cls')
        print(text, end='\n\n')
        answer = input('Ответ:\n')
        bot.send_message(userId, answer)