import telebot
from config import*
from extensions import*
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Здрфвствуйте!\n Я помогу Вам\n рвзобраться с курсом.\n Чтобы посмотреть валюты\n с которыми я рвботаю\n " \
           "введите: /values "
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Вот валюты с которыми я работаю:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException(message,f'Неверное количество параметров!')

        answer = Convertor.get_price(*values)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, answer)


bot.polling()
