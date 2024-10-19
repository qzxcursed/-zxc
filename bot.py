import telebot

token = "7342975986:AAEarkOB-0xpKuEjkWC6e7_nHB8DbrBoZLE"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.infinity_polling()