import telebot
from config import keys, TOKEN
from extensions import ConversionException, CryptoConverter 


bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands = ['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу дайте боту компанду в следующем формате:\n<Нзвание валюты, которая имеется> \
<Название валюты в которую надо отконвертировать> \
<Результат конвертации> \nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands = ['values'])
def values(message: telebot.types.Message):
    text = 'Доступные Валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types = ['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConversionException('СЛишком много параметров')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)


    except ConversionException as e:
        bot.reply_to(message,  f'Ошибка пользователя.\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать компанду\n{e}')
    
    else:

        result = float(amount)*float(total_base)
        result = round(result,2)
        text = f'Цена {amount} {quote} в {base} по кросс курсу- {total_base}, получится: {result} {base} '
        bot.send_message(message.chat.id, text)


bot.polling()