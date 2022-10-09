import random
import time
from functools import reduce
import telebot
import os
import pymongo
from pymongo.server_api import ServerApi
from telebot import types
from replies import messages_chain
from keyboards import MainKeyboard, LanguageOptionKeyboard

bot = telebot.TeleBot(os.getenv('TG_BOT_TOKEN'), parse_mode=None)
db_client = pymongo.MongoClient(
    f"mongodb+srv://{os.getenv('MONGODB_CREDENTIALS')}@cluster0.ybjnnvs.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi('1'))

collection = db_client['Users']['UsersData']


@bot.message_handler(commands=['start'])
def start(message):
    reply_description = "Language / Язык:"
    bot.send_message(message.chat.id, text=reply_description, reply_markup=LanguageOptionKeyboard.keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith("lang:"))
def setup_language(call):
    lang = call.data.replace('lang:', '')
    create_user(call.from_user.id, lang)
    bot.send_message(call.from_user.id, text=messages_chain[lang]['LangSet'], reply_markup=MainKeyboard.langs[lang])


def get_user_lang(user_id):
    if if_user_exists(user_id):
        return collection.find_one({'User': user_id})['Lang']
    else:
        start()


def if_user_exists(user_id):
    return collection.find_one({'User': user_id})


def create_user(user_id, lang):
    if not if_user_exists(user_id):
        collection.insert_one({'User': user_id, 'Meals': [], 'Lang': lang})
    else:
        collection.update_one({'User': user_id}, {"$set": {'Lang': lang}})


@bot.callback_query_handler(func=lambda call: call.data == 'get')
def get_random_meal(call):
    lang = get_user_lang(call.from_user.id)

    bot.send_message(call.from_user.id, text=messages_chain[lang]['Get'][0])
    user_meals_list = collection.find_one({'User': call.from_user.id})['Meals']

    if len(user_meals_list) == 0:
        bot.send_message(call.from_user.id, text=messages_chain[lang]['Get'][1])
        return

    time.sleep(1)
    bot.send_message(call.from_user.id, text=messages_chain[lang]['Get'][2])
    meal = random.choice(user_meals_list)
    time.sleep(1)
    bot.send_message(call.from_user.id, text=messages_chain[lang]['Get'][3] + f"*{meal}*",
                     parse_mode='Markdown')
    time.sleep(1)
    bot.send_message(call.from_user.id, text=messages_chain[lang]['Get'][4])


@bot.callback_query_handler(func=lambda call: call.data == 'add')
def add_meal(call):
    lang = get_user_lang(call.from_user.id)
    message = bot.send_message(call.from_user.id, text=messages_chain[lang]['Add'][0])
    message.lang = lang
    bot.register_next_step_handler(message, read_meal_and_add)


def read_meal_and_add(message):
    lang = message.lang
    meal = message.text.lower().strip()
    collection.update_one({'User': message.from_user.id}, {"$push": {'Meals': meal}})
    bot.send_message(message.from_user.id,
                     text=messages_chain[lang]['Add'][1])


@bot.callback_query_handler(func=lambda call: call.data == 'del')
def delete_meal(call):
    lang = get_user_lang(call.from_user.id)
    meals = collection.find_one({'User': call.from_user.id})['Meals']

    if len(meals) == 0:
        bot.send_message(call.from_user.id, text=messages_chain[lang]['Delete'][0])
        return

    delete_items_keyboard = telebot.types.InlineKeyboardMarkup()
    for meal in meals:
        delete_items_keyboard.add(types.InlineKeyboardButton(meal.capitalize(), callback_data=f'{lang}@{meal}'))

    bot.send_message(call.from_user.id, text=messages_chain[lang]['Delete'][1],
                     reply_markup=delete_items_keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('$#@!'))
def commit_delete(call):
    lang, meal = call.data.split('@')
    meal = meal.lower().strip()
    collection.update_one({'User': call.from_user.id}, {"$pull": {'Meals': meal}})
    bot.send_message(call.from_user.id, text=messages_chain[lang]['Delete'][2])


@bot.callback_query_handler(func=lambda call: call.data == 'show')
def show_meal(call):
    lang = get_user_lang(call.from_user.id)
    meals = collection.find_one({'User': call.from_user.id})['Meals']

    if len(meals) == 0:
        bot.send_message(call.from_user.id, text=messages_chain[lang]['Show'][0])
        return

    result = reduce(
        lambda str1, str2: str1.capitalize() + str2.capitalize() + f'\n{random.choice(["🍫", "🍟", "🥩", "🍓"])}\n', meals,
        "")
    bot.send_message(call.from_user.id, text=messages_chain[lang]['Show'][1] + result)


@bot.message_handler(commands=['menu'], func=lambda m: True)
def trigger(message):
    lang = get_user_lang(message.from_user.id)
    bot.send_message(message.chat.id, text=messages_chain[lang]['Menu'], reply_markup=MainKeyboard.langs[lang])


def main():
    bot.polling()
