import telebot
import time

bot_token = 'your_token'

bot = telebot.TeleBot(bot_token)

chars = "abcdefghijklmnopqrstuvwxyz?!@#$%^&*()_+|?\/ "

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Send me your iranian grade and I will convert it to german grade")


@bot.message_handler(content_types=['text'])
def cal_grade(message):
    pm = 7 - (0.3 * float(message.text))
    text = message.text
    chat_id = message.chat.id
    try:
        inp = int(text)
        bot.send_message(chat_id, "Your Iranian grade is equivalent to : \n\n" + str("{:.2f}".format(pm)) + "\n\nin German grade."
        "\n\n\nyou can also check it for yourself using the equation below:\n\n"
        "     7 - (0.3 * your grade)  \n\n\n\n\n"
        "     1 - 1.5 ➡️ 90 - 100\n\n\n     1.51 - 2.5 ➡️ 80 - 90\n\n\n     2.51 - 3.5 ➡️ 70 - 80\n\n\n     3.51 - 4 ➡️ 60 - 70\n\n\n     4.01 - 5➡️ 50-60")
        if pm < 2:
            bot.reply_to(message, "Congrats! You look like a bookworm 🤓")
        elif 2.01 <= pm <= 2.5:
            bot.reply_to(message, "Nice grade pal")
            bot.send_message(chat_id, "👍🏻")
        elif 2.51 <= pm:
            bot.reply_to(message, "Try to study a bit harder 🙂")
            bot.send_message(chat_id, "💩")
        else:
            bot.send_message(chat_id, "hmmm..")
    except ValueError:
        try:
            inp = float(text)
            bot.send_message(chat_id, "Your Iranian grade is equivalent to : \n\n" + str("{:.2f}".format(pm)) + "\n\nin German grade."
            "\n\n\nyou can also check it for yourself using the equation below:\n\n"
            "     7 - (0.3 * your grade)  \n\n\n\n\n"
            "     1 - 1.5 ➡️ 90 - 100\n\n\n     1.51 - 2.5 ➡️ 80 - 90\n\n\n     2.51 - 3.5 ➡️ 70 - 80\n\n\n     3.51 - 4 ➡️ 60 - 70\n\n\n     4.01 - 5➡️ 50-60")
            if pm < 2:
                bot.reply_to(message, "Congrats! You look like a bookworm 🤓")
            elif 2.01 <= pm <= 2.5:
                bot.reply_to(message, "Nice grade pal")
                bot.send_message(chat_id, "👍🏻")
            elif 2.51 <= pm:
                bot.reply_to(message, "Try to study a bit harder 🙂")
                bot.send_message(chat_id, "💩")
            else:
                bot.send_message(chat_id, "hmmm..")
        except ValueError:
            bot.send_message(chat_id, "Please send me a valid number. Not text!")


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(2)
