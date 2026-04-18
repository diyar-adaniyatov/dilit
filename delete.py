import telebot

TOKEN = "8776900909:AAFtxahSFIqkoXZJHrxwtwYtaJJGtId0We0"
MY_ID = 8405286126

bot = telebot.TeleBot(TOKEN)

def is_owner(message):
    return True


OWNER_ID = 8405286126

def allowed(message):
    return message.from_user.id in [OWNER_ID]
@bot.message_handler(func=lambda message: not allowed(message))
def deny(message):
    bot.send_message(message.chat.id, "❌ У вас нет доступа к этому боту.")

@bot.message_handler(commands=['start'], func=is_owner)
def start(message):
    bot.send_message(message.chat.id, "Бот работает, добавьте его в группу и выдайте права администратора👑")


@bot.message_handler(content_types=['dice'], func=is_owner)
def handle_dice(message):
    if message.dice.emoji == "🎰":
        if message.dice.value == 64:
            bot.delete_message(message.chat.id, message.message_id)


bot.infinity_polling()
