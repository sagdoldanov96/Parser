import telebot
from selenium import webdriver

driver=webdriver.Chrome('/Users/Asus/PycharmProjects/Youtube/chromedriver.exe')
bot=telebot.TeleBot("1805101440:AAFlyoCfJWiCt-MNduHYv6pwCag4tvgls_Y")

@bot.message_handler(commands=['start'])
def start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start','/search_videos')
    bot.send_message(message.from_user.id, "Привет, {0.first_name}!".format(message.from_user),reply_markup=user_markup)

@bot.message_handler(commands=['search_videos'])
def search_videos(message):
    msg=bot.send_message(message.chat.id,"Введите текст, который вы хотите найти в YouTube")
    bot.register_next_step_handler(msg,search)

@bot.message_handler(commands=['search'])
def search(message):
    bot.send_message(message.chat.id,"Начинаю поиск")
    video_href="https://www.youtube.com/results?search_query="+message.text
    driver.get(video_href)

    videos = driver.find_elements_by_id("video-title")
    for i in range(len(videos)):
        bot.send_message(message.chat.id, videos[i].get_attribute('href'))
        if i==10:
            break

bot.polling()
