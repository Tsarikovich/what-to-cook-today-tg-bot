from telebot import types


class MainKeyboard:
    eng_keyboard = types.InlineKeyboardMarkup()
    eng_keyboard.add(types.InlineKeyboardButton('Get a random meal', callback_data='get'))
    eng_keyboard.add(types.InlineKeyboardButton('Add a meal', callback_data='add'))
    eng_keyboard.add(types.InlineKeyboardButton('Delete a meal', callback_data='del'))
    eng_keyboard.add(types.InlineKeyboardButton('Show your meal list', callback_data='show'))

    ru_keyboard = types.InlineKeyboardMarkup()
    ru_keyboard.add(types.InlineKeyboardButton("Что сегодня приготовить ?!", callback_data='get'))
    ru_keyboard.add(types.InlineKeyboardButton("Добавить блюдо в список", callback_data='add'))
    ru_keyboard.add(types.InlineKeyboardButton("Удалить блюдо", callback_data='del'))
    ru_keyboard.add(types.InlineKeyboardButton("Показать список блюд", callback_data='show'))

    langs = {'eng': eng_keyboard, 'ru': ru_keyboard}


class LanguageOptionKeyboard:
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('English 🇺🇸', callback_data='lang:eng'))
    keyboard.add(types.InlineKeyboardButton('Русский 🇷🇺', callback_data='lang:ru'))
