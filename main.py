import qrcode
import telebot
from datetime import datetime

TOKEN = ''
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, 'Just send text and get QR-code!')


@bot.message_handler(content_types='text')
def make_qr(message):
    filename = datetime.now().strftime(f"{message.from_user.id}_%m_%d_%H_%M_%S.png")
    img = qrcode.make(message.text)
    img.save(f'photos/{filename}')
    bot.send_photo(message.chat.id, open(f'photos/{filename}', 'rb'), caption="Here's Your QR-code!")
    bot.send_message(message.chat.id, 'Send text and get QR-code!')


bot.infinity_polling()
