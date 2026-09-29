import os
import telebot
from telebot import types

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(types.KeyboardButton('Сделать заказ'))
    keyboard.row(types.KeyboardButton('Прайс'))
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Я бот для приёма заказов на прохождение Genshin Impact.\n"
        "Выбери, что тебя интересует:"
    )
    bot.send_message(message.chat.id, text, reply_markup=main_menu())

@bot.message_handler(func=lambda m: m.text == 'Прайс')
def price(message):
    text = (
        "*Наши услуги:*\n\n"
        "*Прохождение Арен/Горнило Безысходности:*\n Три арены - 300💠/ 10р \n Пять арен - 600💠/ 20р \nЗоны в открытом мире - 300💠/ 10р\n\n"
        "*Прохождения эха* - 300💠/10р \n Оплата производится только после скрина выполнения."
        "*Прохождение сюжета:*\n Мондштадт - 300💠/10р \n Ли Юэ - 600💠/ жемчужный гимн🐚/ 20р \nИнадзума - 600💠/ жемчужный гимн🐚/ 20р \nСумеру - 980💠/ 30р \nФонтейн - 980💠/ 30р \nНатлан - 980💠/ 30р \nНoд Край - 1980💠/ 60р \nСнежная (1-4 глава) - 600💠/ жемчужный гимн🐚/ 20р\n\n"
        "*Зачистка локаций:*\nСнежная (7.0) - 980💠/ 30р \nНод Край (6.0) - 980💠/ 30р \nНод Край (6.3) - 980💠/ 30р \nМорозная луна - 980💠/ 30р \nХрам пространства- 980💠/ 30р \nПо поводу зачистки других регионов еще неизвестно. \nЦена может меняться в зависимости от прогресса исследования.\n\n"
        "*Сборка персонажа* - Минимальная цена - 300💠/ 10р. \nМожет меняться в зависимости от сета и персонажа."
    )
    bot.send_message(message.chat.id, text, parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == 'Сделать заказ')
def order(message):
    msg = bot.send_message(
        message.chat.id,
        "Напиши свой заказ одним сообщением."
    )
    bot.register_next_step_handler(msg, save_order)

def save_order(message):
    order_text = message.text
    ADMIN_ID = 5018715734

    bot.send_message(
        message.chat.id,
        "✅ Спасибо! Твой заказ принят. Я свяжусь с тобой в ближайшее время."
    )
    bot.send_message(
        ADMIN_ID,
        f"🔔 *Новый заказ!*\n\n"
        f"От: {message.from_user.first_name} (@{message.from_user.username})\n"
        f"ID: {message.from_user.id}\n\n"
        f"Заказ:\n{order_text}",
        parse_mode='Markdown'
    )

@bot.message_handler(content_types=['text'])
def other(message):
    bot.send_message(
        message.chat.id,
        "Я тебя не понял 🤔 Используй кнопки ниже или напиши /start"
    )

print("Бот запущен... ✅")
# ВАЖНО: Здесь больше нет bot.infinity_polling()
