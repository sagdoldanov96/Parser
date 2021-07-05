import telebot
import requests
from bs4 import BeautifulSoup as BS


r=requests.get('https://sinoptik.ua/погода-алматы')
html=BS(r.content,'html.parser')
bot = telebot.TeleBot("1834719208:AAEFv_0SBS3vg2DNAg1v8KF-zOKoJqYy2jw")

for element in html.select('#content'):
    today_temp = element.select('.wMain .today-temp')[0].text
    t_min = element.select('.temperature .min')[0].text
    t_max = element.select('.temperature .max')[0].text
    text = element.select('.wDescription .description')[0].text



@bot.message_handler(commands=['start'])
def start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start')
    bot.send_message(message.from_user.id, "Привет, {0.first_name}!".format(message.from_user),reply_markup=user_markup)
    bot.send_message(message.from_user.id, "Погода на сегодня:\n" + today_temp+'\n'+ t_min +',' + t_max + '\n' + text)


bot.polling(none_stop=True)
