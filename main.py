import re
from slugify import slugify
import telebot
import  requests

from pdf_generator import PdfGenerator

# Создаем экземпляр бота
bot = telebot.TeleBot('Your Token')
# Функция, обрабатывающая команду /start

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Присылай ссылку )')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):

    try:

        page_content = requests.get(url=message.text).text

        name_st = re.search(r".*?<title>(.*?)</title>.*", page_content)[0]
        name_st = slugify(name_st.strip()[7:-8], allow_unicode=True)

        pdf_file = PdfGenerator([message.text]).main()
        with open(f'C:\\Users\{name_st}.pdf', "wb") as outfile:
            outfile.write(pdf_file[0].getbuffer())

    except BaseException as e:
        bot.send_message(message.chat.id, e)
# Запускаем бота
bot.polling(none_stop=True, interval=0)

