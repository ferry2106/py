import telebot

bot = telebot.TeleBot("7747533951:AAEoNJpuwaAjWA3cUwYW_JdGG-ymWjKIP54")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, Selamat datang di channel vincent.text)

bot.infinity_polling()
